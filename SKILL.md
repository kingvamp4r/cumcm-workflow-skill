---
name: cumcm-workflow
description: "Run a rigorous end-to-end workflow for CUMCM and Chinese mathematical-modeling contests: verify a supplied problem and attachments, organize a team project, clarify requirements, assess existing ideas, compare and implement models, validate data and results, and assemble evidence-backed Markdown or user-provided LaTeX/Word paper materials. Use when users ask to analyze a CUMCM problem, set up a modeling-contest project, develop or review models, process contest data, validate results, or prepare contest paper materials."
---

# CUMCM 全流程工作流

Use this skill as an evidence-first project workflow. Do not treat it as permission to invent data, results, sources, experiments, or paper content.

## Non-negotiable entry gate

Before analyzing, modeling, coding, or writing result-bearing paper content, confirm all of the following:

1. A complete problem statement is present and readable.
2. Every attachment named by the statement is present and readable, or the user explicitly confirms that the problem has no attachments.
3. The working project directory is identified.
4. Contest, paper-format, and school rules supplied by the user have been collected. If none are supplied, obtain and use the official CUMCM rules for the problem's contest year before applying any default requirement.

User-supplied rules override the generic workflow. Bind the paper to the contest year stated by the problem. For a historical problem, collect that year's rules; current rules may be used only as a clearly labeled practice reference. If year-matched rules cannot be accessed, state that limitation and label all outputs `练习稿` or `复核稿`; do not claim format or submission compliance, fabricate a year-specific header, or call the file a submission version. Treat a damaged, encrypted, screenshot-only, unreadable, or materially incomplete attachment as missing: do not infer its contents, and request a readable original, access method, password, or field definition. If any other condition is missing, stop the substantive workflow. Ask one precise question at a time until the gap is resolved. It is acceptable only to create the project skeleton and a `待补材料.md` list before the gate passes.

## Set up the project

Create or preserve this structure. Use [scripts/init_cumcm_project.py](scripts/init_cumcm_project.py) when creating a new project.

```text
项目名/
├── 00_题目与计划/
├── 01_数据/
│   ├── 原始数据/
│   ├── 清洗后数据/
│   └── 外部数据说明/
├── 02_模型/
├── 03_代码/
├── 04_结果与图表/
└── 05_论文材料/
```

Maintain these coordination files in `00_题目与计划/`:

- `任务看板.md`: task, owner, status, dependency, deliverable path, and open question.
- `变更记录.md`: lightweight version ID, timestamp, author, change, affected files, evidence, and rollback point.
- `待补材料.md`: missing statement/attachment/template/definition items.

Treat these files as the source of truth. When chat-based teamwork makes the board impractical, generate a short progress message that can be pasted into WeChat or QQ and cite the relevant file paths. Generate such a message at a completed subproblem, key risk, user-decision request, or planned handoff, not for every file edit.

Before writing paper content, add `05_论文材料/论文元数据.json` and `05_论文材料/证据清单.json` from [references/paper-release-gate.md](references/paper-release-gate.md). Keep their model version, rule year, template classification, script paths, run records, and output paths synchronized with the task board, change log, and `LOG.md`. A stale status file blocks handoff.

Use a two-day time budget unless the user supplies another deadline. Adjust the breadth of candidate models, optimization depth, and validation sequence to that budget, but never relax the entry gate, provenance checks, or ban on fabricated evidence. Create a dated work schedule only when the user requests one or supplies a schedule to follow.

Once the entry gate passes, write `00_题目与计划/题目理解简报.md` before proposing models. Include a faithful problem summary, attachment inventory, each subproblem's input/output/constraint, known definitions and units, ambiguity list, and questions still needing confirmation.

## Clarify before deciding

Ask one question at a time until the important ambiguities are fully or mostly resolved. Prioritize: each subproblem's required output, data field meaning and unit, time and spatial scope, objective and constraints, scoring or evaluation rules, external-data permission, and the user's current role/time limit.

Do not silently make a core assumption. If the user explicitly chooses to proceed with an unresolved point, record the assumption and its expected effect in `02_模型/`.

## Select tools and inspect existing work

Before choosing a language, inspect the project for existing code, dependency files, data formats, and runnable toolchains. Prefer an already working stack. If several environments are available, choose the language that fits the task and briefly state why; typical defaults are Python for general data work/numerical optimization, R for statistical modeling, and MATLAB for an existing MATLAB project or toolbox-specific computation.

