/* Pure learning-state operations, also exercised by verify.cjs. */
const GrammarEngine = (() => {
  const fresh = () => ({attempts:[],hinted:false,solved:false});
  function answer(record, value, correct) {
    if (record.solved) return record;
    return {...record,attempts:[...record.attempts,value].slice(-8),solved:value===correct};
  }
  const assisted = r => !!r && (r.hinted || r.attempts.length>1 || (r.attempts.length>0 && !r.solved));
  const independent = r => !!r && r.solved && !assisted(r);
  function review(questions, transfer, records) {
    const tags = new Set(questions.filter((q,i)=>assisted(records[i])).map(q=>q.tag));
    return transfer.map((q,i)=>i).filter(i=>tags.has(transfer[i].tag));
  }
  function clean(raw, modules) {
    const s={version:1,module:0,mode:'learn',lesson:0,variant:0,progress:{}};
    if (!raw || raw.version!==1) return s;
    const int=(x,max)=>Number.isInteger(x)&&x>=0&&x<=max;
    if(int(raw.module,modules.length-1))s.module=raw.module;
    if(['learn','game','review'].includes(raw.mode))s.mode=raw.mode;
    if(int(raw.lesson,modules[s.module].lessons.length-1))s.lesson=raw.lesson;
    if(int(raw.variant,modules[s.module].lessons[s.lesson].variants.length-1))s.variant=raw.variant;
    modules.forEach(m=>{
      const p=raw.progress?.[m.id]; if(!p)return;
      const result={records:{},reviews:{},index:0,reviewIndex:0,queue:[]};
      [['records',m.questions],['reviews',m.transfer]].forEach(([key,bank])=>bank.forEach((q,i)=>{
        const r=p[key]?.[i];if(!r)return;
        const attempts=Array.isArray(r.attempts)?r.attempts.filter(a=>q.options.includes(a)).slice(-8):[];
        result[key][i]={attempts,hinted:!!r.hinted,solved:!!r.solved && attempts.at(-1)===q.answer};
      }));
      if(int(p.index,m.questions.length))result.index=p.index;
      result.queue=Array.isArray(p.queue)?[...new Set(p.queue.filter(i=>int(i,m.transfer.length-1)))]:[];
      if(int(p.reviewIndex,result.queue.length))result.reviewIndex=p.reviewIndex;
      s.progress[m.id]=result;
    });return s;
  }
  return {fresh,answer,assisted,independent,review,clean};
})();
if(typeof module!=='undefined'&&module.exports)module.exports=GrammarEngine;
