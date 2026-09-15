const data=JSON.parse(document.querySelector('#mapData').textContent);
const subjects=['Mathematics','English'];
const all=new Map(data.topics.map(n=>[n.id,n]));
const $=s=>document.querySelector(s),esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let subject='Mathematics',lang='en',domain='',query='',selected='',positions=new Map();
try{if(localStorage.getItem('second-path-map-language')==='zh')lang='zh';}catch{}
const t=(en,zh)=>lang==='en'?en:zh;
const domainLabel=d=>lang==='zh'?(data.domainZh[d]||d):d;
const subjectNames={'Mathematics':'数学','English':'英语','History':'历史','Learning to Learn':'学会学习','Life Skills':'生活技能','Personal & Social Development':'个人与社会发展','Science':'科学'};
const subjectLabel=s=>t(s,subjectNames[s]||s);
const topicLabel=n=>lang==='zh'?data.zh[n.id].name:n.name;
const topicUrl=n=>'https://github.com/withmarbleapp/os-taxonomy/blob/main/data/topics.json#L'+n.sourceLine;
const inSubject=()=>data.topics.filter(n=>n.subject===subject);
const visible=()=>inSubject().filter(n=>(!domain||n.domain===domain)&&(!query||[n.name,data.zh[n.id].name,data.zh[n.id].summary,n.domain,data.domainZh[n.domain],n.description,n.id].join(' ').toLowerCase().includes(query.toLowerCase())));
function links(id){return {before:data.dependencies.filter(e=>e.topicId===id),after:data.dependencies.filter(e=>e.prerequisiteId===id)};}
function chooseSubject(s){subject=s;domain='';query='';selected='';$('#search').value='';render();$('#mapViewport').scrollTo(0,0);}
function render(){document.documentElement.lang=lang==='zh'?'zh-CN':'en';document.title=t('Second Path · Maths & English','第二路径 · 数学与英语');
 $('#pageTitle').textContent=t('Explore the subject maps','看看数学与英语都学些什么');$('#introText').textContent=t('Browse the original topics and see how they connect.','浏览知识点的中文导读，看看它们怎样相连。');
 $('.brand>span').innerHTML=`${t('Second Path','第二路径')}<small>Lianghuan Bi(Hedy Bi)</small>`;
 $('.brand').setAttribute('aria-label',t('Second Path home','第二路径首页'));$('#topicDetail').setAttribute('aria-label',t('Topic details','知识点详情'));
 $('#designer').textContent=t('Designed by Lianghuan Bi(Hedy Bi)','设计：Lianghuan Bi(Hedy Bi)');
 document.querySelectorAll('[data-lang]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.lang===lang)));
 document.querySelectorAll('[data-subject]').forEach(b=>{const on=b.dataset.subject===subject;b.setAttribute('aria-selected',String(on));b.tabIndex=on?0:-1;b.innerHTML=`${subjectLabel(b.dataset.subject)} <span>${data.counts[b.dataset.subject]}</span>`;});
 $('#subjectPanel').setAttribute('aria-labelledby',subject==='Mathematics'?'tab-math':'tab-english');$('#searchLabel').textContent=t('Find a topic','查找知识点');$('#search').placeholder=t('Try fractions, spelling… (English or Chinese)','搜索知识点或内容，如分数、拼读、几何…');$('#reset').textContent=t('Reset view','显示全部');$('#domainTitle').textContent=t('Domains','学习领域');
 $('#readingNote').textContent=t('English mode preserves the source text. Chinese mode offers adapted titles and concise reading guides; original English details remain available. Ages are references, not deadlines. This map does not assess your child.','中文标题与简述根据原始内容改编，便于快速了解，不是逐字翻译；完整英文说明、观察提示及关联理由可展开核对。年龄只作参考，不是达标期限，也不是测评。');
 $('#mapHint').textContent=t('Select a topic to show its direct connections.','点击知识点，显示它的直接关联。');$('#hardLabel').textContent=t('Required','必要基础');$('#softLabel').textContent=t('Helpful','辅助基础');$('#mapViewport').setAttribute('aria-label',t('Skill map. Scroll vertically and horizontally.','知识地图，可上下和左右滚动。'));
 const nodes=inSubject(),domains=[...new Set(nodes.map(n=>n.domain))];
 $('#domains').innerHTML=[['',t('All domains','全部领域'),nodes.length],...domains.map(d=>[d,domainLabel(d),nodes.filter(n=>n.domain===d).length])].map(([d,label,count])=>`<button data-domain="${esc(d)}" aria-pressed="${domain===d}">${esc(label)} <span>${count}</span></button>`).join('');
 $('#domains').querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{domain=b.dataset.domain;selected='';render();$('#mapViewport').scrollTo(0,0);}));
 const nodesShown=visible();if(!nodesShown.some(n=>n.id===selected))selected=nodesShown[0]?.id||'';
 const internal=data.dependencies.filter(e=>all.get(e.topicId)?.subject===subject&&all.get(e.prerequisiteId)?.subject===subject).length;
 $('#counts').textContent=t(`${nodesShown.length} / ${nodes.length} topics · ${domains.length} domains · ${internal} internal links`,`${nodesShown.length} / ${nodes.length} 个知识点 · ${domains.length} 个领域 · ${internal} 条学科内部关系`);
 $('#provenance').textContent=t('Original data: Marble Skill Taxonomy v1. Layout, Chinese titles and concise guides adapted for Second Path. Chinese adaptations: CC BY-SA 4.0. Third-party curriculum standard text is not included.','基于 Marble Skill Taxonomy v1。地图布局、中文标题与简述由第二路径改编；中文改编内容采用 CC BY-SA 4.0。未转载第三方课程标准原文。');
 drawMap(nodesShown);renderDetail();
}
function drawMap(nodes){const canvas=$('#mapCanvas');positions=new Map();if(!nodes.length){canvas.style.cssText='width:100%;height:400px';canvas.innerHTML=`<p class="empty-map">${t('No matching topics. Try a different word or reset the view.','没有匹配的知识点。试试其他词，或点击“显示全部”。')}</p>`;$('#mapFootnote').textContent='';return;}
 const ages=[...new Set(inSubject().map(n=>n.ageRangeStart))].sort((a,b)=>a-b),width=ages.length*196+40;
 let y=68,html=ages.map((age,i)=>`<div class="age-band" style="left:${22+i*196}px;width:174px">${t('From age ','参考起始年龄 ')}${age}</div>`).join('');
 for(const d of [...new Set(nodes.map(n=>n.domain))]){const group=nodes.filter(n=>n.domain===d);html+=`<div class="domain-band" style="top:${y}px;width:${width-44}px">${esc(domainLabel(d))}<span>${group.length}</span></div>`;y+=48;let rows=0;
  for(const [i,age]of ages.entries()){const col=group.filter(n=>n.ageRangeStart===age).sort((a,b)=>a.ageRangeEnd-b.ageRangeEnd||a.name.localeCompare(b.name));rows=Math.max(rows,col.length);col.forEach((n,j)=>{const p={x:22+i*196,y:y+j*102};positions.set(n.id,p);html+=`<button class="topic-node" data-topic="${n.id}" style="left:${p.x}px;top:${p.y}px" aria-label="${esc(topicLabel(n))}" title="${esc(topicLabel(n))}"><strong>${esc(topicLabel(n))}</strong><small>${n.ageRangeStart}–${n.ageRangeEnd} ${t('years','岁')}</small></button>`;});}
  y+=rows*102+25;
 }
 canvas.style.cssText=`width:${width}px;height:${y}px`;canvas.innerHTML=`<svg class="edge-layer" width="${width}" height="${y}" aria-hidden="true"><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8" fill="#accd87"/></marker></defs><g id="edges"></g></svg>`+html;
 canvas.querySelectorAll('[data-topic]').forEach(b=>b.addEventListener('click',()=>selectTopic(b.dataset.topic,false)));
 paintSelection();
}
function paintSelection(){const relation=links(selected),before=new Set(relation.before.map(e=>e.prerequisiteId)),after=new Set(relation.after.map(e=>e.topicId));
 document.querySelectorAll('.topic-node').forEach(b=>{b.classList.toggle('selected',b.dataset.topic===selected);b.classList.toggle('before',before.has(b.dataset.topic));b.classList.toggle('after',after.has(b.dataset.topic));b.setAttribute('aria-pressed',String(b.dataset.topic===selected));});
 const shown=[...relation.before,...relation.after].filter(e=>positions.has(e.prerequisiteId)&&positions.has(e.topicId));
 if($('#edges'))$('#edges').innerHTML=shown.map(e=>{const a=positions.get(e.prerequisiteId),b=positions.get(e.topicId);let path;if(a.x===b.x){const x=a.x+184;path=`M${a.x+174},${a.y+45} C${x+10},${a.y+45} ${x+10},${b.y+45} ${b.x+174},${b.y+45}`;}else{const right=b.x>a.x,sx=a.x+(right?174:0),ex=b.x+(right?0:174),mid=(sx+ex)/2;path=`M${sx},${a.y+45} C${mid},${a.y+45} ${mid},${b.y+45} ${ex},${b.y+45}`;}return `<path d="${path}" stroke="#accd87" stroke-width="2" fill="none" ${e.strength==='soft'?'stroke-dasharray="6 5"':''} marker-end="url(#arrow)"/>`;}).join('');
 $('#mapFootnote').textContent=t(`Arrows run from prerequisites to later topics. ${shown.length} of ${relation.before.length+relation.after.length} direct links are visible in this view; all direct relationships are listed in the details.`, `箭头从前置基础指向后续知识点。当前显示 ${shown.length} / ${relation.before.length+relation.after.length} 条直接关联；完整直接关系列在详情中。`);
}
function selectTopic(id,locate){const n=all.get(id);if(!n||!subjects.includes(n.subject))return;if(n.subject!==subject){subject=n.subject;domain='';query='';$('#search').value='';}else if(!visible().some(n=>n.id===id)){domain='';query='';$('#search').value='';}selected=id;if(!positions.has(id)||!document.querySelector(`[data-topic="${id}"]`)){render();}else{paintSelection();renderDetail();}
 if(locate){const p=positions.get(id);if(p)$('#mapViewport').scrollTo({left:Math.max(0,p.x-100),top:Math.max(0,p.y-100),behavior:'auto'});document.querySelector(`[data-topic="${id}"]`)?.focus({preventScroll:true});}
 if(window.matchMedia('(max-width:1150px)').matches&&!locate)$('#topicDetail').scrollIntoView({block:'start'});
}
function renderDetail(){const n=all.get(selected),el=$('#topicDetail');if(!n){el.innerHTML=`<p>${t('Select a topic to read its details.','请选择知识点查看详情。')}</p>`;return;}const relation=links(n.id);
 const group=(edges,before)=>edges.length?`<ul class="relations">${edges.map(e=>{
  const target=all.get(before?e.prerequisiteId:e.topicId),id=before?e.prerequisiteId:e.topicId;
  const name=target?topicLabel(target):id;
  const reason=lang==='zh'?`<details class="original-reason"><summary>查看关联理由（英文原文）</summary><p lang="en">${esc(e.reason)}</p></details>`:`<p>${esc(e.reason)}</p>`;
  return `<li>${target&&subjects.includes(target.subject)?`<button data-related="${id}">${esc(name)} ↗</button>`:`<a href="${target?topicUrl(target):'https://github.com/withmarbleapp/os-taxonomy/blob/main/data/topics.json'}" target="_blank" rel="noopener">${esc(name)} ↗</a>`}<span class="relation-tag">${e.strength==='hard'?t('Required foundation','必要基础'):t('Helpful foundation','辅助基础')}${target&&target.subject!==subject?' · '+esc(subjectLabel(target.subject)):''}</span>${reason}</li>`;
 }).join('')}</ul>`:`<p class="muted">${t('No direct relationship is listed in the source.','原始数据中未列出直接关系。')}</p>`;
 const original=`<p lang="en">${esc(n.description)}</p>${n.evidence?.length?`<h3>${t('What this can look like','观察提示（英文原文）')}</h3><ul lang="en">${n.evidence.map(s=>`<li>${esc(s)}</li>`).join('')}</ul>`:''}${n.assessmentPrompt?`<p lang="en" class="question">${esc(n.assessmentPrompt.replaceAll('{{name}}','your child'))}</p>`:''}`;
 const content=lang==='zh'?`<div class="chinese-guide"><h3>学习内容 · 中文简述</h3><p>${esc(data.zh[n.id].summary)}</p></div><details class="original-topic"><summary>查看完整说明与观察提示（英文原文）</summary><h3 lang="en">${esc(n.name)}</h3>${original}</details>`:original;
 el.innerHTML=`<div class="topic-meta">${esc(domainLabel(n.domain))} · ${n.ageRangeStart}–${n.ageRangeEnd} ${t('years','岁')}</div><h2 tabindex="-1">${esc(topicLabel(n))}</h2><a class="source-link" href="${topicUrl(n)}" target="_blank" rel="noopener">${t('Original topic','原始知识点')} ↗</a>${content}<h3>${t('Foundations to build on','先有这些基础')} · ${relation.before.length}</h3>${group(relation.before,true)}<h3>${t('What this can lead to','接下来可以发展')} · ${relation.after.length}</h3>${group(relation.after,false)}`;
 el.querySelectorAll('[data-related]').forEach(b=>b.addEventListener('click',()=>selectTopic(b.dataset.related,true)));
}
document.querySelectorAll('[data-subject]').forEach(b=>{b.addEventListener('click',()=>chooseSubject(b.dataset.subject));b.addEventListener('keydown',e=>{if(['ArrowLeft','ArrowRight','Home','End'].includes(e.key)){e.preventDefault();const next=e.key==='Home'?'Mathematics':e.key==='End'?'English':subject==='Mathematics'?'English':'Mathematics';chooseSubject(next);document.querySelector(`[data-subject="${next}"]`).focus();}});});
document.querySelectorAll('[data-lang]').forEach(b=>b.addEventListener('click',()=>{lang=b.dataset.lang;try{localStorage.setItem('second-path-map-language',lang);}catch{}render();}));
$('#search').addEventListener('input',e=>{query=e.target.value.trim();selected='';render();$('#mapViewport').scrollTo(0,0);});
$('#reset').addEventListener('click',()=>chooseSubject(subject));
render();
