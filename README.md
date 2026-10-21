# Second Path

A bilingual family learning project based on Marble Skill Taxonomy. Explore learning habits, mathematics and English through separate tools.

Second Path helps families observe how learning happens through everyday activities, explore subject skills, and ask informed questions using referenced curriculum materials.

**Designed by Lianghuan Bi(Hedy Bi).** English is the default interface language, with a Chinese option and a dark theme with green accents.

[GitHub repository](https://github.com/hedybi/second-path-for-kids) · [Feedback and suggestions](https://github.com/hedybi/second-path-for-kids/issues) · [Marble source project](https://github.com/withmarbleapp/os-taxonomy)

## Start with one of the two main tools

| Tool | What it offers | Website entry | Local build |
| --- | --- | --- | --- |
| **Learning to Learn** | Family activity cases, one flexible observation template, individual reports and a cumulative learner summary | [Open Learning to Learn](https://hedybi.github.io/second-path-for-kids/) | `dist/index.html`; `dist/studio.html` contains the same version |
| **Maths & English** | Mathematics and English skill maps, separate provisional Shanghai comparisons, and a contents-level BNU junior-secondary maths comparison | [Open Maths & English](https://hedybi.github.io/second-path-for-kids/subject-maps.html) | `dist/subject-maps.html` |

These are the intended website entry points. Availability depends on the GitHub Pages publishing directory and deployment result. Updating this README does not upload or deploy the pages.

**The maths game is a separate prototype and is excluded from the Maths & English map release.** Its local file is `dist/math-play.html`; see its description below.

## Shanghai sources and comparison: important limitations

> **The collection of Shanghai textbooks and related materials is incomplete. This is a provisional comparison based on the sources found so far, not a complete Shanghai syllabus, a full review of the new textbook series, or an official curriculum evaluation.**

- The intended scope is **ages 0–12 within Shanghai's education system**, with attention to the **new-textbook pathway for children who entered school in 2024**. It is not limited to Grade 3. Source availability varies across stages.
- Sources include national curriculum and education policies, Shanghai policies and teaching research, selected school teaching examples, and explicitly labelled third-party textbook contents or lesson-plan leads. **Policy goals, textbook content and actual classroom teaching are different kinds of evidence.**
- The new textbooks and their knowledge points have not been checked in full across all grades and terms. Some records are supported only by contents lists or teaching reports, which cannot establish the complete sequence of a textbook series. Current selection catalogues also cannot confirm every future edition a child will use.
- **“No corresponding source found” or “not yet matched” does not mean “Shanghai does not teach this,” “Marble does not contain this,” or “the child cannot do this.”** Identifying a difference requires checking both sides, their level of detail, age scope and supporting sources.
- The page includes the complete imported Marble mathematics and English inventories, but matching them to Shanghai content remains unfinished. A complete inventory is not a complete curriculum comparison, and match counts are not coverage percentages.
- General preschool language-development guidance is not an English syllabus. Reference ages in the imported Marble subjects begin at 4; no requirements for ages 0–3 have been extrapolated. Reference ages are not mastery deadlines.

Contributions of verifiable Shanghai textbook references, official curriculum documents and teaching research are welcome. Please include the **subject, grade, term, publisher, edition or year, and relevant page numbers or official links**. References and brief explanations are sufficient; there is no need to upload entire textbooks.

## Learning to Learn

Start with a small shared experience and observe how learning unfolds. A child does not need to have a problem that requires correction to use this tool.

- **22 activity cases:** 18 relate to Learning to Learn skills, with 4 additional family activities. Cases include materials, steps, questions and observable behaviours.
- **One flexible template:** children can invent an activity and record its title, materials, plan and what happened. Custom activities are not automatically assigned to a Marble skill.
- **Observation records and reports:** generate an individual report, download HTML or print to PDF, and export or import JSON backups.
- **A cumulative learner summary:** review observed behaviours and support needs. At least three distinct sessions across two dates are required before the summary describes repeated independent performance.
- **A Learning to Learn map:** preserves 18 Marble nodes, 22 internal prerequisite relationships and 3 mathematics prerequisites.

Reports use entered observations and fixed rules without calling an AI model. They are family observation notes, not standardized assessments, diagnoses or fixed learning-style classifications. Missing observations are not evidence of inability.

Records are stored in the current browser. Enable “Keep records on this device” to retain generated sessions, and export JSON backups regularly. Records do not automatically sync across devices, browsers, or local files and the published website.

## Maths & English

The standalone map page contains five tabs:

| Tab | Content |
| --- | --- |
| Mathematics | All 503 Marble mathematics topics in the original skill map |
| English | All 286 English topics in the imported Marble inventory |
| Shanghai Mathematics Comparison | Analysed differences, the complete Marble inventory, policy and learning goals, and available textbook evidence |
| Shanghai English Comparison | The same four views, with separate English sources and outstanding verification needs |
| BNU Mathematics Comparison | A standalone, bidirectional table comparing 127 contents headings from six 2024-revised BNU junior-secondary books with Marble mathematics topics |

The page supports English and Chinese, search and filters, topic descriptions, prerequisite relationships and original references. Chinese content includes adaptations; original English references remain available. In the BNU comparison tab, switch between **BNU textbook → Marble** and **Marble → BNU textbook**, then search in either language or filter by one of six volumes and reference status. The comparison covers six 2024-revised Grade 7–9 books, 37 chapters and 127 contents headings; 28 headings have 30 curated links to 23 Marble topics. This is a contents-level index, not a full skill-by-skill decomposition. The source headings come from public third-party contents pages; check the printed book actually used. The [Ministry of Education's 2024 textbook list](https://www.moe.gov.cn/srcsite/A26/s8001/202408/W020240805496325238752.pdf) and [2022 mathematics curriculum-standard notice](https://www.moe.gov.cn/srcsite/A26/s8001/202204/t20220420_619921.html?fromColId=204) provide official context. Curated links are editorial navigation aids, not official equivalences, prerequisites or evidence of full coverage. An unmapped heading or Marble topic is unresolved, not proof of a missing skill. The Shanghai-comparison tabs remain separate. The map page does not collect learner records or include the maths game.

The current comparison data contains 15 selected textbook and teaching evidence records, 19 detailed comparisons and 6 policy comparisons. In mathematics, 95 topics have selected content-evidence associations and 408 remain unassociated; the English counts are 71 and 215. **These are editorial association counts, not measures of Shanghai textbook coverage or missing curriculum content.**

Nine mathematics topics have a Marble reference starting age of 13; the other 494 start at 12 or below. All 286 English topics start at 12 or below. These ages are not directly converted into Shanghai grades. Some findings based on an early national mathematics curriculum PDF still require checking against the corrected edition and original Shanghai textbooks.

See the [Maths & English module README](subject-maps/README.md) for source data, Chinese adaptations and comparison maintenance details.

## Child-friendly edition: Discovery Club

A separate, bright interface for the same 503 mathematics and 286 English topics is available locally at `deliverables/kids-maps.html` (also `dist/kids-maps.html`). It includes domain islands, bilingual search, original references and prerequisite links, with no Shanghai comparisons or games.

Children can keep a local stamp book using “Want to try,” “Exploring,” and “Can explain it,” with an optional note per topic and JSON backup import/export. Stamps record personal exploration, not measured mastery; there are no daily streaks. This edition has not been deployed. See the [Discovery Club module README](kids-maps/README.md) for use, storage limits and build instructions.

## Separate prototype: Maths Adventures

Local build: `dist/math-play.html`. **This page is excluded from the Maths & English map release.**

Five challenges cover budgets, perimeter, equivalent fractions, equal-step patterns and data comparisons, each with two fixed situations. Second Path authored the challenges and linked them to selected Marble nodes. They are not an official Marble question bank and cannot assess the complete mathematics taxonomy or Shanghai curriculum.

A separate “Parent observation guide” tab within the prototype covers the 8 nodes linked to the challenges. It provides observable evidence (`evidence`), assessment questions (`assessmentPrompt`), all 16 direct prerequisite relationships and their reasons, and relevant domain summaries and curriculum associations. Chinese adaptations and upstream originals remain separate.

Completion states describe the current attempt and whether support was used. There are no rankings, age norms or overall mastery percentages. Records are stored in the browser and can be downloaded as text. See the [Maths Adventures module README](math-play/README.md).

## Files: pages, source code and documentation

**One repository can host both main tools. Two website addresses do not require two repositories.** Each tool has its own HTML entry point, with one overview `README.md` at the repository root.

| File or directory | Purpose |
| --- | --- |
| `README.md` | Project navigation, tool descriptions, source limitations and usage instructions |
| `templates/studio.html` | Editable HTML template for Learning to Learn |
| `dist/studio.js`, `dist/content.js`, `dist/reports.js`, `dist/learning-map.js`, `dist/studio.css`, `dist/data/` | Editable Learning to Learn code, styles and data; these currently live in `dist/`, so do not delete that entire directory as a build cache |
| `subject-maps/` | Maths & English source code, data, translations and module documentation, including `bnu2024.json`, `app.js`, `audit.js`, `audit.css` and `audit-data.py` |
| `math-play/` | Source code, data and module documentation for the separate maths-game prototype |
| Root-level `build-*.py` and `make-offline.py` | Scripts that generate the standalone pages |
| Root-level `check-*.mjs` | Data and program checks |
| `dist/index.html`, `dist/studio.html`, `dist/subject-maps.html`, `dist/kids-maps.html`, `dist/math-play.html` | Generated pages that can be opened directly in a browser; the child-friendly map and maths game are separate editions/prototypes |
| Root-level `subject-maps.html` | Mirror of the generated Maths & English map for branch-root Pages publishing; preserve the homepage `index.html` |
| `deliverables/` | Delivery or upload copies; older release packages may lag behind the current source |
| `LICENSE`, `NOTICE.md` | Code licensing and attribution for data and content |

If map files such as `app.js`, `audit.js` or `audit-data.py` appear at the repository root, module files may have been flattened during upload. The table describes the structure required by the build scripts. **Updating the README does not move these files.** When organizing the repository, verify their contents and restore them to `subject-maps/`. Keep the module README inside its module directory instead of using it to replace this project overview.

Each standalone HTML file embeds its required styles, scripts and data, so publishing that page does not require a separate `audit.js` or similar runtime file. For open-source maintenance, retain the editable source, data, build scripts and license files so others can inspect, modify and rebuild the project.

## Local use and builds

Open a generated HTML file directly in a browser. No server installation, database or AI API key is required. Source links and GitHub feedback require internet access.

Development requires Python 3 and Node.js; the existing workflow uses Node.js 24. Run the following commands from the repository root with the source directory structure described above.

### Learning to Learn

```sh
python3 build-learning-map.py
python3 make-offline.py
node check-learning-map.mjs
node check-reports.mjs
```

Outputs: `dist/index.html`, `dist/studio.html` and `deliverables/一起长大.html`.

### Maths & English maps

```sh
python3 subject-maps/shanghai-data.py
python3 subject-maps/audit-data.py
python3 build-subject-maps.py
node check-subject-maps.mjs
```

Outputs: `dist/subject-maps.html` and `deliverables/subject-maps.html`. Interface-only changes do not require regenerating the Shanghai and comparison data. For source updates, edit the relevant data-generation scripts first.

### Separate maths-game prototype

```sh
python3 math-play/data.py
python3 math-play/guide-data.py
python3 build-math-play.py
node check-math-play.mjs
```

Outputs: `dist/math-play.html` and `deliverables/math-play.html`. Some checks also use the existing Maths & English build, so build the maps first.

After source changes, rebuild and update the generated HTML. Data and program checks do not replace browser visual review or establish that the Shanghai research is complete or the activities are validated assessments.

## Publishing and updating GitHub Pages

First check the publishing method under **Settings → Pages**. GitHub supports publishing from a branch's root or `docs/` directory, or through GitHub Actions. See the [official GitHub publishing guide](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

The current [Pages workflow](.github/workflows/pages.yml) publishes the entire `dist/` directory from GitHub Actions. It rebuilds Learning to Learn but does not rebuild the Maths & English page. To keep the map current, run the map build and checks below, then update `dist/subject-maps.html` in the repository. Also keep a root-level `subject-maps.html` copy: it is used if Pages is configured to publish from the `main` branch root, and it is easy to open from the repository. **Do not upload the whole local `dist/` folder just to update the map.**

The two public entry points should be:

| Local file | Name at the repository root | Destination |
| --- | --- | --- |
| `dist/index.html` | `dist/index.html` for the current Actions workflow; `index.html` if publishing from the branch root | [Learning to Learn](https://hedybi.github.io/second-path-for-kids/) |
| `dist/subject-maps.html` | `dist/subject-maps.html` for the current Actions workflow, plus a root-level `subject-maps.html` copy | [Maths & English](https://hedybi.github.io/second-path-for-kids/subject-maps.html) |
| This README | `README.md` | GitHub repository overview |

**Do not rename `subject-maps.html` to `index.html` and overwrite the Learning to Learn entry point.** Both pages can coexist at the URLs above. Use the latest generated `dist/subject-maps.html`; older copies under `deliverables/` may not include recent changes.

The workflow publishes every file already present in the repository's `dist/` directory. Updating only `subject-maps.html` will leave other pages untouched, but any other tracked HTML in `dist/` may also be publicly reachable. The separate maths-game prototype and child-friendly edition are not part of the Maths & English map page.

Confirm the Pages deployment result and open both actual pages after updating. A green check beside a commit alone does not confirm that every entry point works correctly.

## Frequently asked questions

**Where did Learning to Learn go?**

Try the Learning to Learn link above. If the homepage displays Maths & English, check whether `index.html` in the publishing directory was replaced. The local Learning to Learn build remains `dist/index.html` or `dist/studio.html`. Replacing a README and replacing a website entry point are separate issues.

**Which HTML copy should I edit: `dist/`, `deliverables/` or the repository root?**

Edit the corresponding module's source and rebuild, then copy the latest generated page into the actual publishing directory. Avoid manually editing several HTML copies independently. Updating source files alone does not update an already uploaded standalone HTML file.

**Why does GitHub show code when I open an HTML file?**

The repository view displays files. Use the GitHub Pages links above, or download the HTML and open it in a browser.

## Feedback and contributions

Share suggestions, bugs or source references through [GitHub Issues](https://github.com/hedybi/second-path-for-kids/issues), where the maintainer can read and reply. Pull requests are also welcome.

Please name the tool, interface language and issue or suggestion. For curriculum comparisons, include a specific source and edition. For interface issues, describe the steps, expected result and actual result. Public feedback does not need a child's name, school or complete personal learning report.

## Sources and licenses

This project is based on [Marble Skill Taxonomy v1](https://github.com/withmarbleapp/os-taxonomy), copyright **Generative Spark, Inc. (Marble)**. Second Path adds bilingual interfaces, content adaptations, family activities, observation records and curriculum-source organization.

- Database and derived topic/dependency mappings: **ODbL 1.0**.
- Marble-authored learning content, translations and related activity adaptations: **CC BY-SA 4.0**.
- Original application code, styles and artwork: **MIT**, see [LICENSE](LICENSE).
- Third-party standards, textbooks and other sources retain their own terms; consult [upstream PROVENANCE](https://github.com/withmarbleapp/os-taxonomy/blob/main/PROVENANCE.md) and the individual sources.

See [NOTICE.md](NOTICE.md). Generated HTML contains both code and separately licensed data and content; the MIT license does not apply to every included material. The Shanghai comparison provides brief summaries, editorial interpretations and source links, not entire textbooks.

**Design and maintenance: Lianghuan Bi(Hedy Bi)**
