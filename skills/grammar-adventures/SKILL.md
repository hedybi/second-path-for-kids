---
name: grammar-adventures
description: Teach six primary English grammar topics through Chinese explanations, sentence experiments and short games—question words, sentence agreement, plurals and possessives, simple tenses, standard verb forms, and progressive tenses. Use for interactive teaching or adapting the bundled lessons.
---

# Grammar Adventures

Support the child's selected topic using the bundled original bilingual activities. Ages label approximate map ranges, not mastery deadlines. Adapt reading demands to the child; an adult may read questions aloud for younger learners.

## Start with the requested experience

- If the user wants to play, use the bundled `grammar-adventures.html` fragment in a supported Codex inline surface. It contains all six modules. For browsers or downloads, use the standalone `game.html`; never present the host-dependent fragment as a standalone page.
- If an interactive renderer is unavailable, teach in chat: one question at a time, wait for the child's response, then give a short hint or explanation. Do not claim that a clickable game is running.
- If the user wants a custom game, edit the relevant module in `content.py`, preserve sound examples and targeted transfer questions, then rebuild with `build.py --renderer /path/to/visualize/scripts/render.py`. The export helper is environment-specific; prebuilt `game.html` needs no build tooling.
- For text-only requests, provide the requested text. Loading this skill does not authorize repository changes or publication.

## Select only the relevant module reference

| Topic | Reference | Approximate ages |
| --- | --- | --- |
| Question words and simple questions | [question-words.md](question-words.md) | 5–6 |
| Agreement in sentences | [sentence-agreement.md](sentence-agreement.md) | 8–10 |
| Plurals and possessives | [plurals-and-possessives.md](plurals-and-possessives.md) | 8–9 |
| Simple past, present and future | [simple-tenses.md](simple-tenses.md) | 8–9 |
| Standard English verb forms | [standard-verb-forms.md](standard-verb-forms.md) | 8–9 |
| Progressive tenses | [progressive-tenses.md](progressive-tenses.md) | 9–10 |

Read the matching reference for the lesson sequence. Read `lessons.json` when adapting questions, hints or feedback; it is the generated full bank. Do not load all references just to teach one topic.

## Teaching decisions

Begin with a concrete contrast and change one important condition at a time. Show the English sentence, Chinese meaning, grammatical parts and a short explanation of why the form changes. Let the learner operate the change before choosing an answer. Prefer familiar daily vocabulary.

After a mistake, identify the relevant condition and allow another try. Offer a new sentence testing the same distinction. Distinguish independent first-attempt success from hinted or retried success; completion alone is not mastery. Do not invent assessment results, learning history or cross-device records.

### Content boundaries

- Question words: choose the information sought before manipulating word order. Distinguish be questions, ordinary do/does questions and subject questions such as `Who likes apples?`; no universal “every question needs do” formula.
- Agreement: find the subject head rather than the nearest noun; align pronouns with their referents. Accept singular they with `are/have`. Avoid unsupported claims that collective-noun agreement is identical in all varieties of English.
- Possession: separate owner number from object number. Contrast `dogs`, `dog's`, `dogs'`, `children's`, `its` and `it's`. Do not treat every apostrophe-s as possession.
- Simple tenses: present includes habits, facts and states. `will + base form` is the introductory future pattern, not the only future expression. Distinguish be from ordinary verbs and restore base forms after did/will.
- Standard forms: teach school-writing conventions without devaluing dialects, families or speakers. Separate past forms from participles (`saw/seen`, `did/done`, `went/gone`); the module introduces these pairings, not a complete course in perfect aspect.
- Progressive: require be + ing, choose be for subject and time, and retain be for questions and negatives. Explain common spelling changes without treating them as exceptionless; avoid progressive forms for ordinary state meanings of know/believe.

## Delivery and verification

Maintain keyboard-accessible controls, responsive layout and reduced-motion support. The ready-made game uses a fixed local bank, no login, no API calls and no remote learner-data collection. State restoration is limited to the current chat or browser; gracefully keep playing if saving is unavailable.

Before releasing changes, check answer uniqueness, examples and explanations; run `node verify.cjs` from this folder and inspect the rendered interface. Verify lesson switching, incorrect answers, hints, locked completed answers, next-question navigation and transfer review. A state-engine test does not replace browser review.

If screenshots are added later, use actual captures of the delivered game. Label standalone previews versus captures inside Codex accurately; never fabricate app chrome or imply a particular AI client supports inline play without checking. Preserve source map IDs and label the activities as original supplementary exercises, not official Marble assessments.
