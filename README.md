# Second Path · 第二路径

A bilingual family learning notebook based on Marble Skill Taxonomy. The default language is English; the language selector switches cases, forms, reports and the skill map to Chinese. The interface uses a dark background and green accents. Designed by Lianghuan Bi(Hedy Bi).

## Open the notebook

Open `deliverables/一起长大.html`, `dist/studio.html`, or `dist/index.html` directly in a browser. All three are identical standalone files with embedded styles, data and JavaScript, and need no server or installation. Refresh an already-open tab after rebuilding. The editable HTML template is `templates/studio.html`; do not edit a generated entry point.

## Cases and one observation template

Browse all 22 cases directly, with no category dropdown. Each includes materials, three concrete steps, a question and observable behaviors. Eighteen cases map to Learning to Learn and four offer additional family practice.

A separate blank template lets children name their own activity and describe materials, their own plan and what happened. These sessions retain their custom titles in reports and backups; they are not assigned to Marble skills. The behavior checklist is optional for a custom activity with a recorded attempt. Every supplied case also opens the shared observation form. Fill it during practice, generate a report, and download HTML or print to PDF. Earlier reports, backup controls and the cumulative learner summary are under “Reports & saved records” below the template.

The reports use transparent deterministic summaries of entered observations, not AI analysis, diagnoses, standardized scores or fixed learning-style labels. “Not observed” is missing evidence, not inability. Repeated independent observations require at least three distinct sessions across two dates before the summary describes repetition. Activities and checklists are authored adaptations, not validated assessments.

## Records

This version is local and has no account or cloud sync. Form drafts are cached locally. Enable “Keep records on this device” to retain generated sessions after closing the page; otherwise export a backup before leaving. Browser data can be cleared, so keep backups. Imported backups are validated, merge by session ID and never replace existing records with an older copy. Earlier `family-lab-v1` notes are preserved separately and are not counted as structured evidence. Browser storage for file URLs may differ between files and browsers: keep using the same entry point or transfer a JSON backup.

## Data and attribution

The map preserves 18 Learning to Learn nodes, 22 internal prerequisite relationships and 3 mathematics prerequisites from Marble Skill Taxonomy v1. The original excerpt is `dist/data/learning-map-source.json`; translated/adapted text is in `dist/data/learning-map-zh.json`. Outbound cross-subject edges are outside this view's scope. Original reference ages are not deadlines. Source names, IDs and ages were checked against the upstream GitHub data on 2026-09-10.

Source: https://github.com/withmarbleapp/os-taxonomy · © Generative Spark, Inc. (Marble). Database: ODbL 1.0; Marble-authored and adapted text: CC BY-SA 4.0. Third-party curriculum standards retain upstream terms and their text is not reproduced. The site footer and Sources & adaptations dialog contain attribution links.

## Build and checks

```sh
python3 build-learning-map.py
python3 make-offline.py
node check-learning-map.mjs
node check-reports.mjs
```

Checks cover source fidelity, graph integrity and traversal, all 22 bilingual cases, evidence validation, repeat-observation thresholds, backup merge behavior, escaping, self-contained entry points and bundled JavaScript syntax. These checks pass. Browser security policy blocked local-file preview, so click-through behavior, printed output and visual layout have not been verified in a browser. Optional WebMCP tools expose activity listing/navigation only; their runtime integration is unverified.

This package contains no account credentials, service registration or learner records. It has not yet been published.

## Publish manually on GitHub Pages

1. Create a public repository named `second-path-for-kids` under `hedybi`.
2. Upload the **contents** of this folder to the repository root, including `index.html`, `dist/`, `templates/`, the Python and JavaScript scripts, LICENSE and NOTICE.md. Do not upload the ZIP or the enclosing folder itself.
3. Commit the files to `main`.
4. In Settings → Pages, choose **Deploy from a branch**, then **main** and **/(root)**. Click Save.
5. Wait for the deployment to finish and open the URL shown by GitHub Pages. If there is no existing account-level custom domain, the expected address is https://hedybi.github.io/second-path-for-kids/ .

This manual-upload edition publishes directly from the branch, so it does not need a custom Actions workflow or any hidden files. A custom domain is optional. Browser-local learner records do not sync to GitHub.

After modifying the source, run the build and checks listed above. The build refreshes the repository-root `index.html` as well as the other standalone copies. Upload the changed files again to update the live site.

The bilingual footer links to https://github.com/hedybi/second-path-for-kids/issues/new for public suggestions and problem reports. No learner notes are attached to that link.
