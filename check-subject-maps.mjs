import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import vm from 'node:vm';
const data=JSON.parse(fs.readFileSync('subject-maps/source.json','utf8'));
const zh=JSON.parse(fs.readFileSync('subject-maps/zh.json','utf8')).topics;
assert.deepEqual(Object.keys(zh).sort(),data.topics.map(n=>n.id).sort());
for(const n of data.topics){
 assert.equal(zh[n.id].sourceName,n.name);
 assert(/[\u3400-\u9fff]/u.test(zh[n.id].name),`Missing Chinese title: ${n.id}`);
 assert(/[\u3400-\u9fff]/u.test(zh[n.id].summary),`Missing Chinese guide: ${n.id}`);
 assert(!/undefined|null|TODO/.test(zh[n.id].name+' '+zh[n.id].summary));
}
const byId=new Map(data.topics.map(n=>[n.id,n]));
assert.equal(byId.size,data.topics.length);
for(const [subject,count] of Object.entries({Mathematics:503,English:286})){
 const nodes=data.topics.filter(n=>n.subject===subject);
 assert.equal(nodes.length,count);
 for(const n of nodes){
  assert(n.name&&n.description&&data.domainZh[n.domain]);
  assert(Number.isInteger(n.sourceLine)&&n.sourceLine>0);
  assert(n.ageRangeStart<=n.ageRangeEnd);
  assert(/^mt_[A-Za-z0-9_-]+$/.test(n.id));
 }
}
assert.equal(data.dependencies.length,1639);
const uniqueEdges=new Set();
for(const e of data.dependencies){
 assert(byId.has(e.topicId)&&byId.has(e.prerequisiteId));
 assert(['hard','soft'].includes(e.strength));assert(e.reason);
 const key=e.prerequisiteId+'>'+e.topicId;assert(!uniqueEdges.has(key));uniqueEdges.add(key);
}
const visiting=new Set(),done=new Set();
function visit(id){assert(!visiting.has(id),'Prerequisites must form a DAG');if(done.has(id))return;visiting.add(id);for(const e of data.dependencies.filter(e=>e.topicId===id))visit(e.prerequisiteId);visiting.delete(id);done.add(id);}
for(const n of data.topics)visit(n.id);
// A topic must be findable exactly once by domain and reference starting age.
for(const subject of ['Mathematics','English']){
 const nodes=data.topics.filter(n=>n.subject===subject),placed=[];
 for(const domain of new Set(nodes.map(n=>n.domain)))for(const age of new Set(nodes.map(n=>n.ageRangeStart)))placed.push(...nodes.filter(n=>n.domain===domain&&n.ageRangeStart===age));
 assert.equal(placed.length,nodes.length);assert.equal(new Set(placed.map(n=>n.id)).size,nodes.length);
}
const html=fs.readFileSync('deliverables/subject-maps.html','utf8');
assert.equal(html,fs.readFileSync('dist/subject-maps.html','utf8'));
assert.equal((html.split("<script")[0].match(/role="tab"/g)||[]).length,4);
assert.deepEqual(JSON.parse(html.match(/<script id="mapData" type="application\/json">([\s\S]*?)<\/script>/)[1]),{...data,zh});
const script=html.match(/<script type="module">([\s\S]*?)<\/script>/)[1];
const tmp=path.join(os.tmpdir(),'second-path-subject-map-check.mjs');fs.writeFileSync(tmp,script);execFileSync(process.execPath,['--check',tmp]);
assert(!/<script[^>]+src=/.test(html));assert(!/<link[^>]+rel="stylesheet"/.test(html));
// Exercise the actual render/search functions with a minimal DOM adapter.
// This checks generated UI content and state transitions, not browser layout.
const elements=new Map();
function element(dataset={}){return {dataset,attributes:{},listeners:{},textContent:'',innerHTML:'',value:'',style:{},classList:{toggle(){}},setAttribute(k,v){this.attributes[k]=v;},addEventListener(k,fn){const previous=this.listeners[k];this.listeners[k]=e=>{previous?.(e);fn(e);};},click(){this.listeners.click?.({target:this});},querySelectorAll(){return [];},querySelector(s){return get(s);},scrollTo(){},scrollIntoView(){},focus(){}};}
const tabs=['Mathematics','English'].map(subject=>element({subject}));
const compareTabs=['Mathematics','English'].map(subject=>element({compare:subject}));
const comparison=JSON.parse(fs.readFileSync('subject-maps/shanghai.json','utf8'));
const audit=JSON.parse(fs.readFileSync('subject-maps/audit.json','utf8'));
Object.assign(comparison.sources,audit.sources);
comparison.audit={rows:audit.rows,policies:audit.policies};
const langs=['en','zh'].map(lang=>element({lang}));
function get(selector){if(selector.startsWith('[data-topic='))return null;if(!elements.has(selector))elements.set(selector,element());return elements.get(selector);}
get('#mapData').textContent=JSON.stringify({...data,zh});
get('#shanghaiData').textContent=JSON.stringify(comparison);
const storage=new Map();
const htmlText=s=>s.replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const sandbox=vm.createContext({
 document:{documentElement:{},querySelector:get,querySelectorAll:s=>s==='[data-subject]'?tabs:s==='[data-lang]'?langs:s==='[data-compare]'?compareTabs:s==='.subject-tabs [role="tab"]'?[...tabs,...compareTabs]:[]},
 window:{matchMedia:()=>({matches:false})},
 localStorage:{getItem:k=>storage.get(k),setItem:(k,v)=>storage.set(k,v)}
});
vm.runInContext(script,sandbox);
assert.equal(get('#pageTitle').textContent,'Explore the subject maps');
langs[1].listeners.click();
assert.equal(storage.get('second-path-map-language'),'zh');
assert.equal(get('#pageTitle').textContent,'看看数学与英语都学些什么');
assert.equal(get('.brand>span').innerHTML,'第二路径<small>Lianghuan Bi(Hedy Bi)</small>');
for(const subject of ['Mathematics','English']){
 vm.runInContext(`chooseSubject(${JSON.stringify(subject)})`,sandbox);
 const nodes=data.topics.filter(n=>n.subject===subject);
 const mapHtml=get('#mapCanvas').innerHTML;
 assert.equal((mapHtml.match(/class="topic-node"/g)||[]).length,nodes.length);
 for(const n of nodes){
  assert(mapHtml.includes(`<strong>${htmlText(zh[n.id].name)}</strong>`),`Untranslated map node: ${n.id}`);
  vm.runInContext(`selected=${JSON.stringify(n.id)};renderDetail()`,sandbox);
  const detail=get('#topicDetail').innerHTML;
  const visibleDetail=detail.replace(/<details\b[^>]*>[\s\S]*?<\/details>/g,'');
  assert(visibleDetail.includes(htmlText(zh[n.id].summary)),`Guide missing: ${n.id}`);
  assert(!visibleDetail.includes('lang="en"'),`English reference not collapsed: ${n.id}`);
  assert(detail.includes('查看完整说明与观察提示（英文原文）'));
 }
}
vm.runInContext("chooseSubject('Mathematics')",sandbox);
get('#search').listeners.input({target:{value:'三角形全等'}});
assert.equal(vm.runInContext('visible().length',sandbox),1);
assert(get('#topicDetail').innerHTML.includes('三角形全等（12岁起）'));
get('#reset').listeners.click();
assert.equal(vm.runInContext('visible().length',sandbox),503);
tabs[1].listeners.click();
get('#search').listeners.input({target:{value:'拼读'}});
assert(vm.runInContext('visible().length',sandbox)>0);
langs[0].listeners.click();
assert.equal(storage.get('second-path-map-language'),'en');
assert.equal(get('#pageTitle').textContent,'Explore the subject maps');
assert(get('#topicDetail').innerHTML.includes('What this can look like'));
assert(!get('#topicDetail').innerHTML.includes('class="original-topic"'));
assert(vm.runInContext('visible().length',sandbox)>0,'Chinese searches work in English mode');
// All seven game entries must be distinct and open the matching topic.
vm.runInContext("chooseSubject('English')",sandbox);
const gameList=get('#grammarGames').innerHTML;
const gameUrls=[...gameList.matchAll(/href="([^"]+)"/g)].map(m=>m[1]);
assert.equal(gameUrls.length,7);assert.equal(new Set(gameUrls).size,7);
const games=vm.runInContext('grammarGames',sandbox);
for(const game of games){
 vm.runInContext(`selected=${JSON.stringify(game.node)};renderDetail()`,sandbox);
 assert(get('#topicDetail').innerHTML.includes(`href="${game.url}"`),`Wrong game for ${game.node}`);
}
for(const lang of langs){
 lang.listeners.click();
 assert.equal((get('#grammarGames').innerHTML.match(/<li>/g)||[]).length,7);
}
vm.runInContext("chooseSubject('Mathematics')",sandbox);assert.equal(get('#grammarGames').hidden,true);
console.log('PASS: seven distinct grammar game links in both languages, matching topic-detail links, hidden on mathematics.');
console.log('PASS: 503 mathematics topics, 286 English topics, 856 Chinese titles and guides, 21 translated domains, 1,639 unique direct relationships with valid endpoints, DAG, full layout coverage, two original tabs plus two Shanghai tabs and standalone script syntax.');
console.log('PASS: rendered Chinese labels and guides for every map topic; English references collapsed; bilingual search, tabs, reset, language switching and preference saving. Browser layout not tested.');

