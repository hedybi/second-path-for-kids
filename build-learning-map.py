import json
from pathlib import Path

root = Path(__file__).parent / 'dist/data'
source = json.loads((root / 'learning-map-source.json').read_text())
zh = json.loads((root / 'learning-map-zh.json').read_text())
reasons = {
13668:'做完后会检查，有助于进一步学会开始前先计划。',
15138:'先有检查结果的习惯，才能进一步调查出错原因。',
15144:'尝试过不同办法，才有具体经历可以分析哪里出了错。',
2772:'发现当前办法不奏效，才会意识到需要换方法。',
2778:'先有计划和选择，才谈得上主动更换策略。',
9948:'知道求助是合理的，能帮助孩子发现困惑后采取行动。',
10218:'愿意继续探索新内容，为主动唤起已有知识打下基础。',
1038:'先回想已有知识，才能把新旧想法联系起来。',
17202:'把不同想法连起来，有助于发现跨场景的重复规律。',
1974:'在数学中练习解释推理，有助于发展通用的自我解释能力。',
1980:'用自己的话解释，需要先调动已有知识来理解新内容。',
7788:'先发现重复模式，才能进一步把它说成一般规则。',
2796:'把办法迁移到新场景，需要先习惯寻找想法之间的联系。',
2802:'发现新旧场景的结构相似，有助于迁移已有办法。',
18048:'先能解释自己知道什么，才能进一步追问它为什么成立。',
13362:'评价学习方法，需要有主动选择和尝试不同方法的经历。',
13368:'早期在帮助下检查数学答案是否合理，有助于以后评价方法。',
13374:'在数学中检查答案的习惯，有助于以后评价学习策略。',
13380:'能分析方法为什么无效，才更容易判断它是否有帮助。',
16158:'用自己的话解释，有助于说清学习过程中哪些做法有效。',
16164:'分析错误能让学习后的回顾更具体。',
930:'评价方法的能力，可以扩展到检查整个主题的理解情况。',
936:'回顾每次学习的习惯，为检查整个主题的理解情况打基础。',
9366:'目标完成后要诚实回顾，需要先能看清自己的理解程度。',
9372:'设目标、行动、回顾，是早期简单计划习惯的进一步发展。'
}
assert len(source['topics']) == 18
assert len(source['dependencies']) == 25
for t in source['topics'] + source['externalTopics']:
    t['descriptionEn'] = t['description']
    t['promptEn'] = t['assessmentPrompt'].replace('{{name}}', 'your child')
    t.update(zh[t['id']])
for edge in source['dependencies']:
    edge['reasonZh'] = reasons[edge['sourceLine']]
out = 'export const learningMap = ' + json.dumps(source, ensure_ascii=False, indent=2) + ';\n'
(root / 'learning-map-data.js').write_text(out)
print('Generated 18 nodes, 22 internal links and 3 cross-subject prerequisites')
