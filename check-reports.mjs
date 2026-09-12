import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {execFileSync} from 'node:child_process';
import {getCases,getFreeCase,words} from './dist/content.js';
import {learningMap} from './dist/data/learning-map-data.js';
import {textFields,localDate,validDate,validateSession,sanitizeSession,summarizeSessions,mergeBackup,escapeHtml} from './dist/reports.js';

const cases=getCases('en');
for(const lang of ['en','zh']){
  const localized=getCases(lang);
  assert.equal(localized.length,22);
  assert.equal(new Set(localized.map(c=>c.id)).size,22);
  assert.equal(localized.filter(c=>c.ltl).length,18);
  for(const node of learningMap.topics)assert.equal(localized.filter(c=>c.skillId===node.id).length,1);
  for(const c of localized){
    for(const key of ['title','summary','materials','question','skillName'])assert.equal(typeof c[key],'string',`${lang} ${c.id} ${key}`);
    assert.equal(c.observations.length,3);assert.equal(c.steps.length,3);
    assert(c.observations.every(s=>typeof s==='string'&&s.trim()));
    assert(c.steps.every(s=>s.length===2&&s.every(t=>typeof t==='string'&&t.trim())));
    assert(Number.isInteger(c.sourceLine));
  }
}
assert.deepEqual(Object.keys(words.en).sort(),Object.keys(words.zh).sort());
const fields=Object.fromEntries(textFields.map(k=>[k,'']));
const sample={id:'test-one',caseId:'little-teacher',age:8,date:localDate(),fields,
  rows:[{rating:'independent',evidence:'Explained the rules using a new example.'},{rating:'supported',evidence:'After a question, checked what I understood.'},{rating:'unknown',evidence:''}]};
assert(validateSession(sample,cases));
assert(!validateSession({...sample,rows:sample.rows.map(r=>({...r,rating:'unknown'}))},cases));
assert(!validateSession({...sample,rows:sample.rows.map(r=>({...r,evidence:''}))},cases));
assert(!validateSession({...sample,caseId:'not-a-case'},cases));
assert(!validateSession({...sample,date:'2025-02-30'},cases));
assert(!validDate('9999-01-01'));assert(!validDate('2025-1-1'));
assert.equal(sanitizeSession({...sample,id:''},cases),null);
assert.equal(sanitizeSession({...sample,fields:{goal:3}},cases).fields.goal,'');

const one=summarizeSessions([sample],cases);
assert.equal(one.observed,2);assert.equal(one.unknown,1);
assert.equal(one.evidence.length,2);assert.equal(one.skills,1);
assert.equal(one.bySkill[0].independentSessions,1);
// Multiple observations in one session must not become repeated-session evidence.
const allIndependent={...sample,rows:sample.rows.map(r=>({rating:'independent',evidence:r.evidence||'Another example.'}))};
assert.equal(summarizeSessions([allIndependent],cases).bySkill[0].independentSessions,1);
const onlySupported={...sample,id:'test-two',date:'2026-01-02',rows:sample.rows.map(r=>({rating:'supported',evidence:'Needed a reminder.'}))};
const mixed=summarizeSessions([sample,onlySupported,{...onlySupported,id:'test-three',date:'2026-01-03'}],cases);
assert.equal(mixed.bySkill[0].sessions,3);
assert.equal(mixed.bySkill[0].independentSessions,1);
assert.equal(mixed.bySkill[0].independentDates.length,1);
const repeated=summarizeSessions([sample,{...sample,id:'day-two',date:'2026-01-02'},{...sample,id:'day-three',date:'2026-01-03'}],cases);
assert.equal(repeated.bySkill[0].independentSessions,3);
assert.equal(repeated.bySkill[0].independentDates.length,3);
assert.equal(summarizeSessions([],cases).observed,0);
// Restore is idempotent and cannot overwrite newer edits with an old backup.
const backup={format:'learning-together-v2',sessions:[sample,onlySupported]};
const current=[{...sample,fields:{...fields,goal:'Current edit'}}];
const restored=mergeBackup(current,backup,cases);
assert.equal(restored.length,2);assert.equal(restored[0].fields.goal,'Current edit');
assert.equal(mergeBackup(restored,backup,cases).length,2);
assert.throws(()=>mergeBackup(current,{...backup,sessions:[{...sample,caseId:'missing'}]},cases));
assert.equal(current.length,1);
// A child-led activity must survive restoration with its title and plan,
// without being counted as a taxonomy skill or requiring invented ratings.
const allCases=[...cases,getFreeCase('en')];
const ownIdea={...sample,id:'own-idea',caseId:'open-exploration',
  custom:{title:'Secret toy city',materials:'Cardboard',plan:'Connect homes with paper roads'},
  fields:{...fields,attempt:'Built two homes, then widened a road for the toy bus.'},
  rows:Array.from({length:3},()=>({rating:'unknown',evidence:''}))};
assert(validateSession(ownIdea,allCases));
const ownRestored=mergeBackup([],{format:'learning-together-v2',sessions:[ownIdea]},allCases)[0];
assert.deepEqual(ownRestored.custom,ownIdea.custom);
assert.equal(ownRestored.fields.attempt,ownIdea.fields.attempt);
assert.equal(summarizeSessions([ownRestored],allCases).skills,0);
assert.equal(summarizeSessions([ownRestored],allCases).observed,0);
assert.equal(summarizeSessions([ownRestored],allCases).sessions,1);
assert(!validateSession({...ownIdea,custom:{...ownIdea.custom,title:''}},allCases));
assert(!validateSession({...ownIdea,fields},allCases));
assert.equal(getFreeCase('zh').id,getFreeCase('en').id);
assert.equal(escapeHtml('<img src=x onerror="alert(1)">'), '&lt;img src=x onerror=&quot;alert(1)&quot;&gt;');

const html=fs.readFileSync('deliverables/一起长大.html','utf8');
for(const entry of ['dist/index.html','dist/studio.html'])assert.equal(fs.readFileSync(entry,'utf8'),html,`${entry} must also open without a server`);
assert.equal((html.match(/<script type="module">/g)||[]).length,1);
assert.equal((html.match(/<script type="application\/json"/g)||[]).length,1);
assert.equal((html.match(/<\/script>/g)||[]).length,2);
const script=html.match(/<script type="module">([\s\S]*?)<\/script>/)[1];
const checkPath=path.join(os.tmpdir(),'learning-studio-syntax.mjs');
fs.writeFileSync(checkPath,script);
execFileSync(process.execPath,['--check',checkPath]);
assert(!/^import /m.test(script));
assert(!html.includes('src="/studio.js"'));assert(!html.includes('href="/studio.css"'));
assert(html.includes('Designed by Lianghuan Bi(Hedy Bi)'));
console.log('PASS: 22 bilingual cases, all 18 skill mappings, evidence validation, observation counts, repeated-date evidence, idempotent backup restore, escaping and standalone module syntax.');