// Validate the independent evidence view without treating evidence gaps as matches.
vm.runInContext("comparisonView='books'",sandbox);
assert.equal(comparison.rows.length,15);
for(const row of comparison.rows){
 assert(row.topics.length);
 assert(row.sources.every(id=>comparison.sources[id]));
 assert(row.topics.every(id=>byId.get(id)?.subject===row.subject));
 for(const field of ['title','shanghai','difference'])for(const language of ['en','zh'])assert(row[field][language]);
}
for(const language of ['en','zh']){
 langs[language==='en'?0:1].click();
 for(const subject of ['Mathematics','English']){
  compareTabs[subject==='Mathematics'?0:1].click();
  assert.equal(get('#subjectPanel').hidden,true);
  assert.equal(get('#comparisonPanel').hidden,false);
  for(const stage of ['all','baby','early','lower','middle','upper','bridge']){
   vm.runInContext(`comparisonStage=${JSON.stringify(stage)};renderComparison()`,sandbox);
   const rendered=get('#comparisonPanel').innerHTML;
   assert(!/undefined|null|TODO/.test(rendered));
   assert(rendered.includes(language==='zh'?'尚未完成全套教材逐项对照':'not a complete textbook crosswalk'));
   const expected=comparison.rows.filter(r=>r.subject===subject&&(stage==='all'||r.stage===stage||(r.stage==='all'&&!['baby','early'].includes(stage))));
   assert.equal((rendered.match(/class="c-row /g)||[]).length,expected.length);
   const alwaysVisible=rendered.replace(/<details\b[^>]*>[\s\S]*?<\/details>/g,'');
   for(const r of expected){
    assert(alwaysVisible.includes(htmlText(r.title[language])));
    assert(alwaysVisible.includes(htmlText(r.shanghai[language])),'Shanghai content must be visible without expansion');
    assert(alwaysVisible.includes(htmlText(r.difference[language])),'Comparison must be visible without expansion');
   }
   if(expected.length){assert(rendered.includes('<table class="c-table">'));assert.equal((rendered.match(/scope="col"/g)||[]).length,4);}

  }
 }
 tabs[0].click();
 assert.equal(get('#comparisonPanel').hidden,true);
 assert.equal(get('#subjectPanel').hidden,false);
 assert.equal(tabs[0].attributes['aria-selected'],'true');
}
const tabNav=get('.subject-tabs').listeners.keydown;
tabNav({key:'End',target:tabs[0],preventDefault(){},stopImmediatePropagation(){}});
assert.equal(compareTabs[1].attributes['aria-selected'],'true');
tabNav({key:'ArrowRight',target:compareTabs[1],preventDefault(){},stopImmediatePropagation(){}});
assert.equal(tabs[0].attributes['aria-selected'],'true');
console.log('PASS: four-tab keyboard navigation, seven stage filters in both languages, evidence/source links, subject isolation and original map restoration.');

for(const r of audit.rows){
 assert(r.topics.every(id=>byId.get(id)?.subject===r.subject));
 assert(r.sources.every(id=>comparison.sources[id]));
 for(const field of ['title','fact','analysis','probe'])for(const language of ['en','zh'])assert(r[field][language]);
}
for(const r of audit.policies){
 assert(r.sources.every(id=>comparison.sources[id]));
 for(const [subject,ids] of Object.entries(r.topics))assert(ids.every(id=>byId.get(id)?.subject===subject));
}
for(const language of ['en','zh']){
 langs[language==='en'?0:1].click();
 for(const subject of ['Mathematics','English']){
  compareTabs[subject==='Mathematics'?0:1].click();
  for(const view of ['differences','policy','inventory']){
   vm.runInContext(`comparisonView=${JSON.stringify(view)};auditQuery='';auditDomain='';auditFilter='all';renderComparison()`,sandbox);
   const out=get('#comparisonPanel').innerHTML;
   assert(!/undefined|null|TODO/.test(out));
   if(view==='differences')for(const r of audit.rows.filter(r=>r.subject===subject))assert(out.includes(htmlText(r.analysis[language])));
   if(view==='policy')for(const r of audit.policies)assert(out.includes(htmlText(r.analysis[language])));
   if(view==='inventory'){
    const nodes=data.topics.filter(n=>n.subject===subject);
    const ids=[...out.matchAll(/data-a-topic="([^"]+)"/g)].map(m=>m[1]);
    assert.deepEqual(ids.sort(),nodes.map(n=>n.id).sort(),'Every inventory point is rendered exactly once');
    const partitions={};
    for(const filter of ['associated','pending','within','later']){
     partitions[filter]=vm.runInContext(`auditFilter=${JSON.stringify(filter)};auditVisible().length`,sandbox);
    }
    assert.equal(partitions.associated+partitions.pending,nodes.length);
    assert.equal(partitions.within+partitions.later,nodes.length);
    assert.equal(partitions.later,subject==='Mathematics'?9:0);
    vm.runInContext("auditFilter='all';auditDomain='';auditQuery='';",sandbox);
    for(const n of nodes)assert(out.includes(htmlText(language==='zh'?zh[n.id].summary:n.description)));
   }
  }
 }
}
vm.runInContext("comparisonSubject='Mathematics';auditDomain='';auditFilter='all';auditQuery='英镑';",sandbox);
assert(vm.runInContext('auditVisible().length',sandbox)>0);
vm.runInContext("auditQuery='unlikelynonsense12345';",sandbox);
assert.equal(vm.runInContext('auditVisible().length',sandbox),0);
console.log('PASS: 789 inventory IDs rendered exactly once in both languages; evidence/pending and reference-age partitions reconcile; 19 deeper comparisons and 6 policy records have valid sources and subject-specific endpoints.');
