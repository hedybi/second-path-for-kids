# Grammar Adventures

Six ready-to-play English grammar modules for **Second Path**, with Chinese explanations and simple English examples.

**[Play in your browser](https://hedybi.github.io/second-path-for-kids/skills/grammar-adventures/game.html)** · [Teaching skill](SKILL.md) · [Original subject–verb agreement guide](../subject-verb-agreement/README.md)

## Play

Use a module’s **Play** link to open it directly, or choose a module in the shared game. Explore **动画课堂与实验** (lessons and sentence experiments), then try **线索闯关** (12 questions). **错题换句练** gives new examples for topics that needed hints or retries. Each module has five short lessons. There is no timer or penalty for mistakes.

| Module | Reference ages | Play |
| --- | --- | --- |
| [Question Words & Questions](question-words.md) | 5–6 | [Play](https://hedybi.github.io/second-path-for-kids/skills/grammar-adventures/question-words.html) |
| [Agreement in Sentences](sentence-agreement.md) | 8–10 | [Play](https://hedybi.github.io/second-path-for-kids/skills/grammar-adventures/sentence-agreement.html) |
| [Plurals & Possessives](plurals-and-possessives.md) | 8–9 | [Play](https://hedybi.github.io/second-path-for-kids/skills/grammar-adventures/plurals-and-possessives.html) |
| [Simple Past, Present & Future](simple-tenses.md) | 8–9 | [Play](https://hedybi.github.io/second-path-for-kids/skills/grammar-adventures/simple-tenses.html) |
| [Standard English Verb Forms](standard-verb-forms.md) | 8–9 | [Play](https://hedybi.github.io/second-path-for-kids/skills/grammar-adventures/standard-verb-forms.html) |
| [Progressive Tenses](progressive-tenses.md) | 9–10 | [Play](https://hedybi.github.io/second-path-for-kids/skills/grammar-adventures/progressive-tenses.html) |

Ages are approximate map labels, not deadlines. Completion is practice evidence, not a mastery assessment.

## Use with your AI

Give your AI [SKILL.md](SKILL.md) and the relevant module reference, or install this folder as a skill in your supported AI client. Ask:

> Use Grammar Adventures to teach question words. Explain in Chinese. Open the bundled interactive game if this chat supports it; otherwise ask one question at a time and wait for the child's answer.

Installing a skill alone does not launch a game. Inline play needs a client that can render interactive content. In Codex, the `grammar-adventures.html` fragment is used for the inline experience; `game.html` is the browser-ready version. This repository does not supply a one-click installer.

## Offline and privacy

Download **[game.html](game.html)** using GitHub's **Download raw file** control, then open it in a browser. GitHub's file viewer shows source; it does not run the game. The game requires no account, server or paid AI API. Progress stays in the current chat or browser when saving is supported and does not sync across devices. Using an AI to adapt lessons follows that AI account's limits.

## Maintain

Edit `content.py`, `template.html` and `engine.js`; rebuild with `python3 build.py --renderer /path/to/visualize/scripts/render.py`, then run `node verify.cjs` in the output folder. The renderer belongs to the Codex visualize skill; it is not bundled here. Prebuilt play does not require it. `lessons.json` records the full generated question bank.

Map IDs and reference ages come from [Marble Skill Taxonomy v1](https://github.com/withmarbleapp/os-taxonomy), © Generative Spark, Inc. (Marble), under ODbL 1.0 for database material and CC BY-SA 4.0 for source learning content. These are original supplementary activities, not official Marble assessments. See the repository [license](../../LICENSE) and [notice](../../NOTICE.md).
