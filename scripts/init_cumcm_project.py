#!/usr/bin/env python3
"""Create the standard CUMCM project tree and collaboration records."""

from __future__ import annotations

import argparse
from pathlib import Path


DIRECTORIES = (
    "00_题目与计划",
    "01_数据/原始数据",
    "01_数据/清洗后数据",
    "01_数据/外部数据说明",
    "02_模型",
    "03_代码",
    "04_结果与图表",
    "05_论文材料",
)

FILES = {
    "05_论文材料/论文元数据.json": """{
  "paper_kind": "practice_draft",
  "contest_year": null,
  "rules_year": null,
  "rules_source": "",
  "template_class": "draft",
  "template_path": "",
  "model_version": "",
  "audit_scope": "full",
  "legacy_terms": [],
  "required_terms": []
}
""",
    "05_论文材料/证据清单.json": """{
  "claims": []
}
""",
    "LOG.md": """# 项目时间线\n\n| 时间 | 事项 | 决策/结果 | 相关文件或证据 | 风险与待办 |\n| --- | --- | --- | --- | --- |\n""",
    "00_题目与计划/任务看板.md": """# 任务看板\n\n| 子任务 | 负责人 | 状态 | 依赖项 | 产物路径 | 待澄清问题 |\n| --- | --- | --- | --- | --- | --- |\n""",
    "00_题目与计划/变更记录.md": """# 变更记录\n\n| 版本 | 时间 | 作者 | 变更摘要 | 受影响文件 | 证据/验证 | 回退点 |\n| --- | --- | --- | --- | --- | --- | --- |\n""",
    "00_题目与计划/题目理解简报.md": """# 题目理解简报\n\n## 忠实概述\n\n【在题目与附件核验后填写】\n\n## 附件清单\n\n| 文件 | 用途 | 可读性 | 备注 |\n| --- | --- | --- | --- |\n\n## 子问题拆解\n\n| 子问题 | 输入 | 目标输出 | 约束 | 待澄清项 |\n| --- | --- | --- | --- | --- |\n\n## 已知定义与单位\n\n【填写题目明确给出的定义、口径与单位】\n\n## 待确认问题\n\n- [ ] 【问题】\n""",
    "00_题目与计划/待补材料.md": """# 待补材料\n\n- [ ] 完整题目文本或题目文件\n- [ ] 题目声明的全部附件，或“本题无附件”的确认\n- [ ] 当届竞赛规则、论文格式要求和学校要求；若未提供，需核验当届 CUMCM 官方规则\n- [ ] 题目中模糊的字段、单位、目标或约束说明\n- [ ] 用户提供的论文模板（如有）\n""",
    "01_数据/外部数据说明/README.md": """# 外部数据登记\n\n每份外部数据记录：来源链接或发布机构、获取日期、许可/使用限制、字段说明、时间与地域覆盖、真实性/有效性检查、清洗脚本路径。\n""",
    "01_数据/清洗后数据/数据清洗说明.md": """# 数据清洗说明\n\n## 原始数据问题\n\n【缺失、重复、异常、单位或格式问题】\n\n## 处理规则\n\n【规则及依据】\n\n## 影响记录\n\n| 处理 | 受影响记录数 | 字段转换 | 影响说明 |\n| --- | --- | --- | --- |\n\n## 可复现信息\n\n- 清洗脚本：\n- 原始数据路径：\n- 输出 CSV 路径：\n""",
    "02_模型/问题分析.md": "# 问题分析\n\n【通过题目与附件核验后填写】\n",
    "02_模型/模型假设.md": "# 模型假设\n\n【每项假设需写明依据和潜在影响】\n",
    "02_模型/符号说明.md": "# 符号说明\n\n| 符号 | 含义 | 单位 |\n| --- | --- | --- |\n",
    "02_模型/候选模型比较.md": "# 候选模型比较\n\n| 方案 | 主思路 | 优点 | 局限 | 所需数据 | 验证方式 |\n| --- | --- | --- | --- | --- | --- |\n",
    "02_模型/主模型与求解.md": "# 主模型与求解\n\n【在用户确认模型选择后填写】\n",
    "02_模型/验证与局限.md": "# 验证与局限\n\n【记录基准比较、敏感性、稳健性和已知限制】\n",
    "03_代码/运行说明.md": """# 运行说明\n\n| 程序 | 入口 | 输入 | 依赖/工具箱 | 运行方式 | 参数或随机种子 | 输出 |\n| --- | --- | --- | --- | --- | --- |\n""",
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", type=Path, help="new or existing project directory")
    parser.add_argument("--force", action="store_true", help="overwrite standard record files")
    args = parser.parse_args()

    root = args.project_dir.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    for relative in DIRECTORIES:
        (root / relative).mkdir(parents=True, exist_ok=True)
    for relative, content in FILES.items():
        target = root / relative
        if args.force or not target.exists():
            target.write_text(content, encoding="utf-8")
    print(root)


if __name__ == "__main__":
    main()
