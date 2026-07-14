# 论文发布门槛

在 `05_论文材料/` 创建以下两个 JSON 文件；路径均相对项目根目录。

`论文元数据.json`：

```json
{
  "paper_kind": "practice_draft",
  "contest_year": 2025,
  "rules_year": 2025,
  "rules_source": "官方链接或用户提供文件",
  "template_class": "template",
  "template_path": "",
  "model_version": "v1",
  "audit_scope": "full",
  "legacy_terms": [],
  "required_terms": []
}
```

`证据清单.json`：

```json
{
  "claims": [
    {
      "id": "C-01",
      "claim": "可复核的定量或定性结论",
      "paper_files": ["05_论文材料/mainbody/abstract.tex"],
      "model_files": ["02_模型/主模型与求解.md"],
      "script_files": ["03_代码/solver.py"],
      "run_records": ["03_代码/运行说明.md"],
      "data_or_output_files": ["04_结果与图表/result.json"],
      "status": "verified"
    }
  ]
}
```

Rules:

- `paper_kind` is `submission` only with year-matched rules and a full audit; otherwise use `practice_draft` or `review_draft`.
- `template_class` is exactly `template`, `draft`, or `finished_paper`.
- Every `verified` claim requires at least one existing paper, model, script, run-record, and output/data path.
- Put terms from an abandoned model in `legacy_terms`; put the chosen model's indispensable terms in `required_terms`.
- Keep paths in appendices and source files valid relative to project root. If a source lists a retired script or output, update it before auditing.
