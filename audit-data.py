"""Bilateral editorial audit. Links are evidence associations, never equivalences.

The complete Marble inventory is generated from stable IDs by the viewer.
Only manually selected nodes below receive an association; domain membership
alone cannot turn an unreviewed node into a curricular match.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
topics = json.loads((ROOT / 'source.json').read_text())['topics']
def bi(en, zh): return {'en': en, 'zh': zh}
sources = {}
def source(key, en, zh, url, ken, kzh):
    sources[key] = dict(title=bi(en, zh), url=url, kind=bi(ken, kzh))
source('national2022', 'Ministry of Education: curriculum reform 2022', '教育部：2022年义务教育课程改革', 'https://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202204/t20220421_620068.html', 'National direction, not Shanghai textbook sequencing', '国家总方针，不是上海教材进度')
source('mathstructure', 'National maths standard: content structure, p.17', '国家数学课标：内容结构，第17页', 'https://www.pep.com.cn/xw/zt/rjwy/yjkb2022/202205/P020220512583134605579.pdf', 'National standard hosted by PEP; the indexed structure was checked', '人教社收录的国家课标；已核对可检索的内容结构')
source('math2022early', 'National maths standard: April 2022 PDF', '国家数学课标：2022年4月公开文本', 'https://www.moe.gov.cn/srcsite/A26/s8001/202204/W020220420582346895190.pdf', 'Version caveat: recheck against the May 9 correction before textbook assignment', '版本提示：具体条目仍需与5月9日修正版及上海原书复核')
source('mathrelease', 'Ministry release: corrected maths standard', '教育部课标发布页：数学以5月9日版为准', 'https://www.moe.gov.cn/srcsite/A26/s8001/202204/t20220420_619921.html?fromColId=194', 'Authoritative version reference', '正式版本依据')
source('rmbschool', 'Shanghai Qingpu World Foreign Language School: money project', '上海青浦区世外学校：人民币项目化学习实践', 'https://cms.shwfl.edu.cn/_s56/2024/1128/c2425a14645/page.psp', 'School account, 2024; does not establish all new-book editions', '2024年学校实践记录，不证明全套新教材版次')
source('measurementsh', 'Xuhui Tianlin No.3 Primary: measurement teaching', '徐汇田林三小：量感主题教研', 'https://tl3x.xhedu.sh.cn/cms/app/info/doc/index.php/27620', 'Local teaching evidence, not a complete textbook index', '本地教研依据，不是全套教材目录')
source('shai', 'Shanghai AI in basic education action plan, 2024–2026', '上海市教委：人工智能赋能基础教育行动方案（2024—2026年）', 'https://www.shanghai.gov.cn/gwk/search/content/d41f0919ad4446f28076eb15c5669070', 'Shanghai policy; local AI course, not maths/English content', '上海政策；地方人工智能课程，不等于数学或英语章节')
source('strongnation', 'Education development plan, 2024–2035', '《教育强国建设规划纲要（2024—2035年）》', 'https://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202501/t20250119_1176166.html', 'National strategic goals', '国家战略目标')
source('aied2026', 'Five ministries: AI + education, 2026', '五部门：“人工智能+教育”行动计划（2026）', 'https://edu.sh.gov.cn/mbjy_fgwx_qt/20260605/eafd2cbb51794e8d8f997f2902df7889.html', 'National policy reproduced by Shanghai Education Commission', '国家政策，上海市教委转载')
source('doing2026', 'Ministry: learning science by doing, 2026', '教育部：义务教育科学教育“做中学”领航行动（2026）', 'https://edu.sh.gov.cn/mbjy_xwzx/20260812/7cbec405d560411faf8ea4491cf664f7.html', 'Science and interdisciplinary implementation; not an English syllabus', '科学与跨学科实施要求，不是英语课纲')

rows = []
def add(key, subject, kind, title, fact, indices, analysis, test, refs, locator=''):
    rows.append(dict(id=key, subject=subject, kind=kind, title=bi(*title), fact=bi(*fact),
        topics=[topics[i]['id'] for i in indices], analysis=bi(*analysis), probe=bi(*test), sources=refs, locator=locator))

add('rmb', 'Mathematics', 'local', ('Renminbi ↔ pounds and pence', '人民币 ↔ 英镑与便士'),
    ('Shanghai school reports document renminbi learning and shopping projects.', '上海学校记录了人民币认识及购物项目。'), [619,625,630,632,641,655],
    ('Marble has general money skills and explicit £/p nodes, but this imported maths inventory has no named renminbi node. This is a two-way localisation difference, not an absence of financial reasoning. A direct translation of £ into 元 would silently change the source.', 'Marble 有通用货币能力，也明确列出英镑/便士；当前数学数据没有明确的人民币节点。这是双向的地域内容差异，不是缺少理财思维。把 £ 直接译成“元”会改动原始要求。'),
    ('Can the child apply the same change-making method to a new currency after learning its units?', '换一种货币、先说明单位关系后，孩子能否迁移找零方法？'), ['rmbschool'])
add('measure-units', 'Mathematics', 'local', ('Measurement ↔ imperial extensions', '量感与计量 ↔ 英制扩展'),
    ('A Shanghai teaching report covers capacity, length and surface-area activities.', '上海教研记录涉及容量、长度和表面积活动。'), [612,626,640,662,668,677],
    ('The portable skill is choosing, estimating and converting units. Marble also explicitly adds inches, pounds, pints and miles. Those contexts are real Marble additions to the selected local evidence, not proof that Shanghai never introduces them.', '可迁移的能力是选单位、估测、换算。Marble 还明确涉及英寸、磅、品脱、英里；这些超出本次上海教研材料列出的情境，但不能据此断言上海从不介绍英制。'),
    ('Ask for an estimate before measuring, then an explanation of why that unit fits.', '先估测再测量，并解释为什么选这个单位；不能只看是否会套换算公式。'), ['measurementsh'])
add('abacus', 'Mathematics', 'candidate', ('Abacus as a representation', '算盘表示数'),
    ('The April national text names abacus representations.', '国家课标4月公开文本提及用算盘表示数。'), [742,754,762],
    ('No explicit abacus task was found in the imported maths records. Place-value nodes are conceptual neighbours, not an abacus match. This is a candidate source-side omission; the corrected standard and Shanghai book sequence still need checking.', '当前数学记录未找到明确的算盘任务。位值节点只是概念邻居，不能视为算盘教学已覆盖。这是中国侧内容的缺项候选；修正版课标与上海新版课本进度仍待核对。'),
    ('Represent the same number with blocks, written digits and beads; explain what stays the same.', '用积木、数字和算珠表示同一个数，解释不变的位值关系。'), ['math2022early','mathrelease'], 'p.18 · 4月文本，待修正版复核 / April text; correction check pending')
add('reasoning', 'Mathematics', 'shared', ('Reasoning is a shared goal', '推理是共同目标'),
    ('Shanghai new-book training stresses questioning and reasoning.', '上海新教材教研强调提问与推理。'), [574,582,590,593],
    ('Marble separates prompted reasoning, justification, critique and self-monitoring. One broad Shanghai teaching goal may relate to several nodes. Counting it as one versus four would manufacture a gap; assuming equal independence would conceal a real depth question.', 'Marble 把提示下推理、论证、评价他人方法、自我检查分开。上海一项概括性目标可能关联多个点：简单比较“1项对4项”会制造数量差距；直接判等则会掩盖独立性与论证深度的差异。'),
    ('Can the child explain a result, find a counterexample, and revise an argument without a hint?', '能否解释答案、找反例，并在没有提示时修正自己的论证？'), ['m67'])
add('data-depth', 'Mathematics', 'depth', ('Classifying data → inference', '分类整理 → 数据推断'),
    ('The national structure progresses from classification to data work and sampling.', '国家内容结构从分类发展到数据整理、抽样分析。'), [410,415,419,421,422,426],
    ('Marble splits graphs and summaries into separate nodes, reaching scatter plots. This is a progression within its inventory, not six extra Shanghai omissions. The unresolved comparison is which displays, datasets and explanations Shanghai expects at each stage.', 'Marble 按图表与统计量拆点，延伸到散点图。这是其内部的进阶，不是六项“上海没教”。需要继续核对的是上海各阶段采用哪些图、什么数据、要求怎样解释，而不只是有没有“统计”二字。'),
    ('Give the same data as a table and a misleading chart; ask which conclusion is justified.', '把同一组数据画成表格和一张容易误导的图，让孩子判断哪些结论有依据。'), ['mathstructure'])
add('probability-depth', 'Mathematics', 'depth', ('Likelihood ↔ numerical probability', '可能性判断 ↔ 概率计算'),
    ('The national structure separates primary likelihood from secondary event probability.', '国家结构将小学可能性与初中事件概率分层。'), [789,790,791,792,794,795,796,802,803],
    ('Marble ranges from qualitative language to fractions, complements and combined-event sample spaces. Its age labels alone cannot establish earlier Shanghai coverage. A child who can say “more likely” has not thereby mastered counting outcomes or explaining experimental variation.', 'Marble 从定性描述延伸到分数概率、补事件和组合事件样本空间。不能仅据其年龄标签判断上海早教或晚教。会说“更可能”，并不等于会计数所有结果、解释实验频率的波动。'),
    ('Before calculating, ask whether outcomes are equally likely and whether the sample space is complete.', '计算前先问：结果真的等可能吗？有没有漏掉结果？'), ['mathstructure'])
add('ratio-depth', 'Mathematics', 'candidate', ('Proportion ↔ several representations', '比例关系 ↔ 多种表征'),
    ('The April national text includes ratio and direct proportion in contexts.', '国家课标4月文本包含情境中的比与正比例。'), [804,807,811,815,816,820],
    ('Marble distinguishes bar models, ratio notation, graphs and inverse proportion. These are not all equivalent to a single ratio topic. Inverse proportion and algebraic/graphical demands need separate Shanghai verification; this source version is provisional.', 'Marble 分列条形模型、比的记法、图像，还包含反比例，不能全打包成一个“比例已覆盖”。尤其反比例以及代数/图像要求，要分别核对上海内容；此处国家来源版次仍需复核。'),
    ('Can the child move between a recipe, a ratio table and a graph, and say when proportional reasoning fails?', '能否在配方、比值表和图像之间转换，并举出不能按比例推算的例子？'), ['math2022early','mathrelease'], 'p.24 · 版本待复核 / provisional version')
add('algebra-scope', 'Mathematics', 'scope', ('Arithmetic relationships ↔ later algebra', '数量关系 ↔ 后续代数'),
    ('National maths separates primary quantities from secondary algebraic study.', '国家数学结构区分小学数量关系与初中代数学习。'), [375,376,377,379,385,387,388,392,394,395],
    ('Marble includes formula substitution, equations, factorisation and quadratic graphs in one subject inventory. Some start at 13. Listing all of them against ages 0–12 creates a false “Shanghai missing” impression. Age ≤12 is still not a Shanghai grade assignment.', 'Marble 同一学科库存包含代入、方程、因式分解、二次函数图像，其中一些起始年龄是13岁。把它们全算进0–12岁，会产生“上海少教了”的错觉；即使起始年龄≤12，也不能直接换成上海年级。'),
    ('Separate expressing a relationship from solving an equation and interpreting its graph.', '把“表示数量关系”“解方程”“解释图像”分别观察，不用一个“会代数”笼统判断。'), ['mathstructure'])
add('fractions-granularity', 'Mathematics', 'scope', ('One fraction theme, many demands', '同是分数，要求并不相同'),
    ('Primary number-and-operation content includes fractions.', '国家小学数与运算内容包含分数。'), [428,429,431,437,438,439,443,451,478,482,487,492,493],
    ('Marble has separate part-whole, number-line, equivalence and operation nodes. Even “same denominator” splits into results below and above one. Some titles understate their descriptions. Compare representations, operand range and explanation demands before counting matched points.', 'Marble 将分物、数轴、等值与运算拆开；同分母加减又区分结果在1以内或超过1。有的标题还小于正文范围。应先比较表征、操作数范围、解释要求，再统计对应点，不能按关键词批量判等。'),
    ('Ask why an equivalent fraction has the same value, using both an area model and a number line.', '要求用面积图和数轴两种方式解释：为什么等值分数的大小不变？'), ['math2022early','mathrelease'])
add('geometry-depth', 'Mathematics', 'scope', ('Recognising a shape ↔ proving a property', '认图形 ↔ 证明性质'),
    ('National geometry distinguishes recognition/measurement, movement and later properties.', '国家几何结构区分认识测量、位置运动与后续性质研究。'), [495,496,508,517,522,533,541,550,557,561,562,563],
    ('Marble progresses from naming to nets, construction, congruence and trigonometry. These do not share one mastery criterion. A geometry chapter cannot cover every linked node; trigonometry and Pythagoras here have age-13 starts and are outside the chosen starting-age window.', 'Marble 从命名进阶到展开图、作图、全等、三角比，不共享一个达标标准。一章“几何”不能代表全部关联点已覆盖；这里三角比与勾股定理的参考起始年龄为13岁，应移出本次起始年龄范围。'),
    ('After recognising a solid, predict its net; after stating a property, explain why it holds.', '认出立体图形后能否预测展开图？说出性质后能否说明为什么成立？'), ['mathstructure'])

# Keep national-English facts brief. Comparisons below are editorial analyses of
# the supplied Marble records; they do not prescribe Shanghai grade placement.
def english(key, kind, title, fact, ix, analysis, probe, page):
    add(key,'English',kind,title,fact,ix,analysis,probe,['enstandard'],f'Printed p.{page} / 课标正文第{page}页')
english('phonics','shared',('Phonics is present on both sides','两边都有拼读'),
    ('The standard includes sound–letter connections and decoding.', '课标包含音形联系与拼读。'), [87,89,92,99,103,106,109],
    ('Marble explicitly spans blending, fluency, syllables and morphology. That is richer detail than a broad phonics label, not evidence that Chinese English ignores phonics. Compare unfamiliar-word decoding and the amount of prompting; do not import Marble age expectations as EFL deadlines.', 'Marble 明列合音、流利度、音节、词素，拆分比“拼读”更细，不代表中国英语没有自然拼读。需要比较陌生词解码能力和提示量；不能把 Marble 的英语读写年龄当作外语学习达标期限。'),
    ('Try a new decodable word, rather than a memorised word from the unit.', '用符合已学规则的新词，区别真正拼读与背熟课内单词。'), '19')
english('grammar-depth','depth',('Language use ↔ grammar analysis','语言运用 ↔ 语法分析'),
    ('Levels 1–2 introduce basic sentence and tense use.', '一级、二级逐步要求基本句式和时态运用。'), [7,16,23,35,43,55,57,59,62,68,73,74],
    ('Marble extends to relative clauses, passive voice, semicolons and subjunctive forms. This goes beyond basic introductory use, but the later Shanghai sequence is unverified. Recognising a rule, using it in speech and analysing its stylistic effect require separate judgements.', 'Marble 延伸到关系从句、被动、分号、虚拟语气，范围超出基础入门运用；上海后续具体进度仍未核实。识别规则、在交际中使用、分析文体效果，是三个不同要求。'),
    ('Can the child use a form to express a real meaning without first naming the grammar rule?', '孩子能否不先背语法术语，就用合适形式表达真实意思？'), '21')
english('reading-inference','shared',('Reading for meaning and evidence','理解意义与寻找依据'),
    ('Primary levels include prediction and supported interpretation.', '小学阶段包含预测与借助线索理解。'), [110,119,120,129,130,138,144,158,162,172],
    ('Marble separates picture clues, inference, author purpose, fact/opinion and argument evaluation. Later nodes demand more than predicting a picture story. Both have thinking goals; compare text difficulty, evidence quality and independence rather than declaring one side “critical” and the other not.', 'Marble 分列图像线索、推断、作者目的、事实观点与论点评价。后面的要求显然高于看图猜故事。双方都有思考目标；要比较文本难度、依据质量与独立性，不能直接划成“有批判思维”和“没有”。'),
    ('Ask what in the text supports the answer, and whether another interpretation also fits.', '追问文本中哪条证据支持答案，以及是否存在同样说得通的另一种解释。'), '25–27')
english('writing-depth','depth',('Supported sentences ↔ independent composition','支架下写句子 ↔ 独立创作'),
    ('Primary writing includes supported expression and short connected text.', '小学写作包含有支持的表达与连贯短文。'), [248,249,252,258,259,266,270,274],
    ('Marble includes independent critical revision and audience/style decisions. Copying a model accurately cannot establish those skills. The useful gap to investigate is moving from a supplied frame to choosing structure and revising meaning, not simply writing more words.', 'Marble 包含独立审改、针对受众选择文体。准确套用范文不能证明掌握这些能力。值得观察的差距，是能否由给定框架转向自主组织与修改意思，而不是单纯增加字数。'),
    ('Give the same message two audiences; ask what needs changing and why.', '把同一个消息写给朋友与陌生读者，让孩子解释需要改哪些地方。'), '26–27')
english('oral-depth','shared',('Interaction ↔ formal discussion','日常互动 ↔ 正式讨论'),
    ('The standard includes situational interaction and polite language.', '课标包含情境互动与礼貌表达。'), [182,183,185,186,187,194,195,197,200,202],
    ('Marble moves from listening/responding to building on others, evaluating speakers and formal debate. “Can speak English” conceals these differences. Daily communication and formal argument are different tasks; neither should be treated as an automatic substitute for the other.', 'Marble 从倾听回应进阶到接续他人观点、评价发言与正式辩论。“会说英语”会遮住这些差别。日常交际和论证讨论是不同任务，不能互相替代。'),
    ('Can the child first restate someone else’s idea accurately, then add a reasoned response?', '能否先准确复述别人的意思，再给出有理由的回应？'), '23, 25–27')
english('culture-local','local',('Chinese context ↔ cross-cultural literature','中国情境 ↔ 跨文化阅读'),
    ('The standard explicitly includes Chinese and international cultural knowledge.', '课标明确涉及中国及世界文化知识。'), [140,152,171,181],
    ('Marble does contain cultural comparison in reading; it is incorrect to mark culture absent. However, these records do not explicitly define a China-specific English-expression pathway. Reading stories from several cultures and explaining one’s own customs to a visitor are related but different outputs.', 'Marble 的阅读确实包含跨文化比较，不能标成“没有文化”。但当前记录未明确建立中国情境的英语表达路径。读不同文化的故事，与向访客解释自己的习俗，关联但并不等同。'),
    ('Explain a familiar local custom to someone unfamiliar with it, without assuming shared knowledge.', '向不了解中国生活的访客解释一个熟悉习俗，观察能否补足背景信息。'), '24')
english('vocab-depth','shared',('Vocabulary size ↔ vocabulary use','词汇量 ↔ 词汇运用'),
    ('The standard connects word form, meaning and contextual use.', '课标联系词形、意义与语境运用。'), [4,218,227,230,231,232,247],
    ('Marble makes word-learning strategies, word parts and dictionary work visible. A word-count benchmark cannot be compared with a count of these skill nodes. Knowing a translation, inferring a meaning and choosing an appropriate word should be tracked separately.', 'Marble 把词汇策略、构词、查词典列成节点。“词数”不能与“技能点数”比较。知道中文意思、推断新词、选择得体用词，需要分别记录。'),
    ('Ask for a meaning guess from context, then a dictionary check and an original sentence.', '先据语境猜义，再查词典核对，最后在自己的句子中使用。'), '20')
english('learning-strategy','shared',('Learning to learn within English','英语学科中的学会学习'),
    ('The standard includes help-seeking, reflection and learning strategies.', '课标包含求助、反思与学习策略。'), [1,4,5,6,121,248,259,266],
    ('Marble shows monitoring and revision as named skills. National English already has strategy goals, so this is not a policy omission. The real comparison is whether support fades over time and whether the learner can choose a strategy in a new task.', 'Marble 将自我检查与修改独立命名。国家英语已有策略目标，因此不能判为政策缺失。更实质的对比是支持是否逐渐减少，以及能否在新任务中自主选策略。'),
    ('When stuck, ask the learner to choose a next step and later judge whether it helped.', '遇到困难时让孩子选择下一步，事后判断这个办法有没有用。'), '31–32')
english('genre-scope','depth',('Text variety ↔ sustained literary reading','语篇种类 ↔ 持续文学阅读'),
    ('The standard differentiates genres across levels.', '课标按级别区分语篇类型。'), [111,125,126,139,152,153,168,174,181],
    ('Marble reaches whole-book reading, cross-text synthesis and unreliable narrators. A picture story, a short functional text and a full novel differ in length, cultural load and interpretive demand. These nodes are candidate enrichment, not requirements for every Shanghai child of the same reference age.', 'Marble 延伸到整本书、跨文本综合、不可靠叙述者。图画故事、功能短文与整部小说，在长度、文化背景、解释要求上均不同。这些可作拓展候选，不能变成所有上海同龄孩子的必修任务。'),
    ('Compare two accounts of the same event and identify what each leaves out.', '比较同一事件的两个叙述，指出各自遗漏了什么。'), '18')

policies=[]
def policy(key,title,fact,analysis,math,en,probe,refs):
    policies.append(dict(id=key,title=bi(*title),fact=bi(*fact),analysis=bi(*analysis),topics={'Mathematics':[topics[i]['id'] for i in math], 'English':[topics[i]['id'] for i in en]},probe=bi(*probe),sources=refs))
policy('policy-purpose',('What education is for','育人目标与工具用途'),
    ('National policy combines values, capabilities and all-round development.', '国家方针同时规定价值观、能力与德智体美劳全面发展。'),
    ('A national education system also has civic and public-service goals. A skills database organises learnable performances. Their purposes differ: counting policy goals as missing maths/English nodes is not a like-for-like comparison.', '国家教育体系还承担公民培养与公共教育职责；技能数据库主要组织可学习的表现。用途不同，把政策目标硬算成数学/英语“缺失知识点”，并不是同口径比较。'), [],[],
    ('Judge subject knowledge, self-directed learning and broader development separately.', '分别观察学科知识、自主学习与更广泛的发展，不用一张学科技能表替代整体成长判断。'), ['strongnation','national2022'])
policy('policy-project',('Projects and real problems','项目与真实问题'),
    ('Shanghai policy asks schools to incorporate subject and interdisciplinary projects.', '上海政策要求推进学科及跨学科项目学习。'),
    ('Marble can identify component skills; a project tests whether a learner combines them. Neither a policy document nor a completed worksheet proves transfer. Compare the learner’s decisions, revisions and final explanation, not whether an activity is called a project.', 'Marble 能拆出组成能力，项目检验能否组合运用。政策文件或填完的练习单都不能证明迁移；应比较孩子作出的决策、修改过程与最终解释，而不只是活动是否叫“项目”。'), [568,576,580,582],[250,267,195,270],
    ('Plan a small event with a budget and an invitation; preserve the choices and revisions.', '做一个带预算和邀请函的小活动，留下选择依据与修改记录。'), ['project'])
policy('policy-ai',('AI is already in Shanghai policy','上海政策已包含人工智能'),
    ('Shanghai’s 2024–2026 plan specifies local AI courses in Grades 4 and 7.', '上海2024—2026年方案明确在四、七年级开设人工智能地方课程。'),
    ('This is a school-curriculum requirement outside the two subject inventories, not proof of an AI chapter in maths or English. The imported nodes offer reasoning and source-evaluation neighbours; they do not constitute a complete AI literacy curriculum.', '这是两科学科表之外的学校课程安排，不证明数学或英语教材有某一AI章节。当前节点有推理、来源判断等相关基础，却不能组成完整的AI素养课程。'), [582,590],[169,282],
    ('Distinguish a plausible answer from a checked answer; identify evidence that could disprove it.', '区分“看起来合理”与“已经核实”，找出可能推翻答案的证据。'), ['shai','aied2026'])
policy('policy-science',('Inquiry has a concrete process','探究有具体过程'),
    ('The 2026 science initiative specifies tasks for Grades 4–9; Grades 1–3 follow existing science inquiry requirements.', '2026年科学行动对四至九年级规定任务；一至三年级依现有科学探究要求落实。'),
    ('Observation, testing and revision are more demanding than being told a correct explanation. Maths data skills and English reporting can support inquiry, but the science requirement is not a new compulsory English test. Policy implementation in an individual class remains unobserved.', '观察、验证、改进比听懂正确解释更进一步。数学数据能力和英语汇报可支持探究，但科学要求不能改写成额外英语考核；具体班级是否落实仍需实际观察。'), [419,568,582],[130,267,270],
    ('Keep a prediction, measurements and a revised explanation; compare what changed.', '保留预测、测量数据与修改后的解释，比较什么证据改变了想法。'), ['doing2026'])
policy('policy-assess',('Evidence of learning, not just an answer','观察学习过程，不只看答案'),
    ('Shanghai project guidance includes process observations and varied outputs.', '上海项目指导意见包含过程观察与多样成果。'),
    ('Marble observation prompts can help record concrete behaviour. Neither taxonomy completion nor grades alone show independence or transfer. Record the task, support provided, evidence and a repeat attempt in a new context; avoid a permanent trait label from one activity.', 'Marble 的观察提示可帮助记录具体行为。勾完节点或分数都不能单独证明独立性、迁移力。应记录任务、提供的帮助、行为证据，再换情境观察；不凭一次活动给孩子贴永久标签。'), [593,574],[1,5,266],
    ('Was it independent, prompted, modelled, or not yet observed? Record the evidence.', '独立完成、经提示完成、跟示范完成，还是尚未观察？记录具体证据。'), ['project'])
policy('policy-early',('Ages 0–6 are not early school grades','0–6岁不是小学前置年级'),
    ('Shanghai transition guidance centres on developmentally appropriate preparation.', '上海幼小衔接以适宜的发展准备为依据。'),
    ('The imported maths/English nodes start at 4; none define infant milestones. A missing age-0–3 node is a scope boundary, not a child’s deficit. Play-based quantity and spatial experiences can be linked; compulsory preschool English targets cannot be inferred.', '本次数学/英语数据最早从4岁起，没有婴幼儿里程碑。0–3岁没有节点是范围边界，不是孩子有缺陷。游戏中的数量、空间经验可关联，但不能推导学前英语必达目标。'), [396,397,495,496],[],
    ('Observe interests and spontaneous use during play; do not convert the map into age-based drills.', '在游戏中观察兴趣与自发运用，不把图谱变成年龄刷题清单。'), ['transition'])

result = dict(sources=sources, rows=rows, policies=policies)
(ROOT/'audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(f'Wrote {len(rows)} deeper comparisons and {len(policies)} policy comparisons')
