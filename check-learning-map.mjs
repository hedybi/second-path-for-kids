import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {learningMap} from './dist/data/learning-map-data.js';
import {getLearningConnections} from './dist/learning-map.js';
import {activities} from './dist/data/activities.js';

const original=JSON.parse(fs.readFileSync('dist/data/learning-map-source.json','utf8'));
const ids=new Set(learningMap.topics.map(n=>n.id));
const allIds=new Set([...ids,...learningMap.externalTopics.map(n=>n.id)]);
assert.equal(ids.size,18);
assert.equal(learningMap.dependencies.length,25);
assert.equal(learningMap.dependencies.filter(e=>ids.has(e.prerequisiteId)).length,22);
assert.equal(new Set(learningMap.dependencies.map(e=>`${e.topicId}|${e.prerequisiteId}`)).size,25);
for(const e of learningMap.dependencies){assert(ids.has(e.topicId));assert(allIds.has(e.prerequisiteId));assert(['hard','soft'].includes(e.strength));assert(e.reasonZh);const o=original.dependencies.find(x=>x.sourceLine===e.sourceLine);assert.equal(e.topicId,o.topicId);assert.equal(e.prerequisiteId,o.prerequisiteId);assert.equal(e.strength,o.strength);assert.equal(e.reason,o.reason);}
const visiting=new Set(),done=new Set();
function visit(id){assert(!visiting.has(id),'Prerequisite graph must be acyclic');if(done.has(id))return;visiting.add(id);for(const e of learningMap.dependencies.filter(e=>e.topicId===id))visit(e.prerequisiteId);visiting.delete(id);done.add(id);}
for(const n of learningMap.topics){visit(n.id);assert(n.zh&&n.prompt&&n.description);if(n.activity)assert(activities.some(a=>a.id===n.activity));const raw=original.topics.find(t=>t.id===n.id);assert.equal(raw.name,n.name);assert.equal(raw.ageRangeStart,n.ageRangeStart);assert.equal(raw.ageRangeEnd,n.ageRangeEnd);}
const plan=getLearningConnections('mt_QR3vxbN1o4');
assert(plan.before.has('mt_8dstvf-KKb'));
assert(!plan.after.has('mt_8dstvf-KKb'));
assert(plan.after.has('mt_jIszRCO2ij'));
const teach=getLearningConnections('mt_6eTZUwKQZr');
assert(teach.before.has('mt_LE7nFEwS12'));
assert(teach.before.has('mt_S4G6GLKr1-'));
assert(teach.before.has('mt_kJ5wYzO8qC'));
assert(teach.after.has('mt_Y6P9y1Rz-u'));
assert(!teach.before.has('mt_6eTZUwKQZr'));
const html=fs.readFileSync('deliverables/一起长大.html','utf8');
assert(html.includes('id="learningMap"'));
assert(!html.includes('from \'./learning-map.js\''));
assert(!html.includes('href="/data/'));
assert.equal(JSON.parse(html.match(/<script type="application\/json" id="learningMapOriginal">([\s\S]*?)<\/script>/)[1]).topics.length,18);
fs.writeFileSync(path.join(os.tmpdir(),'family-map-offline-check.mjs'),html.match(/<script type="module">([\s\S]*?)<\/script>/)[1]);
console.log('PASS: source fidelity, 18 nodes, 22 internal edges, 3 external prerequisites, DAG, traversal direction, activity links and offline embedding.');