Do not install packages, alter environments, download datasets, or bulk-fetch external resources without the user's explicit approval. Offer a no-install alternative first.

Do not rely on generic canned implementation templates as evidence. Write task-specific code from the confirmed problem and data; add reusable code templates to the skill only after they have been repeatedly used and validated in real projects.

You may propose and search public academic papers, textbooks, official technical material, and method documentation to support model selection. Obtain approval before downloading, bulk-acquiring, formally citing, or incorporating the material into paper content. Cite only sources actually read, directly relevant to the current problem, and independently verifiable.

## Data and source integrity

For every external dataset actually used, store the original file under `01_数据/原始数据/` and create a record under `01_数据/外部数据说明/` with source URL or publisher, access date, license/use restriction, field definitions, coverage, and validation notes.

Before using any data or result, check authenticity, relevance, completeness, unit consistency, duplicates, missingness, outliers, and whether the processing can be reproduced. Save cleaned data and scripts separately, and create `01_数据/清洗后数据/数据清洗说明.md` documenting raw-data issues, transformation rules, affected-row counts, field conversions, output CSV paths, scripts, and likely impact. Never backfill data to support a prewritten narrative.

If the available data cannot reliably answer a target or support its validation, explain the exact gap and impact before modeling further. Let the user choose among approved external data, a narrower question, or a verifiable proxy metric; record the choice and do not conceal the limitation with unsupported assumptions.

## Assess existing ideas, then model

Before proposing candidate models, read [references/method-library.md](references/method-library.md) and load only the section matching the current subproblem. Use it to form alternatives; do not treat it as a substitute for checking the statement, data, or current constraints.

If the user supplies a modeling idea, first write a concise review in `02_模型/`:

- Identify the target, assumptions, variables, constraints, and causal/logical chain.
- Flag a **major defect** if it makes the model answer a different question, violates a stated constraint, uses unavailable/unidentifiable inputs, confuses correlation with causation, creates circular reasoning/data leakage, or makes validation impossible.
- If a major defect exists, explain the evidence and ask whether to rebuild before implementing.
- Otherwise, retain the main idea and propose precise improvements.

The user retains the final decision after receiving a major-defect warning. If the user elects to proceed, record the defect, likely impact, and unverified risk in the model documentation and handoff; do not represent the resulting claim as validated.

Classify each subproblem as prediction/evaluation, optimization/decision, mechanism analysis, data mining/classification, or a mixture. For every key subproblem, propose at least two feasible modeling routes with assumptions, strengths, limits, required data, validation plan, and a short description of the main idea. Prefer the simplest route that matches the problem, remains interpretable, can be validated, and fits the budget; present added complexity only when it has a clear benefit. Recommend a route, but leave the final choice to the user. Do not begin high-cost implementation until the user chooses, unless the user explicitly authorizes advancing under time pressure. Retain a baseline or alternative for key-result validation.

Write problem decomposition, assumptions, notation, candidate-model comparison, derivation, and limitations as Markdown in `02_模型/`. Use Chinese by default and add English terms only where they aid search or implementation.

Use these core files in `02_模型/`: `问题分析.md`, `模型假设.md`, `符号说明.md`, `候选模型比较.md`, `主模型与求解.md`, and `验证与局限.md`. In `候选模型比较.md`, record the selected route, selection rationale, and rejected routes with their reasons. Keep the evidence and reasoning for each claim in the relevant file.

For Markdown mathematical writing, use `\(...\)` for inline expressions and `\[...\]` for display expressions. Do not use dollar-sign delimiters, place formulas inside code spans/tables, or force a long derivation inline. Use standard LaTeX commands for fractions, derivatives, functions, Greek letters, vectors, matrices, and multi-line derivations.

## Implement and validate

Put reproducible programs in `03_代码/`, clean datasets in `01_数据/清洗后数据/`, and only verified tables/figures in `04_结果与图表/`. Every figure or table entering paper material must have a saved generating script, cleaned-data source table in CSV when applicable, input path, parameters/random seed where applicable, output path, and interpretation. Do not use manually altered graphics as computed results.

For every runnable analysis or model program, provide a minimal run note with the entry point, input paths, dependency/toolbox requirements, command or execution steps, parameters/seed, and expected output paths.

