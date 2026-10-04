const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const E=require('./engine.js');
const data=JSON.parse(fs.readFileSync(path.join(__dirname,'lessons.json'),'utf8'));
let checked=0;
for(const m of data){
  assert.equal(m.questions.length,12);
  for(const q of [...m.questions,...m.transfer]){
    const wrong=q.options.find(x=>x!==q.answer);
    let r=E.fresh();r=E.answer(r,q.answer,q.answer);
    assert(E.independent(r));assert.equal(E.answer(r,wrong,q.answer),r);
    r=E.answer(E.fresh(),wrong,q.answer);assert(!r.solved);assert(E.assisted(r));
    r=E.answer(r,q.answer,q.answer);assert(r.solved&&!E.independent(r));
    r=E.answer({...E.fresh(),hinted:true},q.answer,q.answer);assert(r.solved&&!E.independent(r));
    checked++;
  }
  const records={};m.questions.forEach((q,i)=>{
    records[i]=E.answer(E.fresh(),q.options.find(x=>x!==q.answer),q.answer);
    const queue=E.review(m.questions,m.transfer,records);
    assert(queue.some(j=>m.transfer[j].tag===q.tag));
    queue.forEach(j=>assert(!m.questions.some(x=>x.prompt===m.transfer[j].prompt)));
  });
  const saved={version:1,module:data.indexOf(m),mode:'review',lesson:4,variant:0,progress:{[m.id]:{records,index:0,reviews:{},queue:E.review(m.questions,m.transfer,records),reviewIndex:0}}};
  assert.deepEqual(E.clean(JSON.parse(JSON.stringify(saved)),data),saved);
}
assert.equal(E.clean({version:1,module:-50,lesson:999,variant:1000},data).module,0);
assert.deepEqual(E.clean(null,data),E.clean({version:999},data));
const all={version:1,module:0,mode:'game',lesson:0,variant:0,progress:{}};
for(const m of data){all.progress[m.id]={records:{},reviews:{},index:12,reviewIndex:m.transfer.length,queue:m.transfer.map((q,i)=>i)};for(const [key,bank] of [['records',m.questions],['reviews',m.transfer]])bank.forEach((q,i)=>{all.progress[m.id][key][i]=E.answer({...E.fresh(),hinted:true},q.answer,q.answer);});}
assert(Buffer.byteLength(JSON.stringify({privateContent:all,modelContent:{activity:'六个语法互动'}}))<16384);
console.log(`PASS: ${data.length} modules, ${checked} answers, retry/duplicate/hint handling, fresh-question reviews, restoration, malformed-state guards, 16 KiB state budget.`);
