# Second Path · 第二路径

A bilingual family learning project based on Marble Skill Taxonomy. Explore learning habits, mathematics and English through separate tools.

一个帮助家长与孩子一起探索学习的开源项目：从具体活动中观察学习过程，通过能力图谱了解数学与英语，再结合有出处的课程资料提出问题。

**Designed by Lianghuan Bi(Hedy Bi).** 英文默认界面，支持中文切换；黑底与绿色配色。

[GitHub 仓库](https://github.com/hedybi/second-path-for-kids) · [反馈与建议](https://github.com/hedybi/second-path-for-kids/issues) · [Marble 原项目](https://github.com/withmarbleapp/os-taxonomy)

## 两个主要工具，从这里进入

| 工具 | 适合做什么 | 网站入口 | 对应的本地成品 |
| --- | --- | --- | --- |
| **Learning to Learn · 学会学习** | 看亲子案例、填写万能观察模板、导出报告与汇总记录 | [打开学会学习](https://hedybi.github.io/second-path-for-kids/) | `dist/index.html`，同版文件为 `dist/studio.html` |
| **Maths & English · 数学与英语** | 浏览数学、英语能力图谱，以及上海课程资料的阶段性对比 | [打开数学与英语](https://hedybi.github.io/second-path-for-kids/subject-maps.html) | `dist/subject-maps.html` |

以上是本项目约定的网站入口。实际能否访问取决于 GitHub Pages 的发布目录和部署结果；更新这份 README 不会自动上传或发布页面。

**数学小游戏是另一个独立原型，不属于“数学与英语”图谱页面的发布内容。** 它的本地文件是 `dist/math-play.html`，介绍见下方。保留这些区别，避免把学习记录、图谱和游戏混为一个工具。

English: Use **Learning to Learn** for family activities and observation records. Use **Maths & English** for subject maps and a provisional Shanghai comparison. The maths game is a separate prototype. Shanghai source collection and curriculum matching are incomplete; an unmatched skill does not establish a curriculum gap or a child's learning deficit.

## 上海资料与对比：请先了解这些限制

> **上海教材及相关资料目前收集不完整。这里是基于已找到资料的阶段性对比，不是完整的上海教纲、全套新教材审校结果，也不是官方课程评价。**

- 范围面向 **0–12 岁、上海教育体系**，关注 **2024 年入学儿童的新教材路径**，并非仅限三年级。不同年龄段的资料完整程度不同。
- 资料包括国家课程与教育政策、上海地方政策和教研材料、部分学校教学实例，以及明确标注的第三方教材目录或教案线索。**政策目标、教材内容、课堂实际教学是不同层次的证据。**
- 上海各年级、各学期的新教材原文与知识点尚未全部核验。部分内容只有目录或教学报道支持，不能据此推断一套教材的完整安排；现有选用目录也不能确定孩子未来每一年会使用的版本。
- **“未找到对应资料”“尚未匹配”不等于“上海不教”或“Marble 没有”，更不等于“孩子不会”。** 判断差异需要同时检查双方内容、表述粒度、年龄范围和证据来源。
- Marble 数学与英语条目清单已完整列入本页，但与上海课程的逐点对应仍未完成。不能把清单完整当成课程对比完整，也不能把匹配数量当作覆盖率。
- 学龄前的一般语言发展指导不等于英语课程要求；Marble 本次导入科目的参考年龄从 4 岁开始，没有据此推导 0–3 岁要求。参考年龄也不是必须掌握的期限。

欢迎补充可核验的上海新教材、官方课程文件或教研资料。请附**科目、年级、学期、出版社、版次或年份、相关页码或官方链接**。可以提供引用信息与简短说明，不需要上传整本教材。

## Learning to Learn · 学会学习

从“小小的体验”开始记录学习怎样发生，不要求孩子先有一个需要纠正的问题。

- **22 个案例**：18 个关联学会学习能力，另有 4 个亲子拓展练习；提供材料、步骤、提问与可观察表现。
- **一个万能模板**：孩子可以自创活动，填写活动名称、材料、计划和尝试中发生的事情；自创活动不会被自动归入某项 Marble 能力。
- **观察记录与报告**：填写后生成单次报告，下载 HTML 或通过打印保存 PDF；支持 JSON 备份与导入。
- **学习者观察汇总**：汇总已有记录中的表现与支持需求。至少三个独立活动记录、分布在两个日期，才会描述重复出现的独立表现。
- **学会学习图谱**：保留 18 个 Marble 节点、22 条内部前置关系和 3 项数学前置能力。

报告依据填写的内容和固定规则生成，不调用 AI 模型。它是家庭观察笔记，不是标准化测评、诊断或固定“学习类型”判定；未观察到的表现不能被当作能力不足。

记录保存在当前浏览器中。启用“在此设备保留记录”可保留生成的活动记录，建议定期导出 JSON 备份。不同设备、浏览器以及本地文件和线上网站之间不会自动同步。

## Maths & English · 数学与英语

独立图谱页面包含四个标签页：

| 标签页 | 内容 |
| --- | --- |
| 数学 | Marble 的 503 个数学知识与能力点 |
| 英语 | Marble 的 286 个英语知识与能力点 |
| 上海数学对比 | 已分析差异、完整 Marble 清单、政策与学习目标、已有教材证据 |
| 上海英语对比 | 同样的四类视图，单独列出英语资料与待核验内容 |

支持中英文、搜索与筛选，查看节点说明、前置关系及原文参考。中文内容包括翻译与简明改写；原始英文参考保留在页面中。图谱页不收集学习记录，不包含数学小游戏。

当前对比数据包含 15 条精选教材及教学证据记录、19 条深入对比和 6 条政策对比。数学有 95 个点关联了选定的内容证据，408 个点尚未关联；英语分别为 71 个和 215 个。**这些是编辑整理的关联数量，不是上海教材的覆盖率或缺失数量。**

数学清单中有 9 个点的 Marble 参考起始年龄为 13 岁，其余 494 个为 12 岁及以下；英语 286 个均为 12 岁及以下。这些年龄没有被直接换算成上海年级。涉及国家数学课标早期 PDF 的部分判断仍需结合更正版本及上海教材原本复核。

源数据、汉化与对比的维护说明见 [数学与英语模块 README](subject-maps/README.md)。

## 独立原型：Maths Adventures · 数学小冒险

本地成品：`dist/math-play.html`。**本次数学与英语图谱发布不包含这个页面。**

五个挑战围绕预算、周长、等值分数、等差规律、数据比较展开，每个挑战有两种固定情境。题目由 Second Path 编写，关联部分 Marble 节点；不是 Marble 官方题库，也不能评估整个数学图谱或上海数学课程。

页面另有“家长观察指南”标签页，针对挑战关联的 8 个节点提供：能力表现证据（evidence）、观察提问（assessmentPrompt）、16 条直接前置关系及原因，以及对应的领域概述和课标关联。中文改写与上游原文分别保留。

完成状态只描述这一次尝试及是否使用帮助；没有排名、年龄常模或整体掌握率。记录存于浏览器，可下载文本。详见 [数学小冒险模块 README](math-play/README.md)。

## 文件怎么分：网页、源码和说明

**同一个仓库可以容纳两个主要工具，不需要为两个网址再建两个仓库。** 每个工具有自己的 HTML 入口；根目录只需要一份综合 `README.md`。

| 文件或目录 | 用途 |
| --- | --- |
| `README.md` | 仓库总导航、工具说明、资料限制与使用方法 |
| `templates/studio.html` | 学会学习页面的可编辑 HTML 模板 |
| `dist/studio.js`、`dist/content.js`、`dist/reports.js`、`dist/learning-map.js`、`dist/studio.css`、`dist/data/` | 学会学习的可编辑程序、样式与数据；目前放在 `dist/`，不能把整个目录当缓存删除 |
| `subject-maps/` | 数学与英语图谱的源码、数据、翻译及模块说明，包括 `app.js`、`audit.js`、`audit.css`、`audit-data.py` 等 |
| `math-play/` | 独立数学小游戏原型的源码、数据与模块说明 |
| 根目录的 `build-*.py`、`make-offline.py` | 生成网页的构建脚本 |
| 根目录的 `check-*.mjs` | 数据与程序检查脚本 |
| `dist/index.html`、`dist/studio.html`、`dist/subject-maps.html`、`dist/math-play.html` | 构建生成的可直接打开的网页 |
| `deliverables/` | 交付或上传副本；旧发布包可能落后于当前源码 |
| `LICENSE`、`NOTICE.md` | 代码许可、数据及内容来源说明 |

如果仓库根目录已经出现 `app.js`、`audit.js`、`audit-data.py` 等图谱文件，说明模块文件可能在上传时被平铺到了根目录。上表描述的是构建脚本要求的目录结构，**更新 README 不会自动移动这些文件**。后续整理时应核对内容并放回 `subject-maps/`，保留模块自己的 README，不用它覆盖仓库总 README。

独立 HTML 已嵌入运行所需的样式、脚本和数据，所以单独发布网页时不需要额外的 `audit.js` 等文件。开源维护则应保留源码、数据、构建脚本和许可文件，让其他人可以检查、修改和重新生成网页。

## 本地使用与构建

直接用浏览器打开生成的 HTML 即可使用，无需安装服务、数据库或配置 AI API Key。访问来源链接或 GitHub 反馈需要联网。

修改项目需要 Python 3 与 Node.js（现有工作流使用 Node.js 24）。下面的命令在仓库根目录执行，并依赖上表中的源码目录结构。

### 学会学习

```sh
python3 build-learning-map.py
python3 make-offline.py
node check-learning-map.mjs
node check-reports.mjs
```

输出 `dist/index.html`、`dist/studio.html` 和 `deliverables/一起长大.html`。

### 数学与英语图谱

```sh
python3 subject-maps/shanghai-data.py
python3 subject-maps/audit-data.py
python3 build-subject-maps.py
node check-subject-maps.mjs
```

输出 `dist/subject-maps.html` 和 `deliverables/subject-maps.html`。只调整界面时不需要重新生成上海与对比数据；调整资料时应先修改相应的数据生成脚本。

### 独立数学小游戏原型

```sh
python3 math-play/data.py
python3 math-play/guide-data.py
python3 build-math-play.py
node check-math-play.mjs
```

输出 `dist/math-play.html` 和 `deliverables/math-play.html`。部分检查也使用已有的数学与英语成品，应先构建图谱。

修改源码后需要重新构建并更新成品 HTML。数据与程序检查不等于浏览器视觉验收，也不能证明上海资料收集完整或活动具有测评效度。

## GitHub Pages 发布与更新

先确认仓库 **Settings → Pages** 当前使用的发布方式。GitHub 支持从分支的根目录或 `docs/` 发布，也支持 GitHub Actions；具体操作见 [GitHub 官方发布说明](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)。

如果当前从 `main` 分支的根目录发布，两个主要入口应这样放置：

| 本地文件 | 上传到仓库根目录后的名字 | 对应网址 |
| --- | --- | --- |
| `dist/index.html` | `index.html` | `https://hedybi.github.io/second-path-for-kids/` |
| `dist/subject-maps.html` | `subject-maps.html` | `https://hedybi.github.io/second-path-for-kids/subject-maps.html` |
| 本 README | `README.md` | GitHub 仓库首页说明 |

**不要把 `subject-maps.html` 改名为 `index.html` 覆盖学会学习入口。** 两个 HTML 可以并存，README 负责将两个入口列清楚。发布数学与英语时可使用 `deliverables/github-maths-english/subject-maps.html` 副本，但应确保它与最新构建一致。

现有 `.github/workflows/pages.yml` 只构建和检查学会学习，却会将整个 `dist/` 作为网站发布。因此，若使用这个工作流，需要另行补齐数学与英语的构建步骤，并明确限定要发布的成品；否则已有的游戏原型也可能随 `dist/` 一起发布。这份 README 的更新没有修改工作流。

更新后以 Pages 部署结果及实际打开两个页面为准，不能仅凭提交旁的绿色勾判断所有入口都正确。

## 常见问题

**找不到 Learning to Learn 了？**

先打开上方“学会学习”入口。若首页显示数学与英语，检查发布目录里的 `index.html` 是否被替换；学会学习本地成品仍是 `dist/index.html` 或 `dist/studio.html`。README 被覆盖与网页入口被覆盖是两件不同的事。

**`dist/`、`deliverables/` 和根目录的 HTML，应该改哪份？**

修改对应模块源码，再构建生成成品；将最新成品复制到实际发布目录。不要分别手工修改多个 HTML 副本。仅更新源码不会自动更新已经上传的独立 HTML。

**为什么打开 GitHub 里的 HTML 看到的是代码？**

GitHub 仓库页面用于查看文件。请使用上方 GitHub Pages 网址，或下载 HTML 后用浏览器打开。

## 反馈与参与

在 [GitHub Issues](https://github.com/hedybi/second-path-for-kids/issues) 留下建议、问题或资料补充，维护者可以在仓库中查看与回复；也欢迎提交 Pull Request。

反馈时请说明工具名称、使用语言、问题或建议。课程对比请附具体来源和版本；界面问题请描述操作步骤、预期结果和实际结果。公开反馈不需要孩子的姓名、学校或完整个人学习报告。

## 来源与许可

本项目基于 [Marble Skill Taxonomy v1](https://github.com/withmarbleapp/os-taxonomy)，上游版权归 **Generative Spark, Inc. (Marble)** 所有。Second Path 提供中英文界面、内容改写、亲子活动、观察记录与课程资料整理。

- 数据库与派生的节点、依赖映射：**ODbL 1.0**。
- Marble 编写的学习内容、翻译与相应活动改写：**CC BY-SA 4.0**。
- 本项目原创程序、样式与图形：**MIT**，见 [LICENSE](LICENSE)。
- 第三方课标、教材及其他来源保留各自授权条件；参考 [上游 PROVENANCE](https://github.com/withmarbleapp/os-taxonomy/blob/main/PROVENANCE.md) 与具体来源。

详见 [NOTICE.md](NOTICE.md)。生成的 HTML 同时包含代码与另行授权的数据、内容，不能将整个网页中的全部材料都视为 MIT 授权。上海部分仅提供简短摘要、编辑解释与来源链接，不提供整本教材。

**设计与维护：Lianghuan Bi(Hedy Bi)**
