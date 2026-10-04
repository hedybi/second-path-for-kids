"""Original bilingual teaching activities; age labels and IDs follow Marble v1."""
def variant(label, sentence, zh, parts, rule):
    return dict(label=label,sentence=sentence,zh=zh,parts=parts,rule=rule)
def lesson(title, clue, variants):
    return dict(title=title,clue=clue,variants=variants)
def question(tag, prompt, options, answer, hint, explain):
    return dict(tag=tag,prompt=prompt,options=options,answer=answer,hint=hint,explain=explain)
V,L,Q=variant,lesson,question
MODULES=[
dict(id='question-words',name='疑问词与提问',en='Question Words & Questions',age='5–6',icon='🔎',node='mt_6lHBTwQPrS',mission='帮小兔找到问题里缺少的线索。',boundary='先学问什么，再学怎样问。成人可读出题目；不要求孩子独立阅读所有英文。',lessons=[
 L('想问人，还是东西？','先决定你想知道什么，再选疑问词。',[
 V('问谁 · Who','Who is at the door?','谁在门口？',['Who → 谁','is → 是 / 处于','at the door → 在门口'],'回答应指向人：Mum is at the door. 不用 where 问“谁”。'),
 V('问什么 · What','What is in the box?','盒子里是什么？',['What → 什么','is → 是 / 处于','in the box → 在盒子里'],'回答应说明东西：A ball is in the box. who 问人，what 在这里问东西。')]),
 L('地点和时间分开问','哪里问地点，什么时候问时间。',[
 V('找地点 · Where','Where is the rabbit?','小兔在哪里？',['Where → 哪里','is → be 动词','the rabbit → 小兔'],'In the garden. 回答的是地点，不是时间。'),
 V('找时间 · When','When is the party?','聚会在什么时候？',['When → 什么时候','is → be 动词','the party → 聚会'],'On Sunday. 回答的是时间，不是地点。')]),
 L('原因和方法分开问','为什么？怎样做？是两种不同的信息。',[
 V('问原因 · Why','Why are you happy?','你为什么开心？',['Why → 为什么','are → be 动词','you happy → 你开心'],'Because it is my birthday. because 引出原因。'),
 V('问方法 · How','How do you go to school?','你怎样去学校？',['How → 怎样','do → 提问小助手','you go → 你去'],'By bus. 回答出行方式；how 还可以问状态，如 How are you?')]),
 L('同一件事，问法不同','有 be 的句子，把 be 放在主语前提问。',[
 V('先说一件事','The rabbit is in the garden.','小兔在花园里。',['The rabbit → 主语','is → be 动词','in the garden → 地点'],'句子告诉我们一件事，结尾用句号。'),
 V('问是不是','Is the rabbit in the garden?','小兔在花园里吗？',['Is → 放到前面','the rabbit → 主语','in the garden? → 问号'],'可以回答 Yes 或 No。Is 来到主语前面，不用再加 do。'),
 V('问在哪里','Where is the rabbit?','小兔在哪里？',['Where → 想知道的地点','is → be 动词','the rabbit? → 主语'],'问的是缺少的地点，回答 In the garden.，只说 Yes 不够。')]),
 L('动作句的小助手','练熟例句即可；这不是所有疑问句的万能公式。',[
 V('你喜欢吗','Do you like apples?','你喜欢苹果吗？',['Do → 小助手','you → 主语','like → 原形'],'普通动词 like 提问：Do you like…? 可以回答 Yes, I do.。'),
 V('她喜欢什么','What does she like?','她喜欢什么？',['What → 问东西','does → 小助手','she like → 主语 + 原形'],'does 后面的 like 用原形，不写 likes。'),
 V('谁喜欢苹果','Who likes apples?','谁喜欢苹果？',['Who → 主语未知','likes → 动词','apples? → 苹果'],'这里 Who 自己就是主语，基础中性问法不加 do。先认得例句，不背复杂术语。')])],questions=[
 Q('who','想知道门口是谁：___ is at the door?',['Who','Where','When'],'Who','你在找人、地点还是时间？','Who 问谁；回答可以是 Dad。'),
 Q('what','回答是 A ball.：___ is in the box?',['When','What','Who'],'What','ball 是东西。','What 问盒子里是什么。'),
 Q('where','回答是 In the garden.：___ is the rabbit?',['Where','Why','When'],'Where','garden 是地点。','Where 问地点。'),
 Q('when','回答是 On Sunday.：___ is the party?',['Who','Where','When'],'When','Sunday 告诉我们时间。','When 问什么时候。'),
 Q('why','回答是 Because I lost my toy.：___ are you sad?',['Why','What','Where'],'Why','because 后面给出原因。','Why 问为什么。'),
 Q('how','回答是 By bus.：___ do you go to school?',['Who','How','When'],'How','这是出行方法。','How 在这里问怎样去。'),
 Q('be','把 The cat is here. 变成“猫在这里吗？”',['Is the cat here?','Does the cat here?','The cat here?'],'Is the cat here?','原句的动词是 is。','把 is 移到主语前，结尾换问号。'),
 Q('where','Where is my bag? 哪个回答提供了地点？',['On the chair.','Tomorrow.','My sister.'],'On the chair.','Where 要找位置。','On the chair. 表示在椅子上。'),
 Q('do','___ you like milk?',['Are','Do','Does'],'Do','like 是普通动词，主语是 you。','Do you like milk?；不能把 are 放在普通动词 like 前这样提问。'),
 Q('does','What does Lily ___?',['likes','liking','like'],'like','小助手 does 已经出现。','does 后面的主要动词用原形 like。'),
 Q('who','问“谁喜欢苹果？”',['Who likes apples?','Where likes apples?','Who like apples?'],'Who likes apples?','问的这个“谁”自己在做动作。','基础问法是 Who likes apples?；不是把每个疑问句都套上 do。'),
 Q('when','你想知道生日的时间，选一句。',['Where is your bag?','When is your birthday?','Who is your friend?'],'When is your birthday?','要问的不是人或地点。','When is your birthday? 问生日在什么时候。')],transfer=[
 Q('who','回答是 My teacher.：___ is at the gate?',['When','Who','Where'],'Who','想知道的是人。','Who 问是谁。'),
 Q('what','回答是 A kite.：___ is on the desk?',['What','Why','When'],'What','kite 是物品。','What 问是什么。'),
 Q('where','回答是 Under the bed.：___ is the shoe?',['When','Who','Where'],'Where','under the bed 是位置。','Where 问哪里。'),
 Q('when','回答是 At six.：___ is dinner?',['When','Where','What'],'When','At six 是时间。','When 问什么时候。'),
 Q('why','回答是 Because it is cold.：___ are you wearing a coat?',['Who','Why','Where'],'Why','解释穿外套的原因。','Why 问为什么。'),
 Q('how','回答是 On foot.：___ do you get home?',['How','When','Who'],'How','步行是一种方式。','How 问怎样回家。'),
 Q('be','问“书包是红色的吗？”',['Does the bag red?','Is the bag red?','Are the bag red?'],'Is the bag red?','the bag 是单数；red 是形容词。','用 Is the bag red?。'),
 Q('do','___ you play tennis?',['Do','Is','Does'],'Do','you 配哪个小助手？','Do you play tennis?。'),
 Q('does','Where does Ben ___?',['lives','live','living'],'live','does 后面恢复原形。','Where does Ben live? 问他住哪里。')]),
dict(id='sentence-agreement',name='句子中的一致关系',en='Agreement in Sentences',age='8–10',icon='🤝',node='mt_2NfIKEYdbm',mission='找到真正的主语，让动词和代词组成队伍。',boundary='承接基础主谓一致；不把“最近的名词”当主语，不把单数 they 判为错误。',lessons=[
 L('先找整个主语的中心','夹在中间的描述，不决定动词形式。',[
 V('一个女孩','The girl with two dogs is happy.','带着两只狗的女孩很开心。',['The girl → 主语中心，单数','with two dogs → 补充描述','is → 跟 girl 一致'],'two dogs 离 is 很近，但主语中心是 girl。'),
 V('多个女孩','The girls with a dog are happy.','带着一只狗的女孩们很开心。',['The girls → 主语中心，复数','with a dog → 补充描述','are → 跟 girls 一致'],'a dog 是描述的一部分，不能让 are 变 is。')]),
 L('and 连接的人物有几个？','本课比较两个独立的人物和一个人物。',[
 V('一个人','Mia plays outside.','米娅在外面玩。',['Mia → 一个人','plays → 第三人称单数','outside → 在外面'],'普通动词一般现在时肯定句中，Mia 配 plays。'),
 V('两个人','Mia and Ben play outside.','米娅和本在外面玩。',['Mia and Ben → 两个人','play → 原形','outside → 在外面'],'两个人组成复数主语，可以换成 they。')]),
 L('代词接住前面的人或物','先找到代词在说谁，再检查搭配。',[
 V('一只猫','The cat is hungry. It wants food.','猫饿了。它想吃东西。',['The cat → 单数','It → 指这只猫','wants → 随 it 变化'],'It 接住 the cat，两个句子说的是同一个对象。'),
 V('多只猫','The cats are hungry. They want food.','猫们饿了。它们想吃东西。',['The cats → 复数','They → 指这些猫','want → 原形'],'这里 They 接住复数 cats。'),
 V('单数 they','Alex uses they/them pronouns. They are here.','Alex 使用 they/them 代词。Alex 在这里。',['Alex → 一个人','They → Alex 使用的代词','are → they 的搭配'],'they 也能指一个人；标准搭配仍是 they are / they have，不写 they is。')]),
 L('所有关系也要接得上','my、her、their 说明谁拥有东西。',[
 V('Mia 的','Mia has a bag. Her bag is blue.','米娅有个包。她的包是蓝色的。',['Mia → 拥有者','Her → 她的','bag is → 一个包'],'Her 指 Mia；is 跟本句的主语 bag 一致。'),
 V('孩子们的','The children have bags. Their bags are blue.','孩子们有包。他们的包是蓝色的。',['The children → 拥有者','Their → 他们的','bags are → 多个包'],'their 说明拥有者；are 由 bags 决定，不由 their 决定。')]),
 L('每一个与特殊搭配','every + 单数名词，在本课例句里配单数动词。',[
 V('每个孩子','Every child has a pencil.','每个孩子都有一支铅笔。',['Every child → 逐个看，单数','has → have 的单数形式','a pencil → 宾语'],'现实里可能有很多孩子，但 every child 这个主语按单数搭配。'),
 V('I 和 you','I am ready. You are ready.','我准备好了。你准备好了。',['I → am','You → are','ready → 状态'],'不能只按“一个人”选 is；人称也影响 be 的形式。')])],questions=[
 Q('head','The boy with two cats ___ happy.',['are','is','am'],'is','先圈出主语中心 boy。','with two cats 只描述 boy，单数 boy 配 is。'),
 Q('head','The dogs near the tree ___ hungry.',['is','am','are'],'are','near the tree 是位置描述。','真正的主语中心 dogs 是复数，配 are。'),
 Q('and','Lily and Ben ___ tennis every day.',['plays','play','playing'],'play','Lily 和 Ben 是两个人。','复数主语的一般现在时用 play。'),
 Q('pronoun','The rabbit is small. ___ has long ears.',['They','It','We'],'It','前面说一只兔子。','这里用 It 接住 the rabbit。'),
 Q('pronoun','The birds are noisy. They ___ in the tree.',['is','am','are'],'are','they 的 be 形式是什么？','They are；这里指这些鸟。'),
 Q('possessor','The children have bikes. ___ bikes are new.',['His','Their','Its'],'Their','是谁拥有这些自行车？','Their 指孩子们的。'),
 Q('every','Every student ___ a book.',['have','has','having'],'has','every student 逐个看，按单数搭配。','Every student has a book.。'),
 Q('person','You ___ my friend.',['is','am','are'],'are','you 即使指一个人，也有自己的搭配。','You are。'),
 Q('head','The box of pencils ___ on the desk.',['is','are','am'],'is','是在说盒子的位置，还是铅笔的位置？','主语中心 box 是单数，用 is。'),
 Q('singular-they','Alex uses they/them pronouns. They ___ kind.',['is','are','am'],'are','they 的搭配不因这里指一人而变 is。','单数 they 也配 are。'),
 Q('possessor','Mia has a dog. ___ dog likes milk.',['Their','Her','Its'],'Her','在这里要说“米娅的狗”。','Her 指 Mia；Its 会把拥有者换成物或动物。'),
 Q('pronoun','The kittens are hungry. ___ want food.',['It','He','They'],'They','kittens 是多只小猫。','They 接住复数 kittens，后面用 want。')],transfer=[
 Q('head','The basket of apples ___ heavy.',['are','is','am'],'is','主语中心是 basket。','of apples 不决定动词；basket 配 is。'),
 Q('and','Tom and Sue ___ ready.',['is','am','are'],'are','两个独立的人组成复数主语。','Tom and Sue are ready.。'),
 Q('pronoun','The flowers are red. ___ look lovely.',['It','They','She'],'They','flowers 是复数。','They 接住 flowers。'),
 Q('possessor','The boys have a ball. ___ ball is green.',['Their','Her','Its'],'Their','看拥有者 boys。','他们的球：Their ball；球只有一个仍用 is。'),
 Q('every','Every player ___ a number.',['have','has','are'],'has','every player 按单数搭配。','Every player has a number.。'),
 Q('person','I ___ excited.',['are','is','am'],'am','I 有单独的 be 形式。','I am。'),
 Q('singular-they','Sam uses they/them pronouns. They ___ a book.',['has','have','is'],'have','they 配 have，即使指一个人。','They have a book.。')]),
dict(id='plurals-and-possessives',name='名词复数与所有格',en='Plurals & Possessives',age='8–9',icon='🎒',node='mt_bn5ggh84qD',mission='替失物招领站分清：几个？谁的？',boundary='区分复数 s、单数所有格 ’s、规则复数所有格 s’ 和不规则复数所有格；不把所有 ’s 都当所属。',lessons=[
 L('先问几个，再问谁的','复数说明数量，所有格说明所属。',[
 V('几只狗','Two dogs are here.','两只狗在这里。',['dog → 狗','dogs → 多只狗','不加撇号 → 复数'],'只表达多只狗，加 s，不加撇号。'),
 V('一只狗的球',"The dog's ball is red.",'这只狗的球是红色的。',['the dog → 一只狗',"dog’s → 狗的",'ball → 被拥有的东西'],'一只狗拥有球：在 dog 后加 ’s。')]),
 L('主人不止一个','先写出拥有者的复数，再决定撇号。',[
 V('一个女孩的包',"The girl's bag is blue.",'这个女孩的包是蓝色的。',['girl → 一个女孩',"girl’s → 单数所有格",'bag → 一个包'],'一个女孩：girl + ’s。'),
 V('多个女孩的包',"The girls' bags are blue.",'这些女孩的包是蓝色的。',['girls → 多个女孩',"girls’ → 已有复数 s，只加撇号",'bags → 多个包'],'girls 已经以复数 s 结尾，后面加撇号：girls’。')]),
 L('不规则复数怎么办？','children 已经是复数，不再加一个复数 s。',[
 V('多个孩子','The children are playing.','孩子们正在玩。',['child → 一个孩子','children → 多个孩子','are playing → 正在玩'],'children 本身是复数，不写 childrens。'),
 V('孩子们的玩具',"The children's toys are here.",'孩子们的玩具在这里。',['children → 复数，不以 s 结尾',"children’s → 加 ’s",'toys → 多个玩具'],'不以 s 结尾的不规则复数，所有格仍加 ’s。')]),
 L('主人数量和东西数量分开看','撇号放哪里，由拥有者决定。',[
 V('一只狗，多个玩具',"The dog's toys are here.",'这只狗的玩具们在这里。',["dog’s → 一只狗的",'toys → 多个玩具','are → 随 toys 变化'],'玩具有多个，不会把 dog’s 改成 dogs’；主人仍是一只狗。'),
 V('多只狗，共用一个碗',"The dogs' bowl is here.",'这些狗共用的碗在这里。',["dogs’ → 多只狗的",'bowl → 一个共用的碗','is → 随 bowl 变化'],'碗只有一个，拥有它的狗有多只；两件事要分开。')]),
 L('撇号还有缩写用途','试着把 ’s 展开，看意思是否成立。',[
 V('说明所属',"Lily's bag is new.",'莉莉的包是新的。',["Lily’s → 莉莉的",'bag → 包','is new → 是新的'],'Lily’s 后面是她拥有的包。'),
 V('缩写 is',"Lily's happy.",'莉莉很开心。',["Lily’s → Lily is",'happy → 开心','不能解释成“莉莉的开心的”'],'这里 ’s 是 is 的缩写；其他语境也可能缩写 has，不能只凭撇号判断。'),
 V('its 不加撇号','The cat licks its paw.','猫舔它的爪子。',['its → 它的','paw → 爪子',"it’s → it is / it has 的缩写"],'所属代词 its 不加撇号；it’s 不能在这里替换 its。')])],questions=[
 Q('plural','两只猫：two ___',['cats',"cat's","cats'"],'cats','只数数量，没有说谁的东西。','cats 是复数，不加撇号。'),
 Q('single','一只狗的球：the ___ ball',['dogs',"dogs'","dog's"],"dog's",'拥有者是一只狗。','单数拥有者 dog + ’s。'),
 Q('plural-owner','多个女孩各自的书包：the ___ bags',["girl's","girls'",'girls'],"girls'",'拥有者是 girls，已经以 s 结尾。','规则复数 girls 后只加撇号。'),
 Q('irregular',"孩子们的玩具：the ___ toys",["childrens'","children's",'childrens'],"children's",'children 是不以 s 结尾的复数。','children + ’s 表示孩子们的。'),
 Q('two-counts','一只猫的两只耳朵：the ___ ears',["cat's","cats'",'cats'],"cat's",'主人只有一只；耳朵有两只。','撇号由拥有者 cat 决定，与耳朵数量分开。'),
 Q('two-counts','两只狗共用一个碗：the ___ bowl',["dog's",'dogs',"dogs'"],"dogs'",'拥有者是两只狗。','多只狗 dogs 的所有格是 dogs’。'),
 Q('contraction',"Lily's tired. 中的 Lily's 是什么？",['Lily is','莉莉的物品','多个莉莉'],'Lily is','把 is 放回去能否组成句子？','Lily is tired.：这里 ’s 缩写 is。'),
 Q('its','The bird opens ___ wings.',['its',"it's",'it'],'its','这里说“它的翅膀”。','its 表示它的；it’s 是 it is 或 it has 的缩写。'),
 Q('plural','三辆公交车：three ___',['bus',"bus's",'buses'],'buses','复数不需要撇号。','bus 的规则复数是 buses。'),
 Q('irregular',"这些男士的帽子：the ___ hats",["men's","mens'",'mens'],"men's",'men 已经是复数，不以 s 结尾。','men 的所有格是 men’s。'),
 Q('single',"Ben 的书：___ book",['Bens',"Ben's","Bens'"],"Ben's",'Ben 是一个人的名字。','Ben + ’s 表示 Ben 的。'),
 Q('contraction',"It's cold. 中的 It's 可以展开成什么？",['It is','它的','很多个它'],'It is','cold 在这里描述状态。','It is cold.；这里不是所属关系。')],transfer=[
 Q('plural','三只兔子：three ___',["rabbit's",'rabbits',"rabbits'"],'rabbits','只数数量。','rabbits 是复数，不用撇号。'),
 Q('single','一个老师的桌子：the ___ desk',["teacher's","teachers'",'teachers'],"teacher's",'只有一位老师。','单数 teacher 后加 ’s。'),
 Q('plural-owner','多个学生的书：the ___ books',["student's",'students',"students'"],"students'",'students 是以 s 结尾的复数。','在 students 后加撇号。'),
 Q('irregular','女士们的包：the ___ bags',["womens'","women's",'womens'],"women's",'women 已经是复数。','不以 s 结尾的复数所有格加 ’s。'),
 Q('two-counts','一位男孩的多辆玩具车：the ___ cars',["boys'","boy's",'boys'],"boy's",'先看拥有者，而不是车的数量。','一个 boy 拥有多辆 cars，用 boy’s cars。'),
 Q('contraction',"Tom's here. 是什么意思？",['Tom is here.','汤姆的这里','多个汤姆'],'Tom is here.','here 表示在这里。','这里 ’s 是 is 的缩写。'),
 Q('its','The dog wags ___ tail.',['it',"it's",'its'],'its','表示狗的尾巴。','its tail：它的尾巴。')]),
dict(id='simple-tenses',name='一般过去、现在与将来时',en='Simple Past, Present & Future',age='8–9',icon='🕰️',node='mt_Of-WsrRQ8B',mission='驾驶时间列车，送动词到正确的时间站。',boundary='一般现在表达习惯、事实或状态；本课用 will + 原形表达将来，不声称它是唯一方式。',lessons=[
 L('时间不是只看中文“现在”','先分清习惯、已发生、将来。',[
 V('每天 · 习惯','Mia plays tennis every day.','米娅每天打网球。',['Mia → 第三人称单数','plays → 一般现在','every day → 习惯'],'一般现在时表示习惯，不是说她此刻正在打球。'),
 V('昨天 · 已发生','Mia played tennis yesterday.','米娅昨天打了网球。',['Mia → 主语','played → 过去式','yesterday → 昨天'],'过去的事用过去式，不再因为 Mia 而加第三人称 s。'),
 V('明天 · 将来','Mia will play tennis tomorrow.','米娅明天将打网球。',['Mia → 主语','will play → will + 原形','tomorrow → 明天'],'will 后用原形 play；将来还可用其他表达，本课先学这一种。')]),
 L('过去式：规则变化与单独记忆','不是所有过去式都加 ed。',[
 V('规则动词','We walked home yesterday.','我们昨天走路回家。',['walk → walked','yesterday → 过去','We → 不改变过去式'],'常见规则变化加 ed；study → studied，stop → stopped 要留意拼写。'),
 V('不规则动词','We went home yesterday.','我们昨天回家了。',['go → went','不写 goed','yesterday → 过去'],'went 是 go 的过去式，需要结合例句单独记。')]),
 L('be 也有时间变化','be 不使用普通动词的加 ed 规则。',[
 V('今天的状态','I am happy today.','我今天很开心。',['I → am','happy → 状态','today → 今天'],'描述现在的状态可用一般现在时。'),
 V('昨天的状态','I was happy yesterday.','我昨天很开心。',['I → was','you / we / they → were','yesterday → 过去'],'am / is 的常用过去式是 was；you / we / they 配 were。'),
 V('将来的状态','I will be happy.','我会开心的。',['will → 将来','be → 原形','happy → 状态'],'will 后用 be，不写 will am 或 will was。')]),
 L('提问和否定，小助手负责变化','普通动词遇到 did 或 will 后，用原形。',[
 V('过去否定',"She didn't go out.",'她没有出去。',["didn’t → did not",'go → 原形','不用 went'],'过去的否定由 did 表示，后面的 go 回原形。'),
 V('过去提问','Did she go out?','她出去了吗？',['Did → 过去提问','she → 主语','go → 原形'],'Did she go…? 不写 Did she went…?。'),
 V('将来提问','Will she go out?','她会出去吗？',['Will → 提问','she → 主语','go → 原形'],'Will 放主语前；否定可用 will not / won’t。')]),
 L('同一个故事里的时间线','时间明确改变，时态可以跟着改变。',[
 V('先过去','Yesterday I visited Grandma.','昨天我看望了奶奶。',['Yesterday → 时间','visited → 过去式','Grandma → 奶奶'],'叙述过去的经历，保持过去时。'),
 V('再将来','Tomorrow I will visit Grandma again.','明天我将再次看望奶奶。',['Tomorrow → 时间改变','will visit → 将来','again → 再次'],'时间从昨天转到明天，改变时态是有理由的。')])],questions=[
 Q('habit','She ___ to school every day.',['walked','walks','will walked'],'walks','every day 表示这里的习惯。','一般现在时，she 配 walks。'),
 Q('past','Yesterday we ___ football.',['play','played','will play'],'played','yesterday 明确是过去。','规则动词 play 的过去式是 played。'),
 Q('future','Tomorrow he will ___ a cake.',['makes','made','make'],'make','will 后看动词原形。','will make，不受 he 的第三人称影响。'),
 Q('irregular','Last Sunday, we ___ to the zoo.',['goed','go','went'],'went','go 的过去式需要单独记。','go → went。'),
 Q('did',"She didn't ___ breakfast yesterday.",['eat','ate','eats'],'eat','didn’t 已经表示过去。','didn’t 后用原形 eat。'),
 Q('did','Did Ben ___ the door?',['opened','opens','open'],'open','小助手 Did 已经变化。','Did Ben open…?。'),
 Q('be','I ___ at home yesterday.',['am','was','were'],'was','过去的 I 配哪个 be？','I was，you / we / they were。'),
 Q('be','They ___ tired last night.',['was','are','were'],'were','last night 是过去，主语是 they。','They were tired last night.。'),
 Q('future','She will ___ ready soon.',['is','be','was'],'be','will 后的 be 保持原形。','will be，不用 will is。'),
 Q('habit','哪句表达平时的习惯？',['I read every evening.','I am reading now.','I read a book yesterday.'],'I read every evening.','找“经常、每天”的语境。','every evening 表示习惯；now 的那句是在进行。'),
 Q('spelling','Yesterday Lily ___ English.',['studyed','studies','studied'],'studied','study 以辅音字母 + y 结尾。','study → studied；这里是过去式，不是 studies。'),
 Q('timeline','Yesterday I played. Tomorrow I ___ again.',['played','will play','plays'],'will play','第二句把时间移到明天。','有明确时间变化，所以使用 will play。')],transfer=[
 Q('habit','Ben ___ books every night.',['reads','readed','will reads'],'reads','习惯，主语 Ben。','一般现在时 Ben 配 reads。'),
 Q('past','Last night, I ___ my room.',['clean','cleaned','cleans'],'cleaned','last night 是已过去的时间。','clean → cleaned。'),
 Q('future','Next week, we will ___ our aunt.',['visited','visits','visit'],'visit','will 后用原形。','will visit。'),
 Q('irregular','Yesterday she ___ an apple.',['eated','ate','eats'],'ate','eat 的过去式不加 ed。','eat → ate。'),
 Q('did','Did you ___ the game?',['enjoyed','enjoy','enjoys'],'enjoy','Did 承担过去的变化。','Did you enjoy…?。'),
 Q('be','You ___ at school yesterday.',['was','were','are'],'were','you 的过去 be 形式。','You were。'),
 Q('spelling','Yesterday the bus ___ here.',['stoped','stops','stopped'],'stopped','stop 的过去式需双写 p。','stop → stopped。'),
 Q('timeline','Last week I visited Ben. Next week I ___ Mia.',['will visit','visited','visits'],'will visit','next week 改成将来。','按新时间用 will visit。')]),
dict(id='standard-verb-forms',name='标准英语动词形式',en='Standard English Verb Forms',age='8–9',icon='🛠️',node='mt_ay0qkGj0jg',mission='帮句子修理站选择适合学校书面表达的动词。',boundary='标准书面形式是一种表达场合要求，不把家庭语言、方言或说话者贬为错误。',lessons=[
 L('先认清表达场合','本课练学校书面表达中的标准形式；不同社区有自己的语言变体。',[
 V('一个人，过去','He was at home.','他当时在家。',['He → 主语','was → 过去 be','at home → 地点'],'标准书面英语中 he 配 was；不据此评价说其他变体的人。'),
 V('多个人，过去','They were at home.','他们当时在家。',['They → 主语','were → 过去 be','at home → 地点'],'同样是过去，主语换成 they，be 用 were。')]),
 L('普通过去式和 have 后的形式','先看前面有没有 has / have / had。',[
 V('直接说过去','I saw the bird yesterday.','我昨天看见了那只鸟。',['saw → see 的过去式','yesterday → 过去','没有 have → 不用 seen'],'普通过去句用 saw，不写 I seen the bird yesterday.。'),
 V('已经见过','I have seen the bird.','我见过那只鸟。',['have → 小助手','seen → 过去分词','see → saw → seen'],'have 后用 seen，不写 have saw；这里先学形式配对，完成时另作深入学习。')]),
 L('do：did 和 done 有不同搭档','did 可以做主要动词，也可以做小助手。',[
 V('主要动词 did','She did her homework.','她做了作业。',['did → do 的过去式','her homework → 作业','直接说过去'],'这里 did 自己就是“做”的过去式。'),
 V('have + done','She has done her homework.','她已经做完了作业。',['has → 小助手','done → 过去分词','do → did → done'],'has 后用 done，不用 did。'),
 V('did + 原形','Did she do her homework?','她做作业了吗？',['Did → 提问小助手','do → 主要动词原形','不写 did done'],'提问的 Did 后，主要动词 do 用原形。')]),
 L('最常见的搭配别重复变化','看主语，也看小助手。',[
 V('have / has','She has a bike. They have bikes.','她有一辆自行车。他们有自行车。',['She → has','They → have','这里 have 表示拥有'],'一般现在时：she has，they have。'),
 V('doesn’t + 原形',"He doesn't like rain.",'他不喜欢下雨。',["He → doesn’t",'like → 原形','不写 doesn’t likes'],'doesn’t 后的主要动词用原形。'),
 V('can + 原形','She can swim.','她会游泳。',['can → 情态动词','swim → 原形','不写 can swims'],'不管主语是谁，can 后用动词原形。')]),
 L('更多不规则形式','同一动词的过去式和过去分词可能不同。',[
 V('go → went → gone','He went home. He has gone home.','他回家了。他已经回家了。',['went → 普通过去','has gone → has + 分词','不写 has went'],'gone 常表示去了而尚未回来；本课重点先认出 has gone 的形式。'),
 V('write → wrote → written','I wrote a note. I have written a note.','我写了便条。我已经写好一张便条。',['wrote → 普通过去','have written → have + 分词','不写 have wrote'],'不需要一口气背全部不规则动词表，先用常见词造句。')])],questions=[
 Q('was-were','学校书面表达：We ___ late yesterday.',['was','were','is'],'were','主语 we，过去的 be。','标准书面形式是 We were。'),
 Q('was-were','学校书面表达：She ___ at home last night.',['were','are','was'],'was','主语 she，过去的 be。','She was。'),
 Q('saw-seen','Yesterday I ___ a fox.',['seen','saw','seeing'],'saw','直接表达过去，前面没有 have。','see 的普通过去式是 saw。'),
 Q('saw-seen','I have ___ that film.',['saw','see','seen'],'seen','have 后需要过去分词。','have seen，不写 have saw。'),
 Q('did-done','She has ___ her homework.',['did','done','do'],'done','has 后用 do 的过去分词。','has done。'),
 Q('did-base','Did they ___ the job?',['done','did','do'],'do','Did 是提问小助手。','Did they do…?；do 用原形。'),
 Q('have-has','My sister ___ a red bike.',['have','has','having'],'has','my sister 可换成 she。','She has / My sister has。'),
 Q('does-base',"He doesn't ___ coffee.",['likes','like','liked'],'like','doesn’t 已经随主语变化。','doesn’t like。'),
 Q('modal','Lily can ___ fast.',['runs','ran','run'],'run','can 后的动词是什么形式？','can run，用原形。'),
 Q('went-gone','He has ___ home.',['went','go','gone'],'gone','has 后需要过去分词。','go → went → gone；has gone。'),
 Q('wrote-written','I have ___ a letter.',['written','wrote','write'],'written','have 后看过去分词。','write → wrote → written。'),
 Q('did-done','Yesterday she ___ the washing-up.',['done','did','does'],'did','直接说过去，前面没有 has。','普通过去式用 did。')],transfer=[
 Q('was-were','You ___ very helpful yesterday.',['was','were','is'],'were','you 的过去 be 形式。','标准书面形式 You were。'),
 Q('saw-seen','Ben has ___ a rainbow.',['saw','seen','see'],'seen','has 后用过去分词。','has seen。'),
 Q('did-done','We have ___ the work.',['did','do','done'],'done','have 后用分词。','have done。'),
 Q('did-base',"I didn't ___ the answer.",['knew','known','know'],'know','didn’t 后恢复原形。','didn’t know。'),
 Q('have-has','The children ___ lunch at school.',['has','have','having'],'have','children 是复数。','The children have lunch…。'),
 Q('does-base',"Mia doesn't ___ TV every day.",['watches','watch','watched'],'watch','doesn’t 后用原形。','doesn’t watch。'),
 Q('modal','They must ___ here.',['wait','waits','waited'],'wait','must 和 can 一样，后接原形。','must wait。'),
 Q('went-gone','Yesterday Ben ___ to the park.',['gone','went','go'],'went','没有 have，直接说过去。','普通过去式 went。'),
 Q('wrote-written','Last night, I ___ a story.',['written','write','wrote'],'wrote','直接描述昨晚的动作。','普通过去式 wrote。')]),
dict(id='progressive-tenses',name='进行时态',en='Progressive Tenses',age='9–10',icon='🎬',node='mt_mkDqmejLMw',mission='把动作定格，看看那一刻谁正在做什么。',boundary='涵盖现在、过去、将来进行时；强调 be + ing，否定、提问和常见状态动词的边界。',lessons=[
 L('习惯和正在进行不一样','像相机一样，定格某个时间的动作。',[
 V('平时的习惯','She reads every evening.','她每天晚上读书。',['reads → 一般现在','every evening → 习惯','不是某个瞬间'],'一般现在时不等于正在发生。'),
 V('此刻的动作','She is reading now.','她现在正在读书。',['She → 主语','is + reading → be + ing','now → 此刻'],'进行时需要 be 和 ing 动词一起工作，不能只写 She reading。')]),
 L('把同一个动作移到不同时间','变的是 be 部分，reading 保持 ing 形式。',[
 V('现在','They are reading now.','他们现在正在读书。',['They → 主语','are reading → 现在进行','now → 现在'],'I am；he / she / it is；you / we / they are，加 ing 动词。'),
 V('过去某一刻','They were reading at eight last night.','昨晚八点他们正在读书。',['They → 主语','were reading → 过去进行','at eight last night → 过去的一刻'],'I / he / she / it was；you / we / they were，加 ing 动词。'),
 V('将来某一刻','They will be reading at eight tomorrow.','明天八点他们将正在读书。',['They → 主语','will be reading → 将来进行','at eight tomorrow → 将来的一刻'],'will be + ing；will 后 be 用原形。')]),
 L('ing 的拼写工坊','规则服务于单词，不把一个口诀套给所有结尾。',[
 V('直接加 ing','play → playing','玩 → 正在玩',['play → 原形','playing → ing 形式','y 保留'],'多数动词直接加 ing：read → reading；play 不变 plaing。'),
 V('去不发音 e','make → making','制作 → 正在制作',['make → 去 e','making → 加 ing','see → seeing 保留 ee'],'常见不发音 e 结尾去 e；不是所有 e 结尾都去 e。'),
 V('双写末尾辅音','run → running','跑 → 正在跑',['run → 双写 n','running → 加 ing','stop → stopping'],'run、sit、stop 等常见短词按此模式；不要把所有辅音结尾都双写。'),
 V('ie 变 y','lie → lying','躺 → 正在躺',['lie → ie 换 y','lying → 加 ing','不是 lieing'],'先记常用例词 lie → lying。')]),
 L('否定和疑问都围绕 be','有 be 的进行时，不再添加 do 来提问。',[
 V('肯定','She is drawing.','她正在画画。',['She → 主语','is → be','drawing → ing 动词'],'两个部分 is + drawing 缺一不可。'),
 V('否定','She is not drawing.','她没有在画画。',['She → 主语','is not → be 后加 not','drawing → 保留 ing'],'把 not 放在 is 后面。'),
 V('提问','Is she drawing?','她正在画画吗？',['Is → 移到主语前','she → 主语','drawing? → 保留 ing'],'不写 Does she drawing?。将来进行时提问把 will 移到前面。')]),
 L('背景动作与发生的事情','一个动作进行着，另一个事情发生了。',[
 V('正在读书时响铃','I was reading when the phone rang.','电话响时，我正在读书。',['was reading → 进行中的背景','when → 当……时','rang → 响铃这件事'],'背景用过去进行时；发生的事件用一般过去时。'),
 V('状态不硬套 ing','I know the answer.','我知道答案。',['know → 知道这种状态','一般现在时','不写 I am knowing the answer.'],'know、believe 等常见状态意义通常不用进行时；有些动词换意义可有其他用法。')])],questions=[
 Q('present','Look! She ___ a picture.',['is drawing','draws every day','drawing'],'is drawing','Look! 指向此刻正在做的动作。','现在进行时 is + drawing，不能漏 is。'),
 Q('present','I ___ reading now.',['is','am','are'],'am','I 的 be 形式。','I am reading。'),
 Q('past','At seven yesterday, we ___ dinner.',['are eating','was eating','were eating'],'were eating','过去一刻，主语 we。','过去进行时 were eating。'),
 Q('future','At this time tomorrow, she will ___ sleeping.',['is','be','was'],'be','will 后 be 必须用原形。','will be sleeping。'),
 Q('spelling','run 的 ing 形式是？',['runing','running','runs'],'running','这个短词要双写末尾 n。','run → running。'),
 Q('spelling','make 的 ing 形式是？',['makeing','making','makking'],'making','先去掉末尾不发音 e。','make → making。'),
 Q('negative','“他现在没在跑。”选一句。',['He not running.','He is not running.','He does not running.'],'He is not running.','进行时保留 be，在其后放 not。','is not running。'),
 Q('question','“他们正在玩吗？”选一句。',['Do they playing?','Are they playing?','Is they playing?'],'Are they playing?','they 配 are，再把 are 放前面。','Are they playing?，不需要 do。'),
 Q('habit','Every Monday, Ben ___ tennis.',['plays','is play','playing'],'plays','这里说每周的习惯。','一般现在时 Ben plays，不是见动作就用 ing。'),
 Q('background','I ___ when the doorbell rang.',['was sleeping','will sleep','am sleeping'],'was sleeping','响铃时，睡觉这个动作已经在进行。','过去进行时 was sleeping 表示背景。'),
 Q('state','“我知道你的名字。”选一句。',['I am knowing your name.','I know your name.','I knowing your name.'],'I know your name.','know 在这里表示状态。','这种意义通常用一般现在时。'),
 Q('spelling','lie（躺）的 ing 形式是？',['lieing','lying','liing'],'lying','ie 先变成 y。','lie → lying。')],transfer=[
 Q('present','Listen! The birds ___ singing.',['is','are','am'],'are','birds 是复数。','The birds are singing。'),
 Q('past','At noon yesterday, he ___ cooking.',['were','is','was'],'was','过去某一刻，he 配哪个 be？','He was cooking。'),
 Q('future','At nine tomorrow, we ___ travelling.',['will be','will are','will'],'will be','将来进行需要 will + be + ing。','will be travelling（美式也常拼 traveling）。'),
 Q('spelling','sit 的 ing 形式是？',['siting','sitting','sitinging'],'sitting','常见短词 sit 双写 t。','sit → sitting。'),
 Q('negative','把 They are playing. 变成否定句。',['They not playing.','They are not playing.','They do not playing.'],'They are not playing.','在 are 后加 not。','They are not playing.。'),
 Q('question','“她当时正在读书吗？”',['Did she reading?','Was she reading?','Were she reading?'],'Was she reading?','过去进行时 she 配 was。','Was she reading?。'),
 Q('habit','My mum ___ tea every morning.',['drinks','drinking','is drink'],'drinks','every morning 表示习惯。','一般现在时 drinks。'),
 Q('background','We ___ when it started to rain.',['are walking','were walking','will walk'],'were walking','下雨发生时，我们已经在走路。','过去进行时 were walking 表示背景。'),
 Q('state','表示“我相信你”：',['I am believing you.','I believe you.','I believing you.'],'I believe you.','believe 在这里是状态。','这种意思通常不用进行时。')])
]