Execute a program at least once before calling it runnable or using its output in a conclusion, and record the run status. If execution is blocked by missing data, environment, permission, or another limitation, deliver it only as an unrun implementation draft and do not treat it as evidence.

When code errors, results are anomalous, or output cannot be reproduced, preserve the reproduction conditions, error/output, diagnosis, and repair in `03_代码/` or the change log. Do not silently overwrite the prior version; mark any result produced before the repair as unusable until rerun and revalidated.

Before calling a result usable, check the appropriate subset of: train/test separation or leakage, constraint feasibility, units/dimensions, edge cases, numerical convergence, random-seed stability, sensitivity/robustness, baseline comparison, and consistency with the problem statement. Clearly label unverified or exploratory output; do not put it in conclusions.

Follow any precision and submission-format requirements in the problem or official rules. Otherwise choose reported precision from input accuracy and stability/sensitivity checks; do not report spurious digits that imply more certainty than the evidence supports.

For heuristic, stochastic, or approximate optimization, record the algorithm, stopping condition, search budget, seed(s), and feasibility check. Unless global optimality is actually established, describe the output as a feasible candidate or approximate solution, not an optimum.

## Prepare paper materials honestly

Create a paper outline and placeholders early, but write no quantitative conclusion, result table, figure claim, or citation-dependent statement until its source data, script, and validation are available. Classify every user-provided Word or LaTeX file before reuse as `template`, `draft`, or `finished_paper`; record the basis in `论文元数据.json`. A finished paper is evidence to inspect, not a template to copy wholesale. Reuse a finished paper's layout only after user approval, and rebuild its abstract, model, results, conclusion, appendices, citations, and identity fields from current evidence. Use a user-provided template after inspecting it; preserve its required structure and styles. Do not make structural or general style changes without approval, except that you may resize, reposition, or adjust float behavior of images to eliminate large blank areas caused by image layout.

If no user template exists, use `assets/latex-paper-skeleton/` only as a generic Chinese modeling-paper fallback. It is not an official CUMCM format. The skeleton contains no province-specific contest identity and no copied contest result.

Build paper material in `05_论文材料/` from verified assets only. Cite sources, distinguish results from limitations, and never copy long passages, fabricate citations, or describe unrun experiments as completed. Do not reuse a result, table, figure, appendix path, or script list from an older model version. If the model changes, rerun the compatible implementation or label the item as a baseline; regenerate every affected paper statement.

When a user-provided LaTeX or Word template and a compatible toolchain are available, produce a PDF and inspect compilation errors or rendered layout before handoff. If either is unavailable, deliver editable source files and state why a final layout check was not possible.

Keep explanatory visuals distinct from computed figures. For a scenario schematic or other illustrative image, provide a precise image-generation prompt for the user unless the user supplies/requests an asset. For a process flowchart, create a Draw.io source file when the user asks for one and the environment supports it; otherwise provide a precise prompt or flow specification for the user. Never present an explanatory visual as measured or computed evidence.

Before producing any PDF, run [scripts/audit_paper_evidence.py](scripts/audit_paper_evidence.py) against `论文元数据.json` and `证据清单.json`. Treat an audit failure as a release blocker. The audit must cover every key statement in the abstract, conclusion, figure/table caption, and body: trace each to a model derivation, reproducible output, or credible source; verify template classification, contest/rules-year compatibility, actual run records, file paths in appendices, and forbidden legacy terminology. If time is tight, reduce scope only to abstract, conclusion, and every quantitative claim; record the reduced scope and remaining risk in metadata, and label the output `草稿`, never `最终版` or `投稿版`.

## Completion check

Before declaring a subproblem complete, report: the result file paths, source/data provenance, model version, program used, validation performed, limitations, and any remaining unresolved question. Update the task board and change log.

Maintain a root-level `LOG.md` as the chronological project record. Append major clarifications, user decisions, data acquisition/cleaning, model choices, program runs/failures, validation, important file changes, risks, and handoffs with timestamps and paths.

Before submission, create a checklist under `00_题目与计划/`. Check mandatory items first: required problem number and filename, every required attachment/result table, readable final PDF, applicable template/format rules, required output coverage, synchronized coordination records, and traceable evidence for every key conclusion. Treat comprehensive sensitivity analysis and deep layout polishing as time-permitting items; a full claim--evidence audit is mandatory. Report explicitly if any nonmandatory item is skipped.
