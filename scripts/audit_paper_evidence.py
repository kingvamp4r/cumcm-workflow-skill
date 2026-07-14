#!/usr/bin/env python3
"""Block CUMCM paper release when metadata, evidence, or paper text disagree."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


TEXT_SUFFIXES = {".md", ".tex", ".txt", ".bib"}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"无法读取 JSON：{path}: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", type=Path)
    parser.add_argument("--paper-dir", default="05_论文材料")
    args = parser.parse_args()
    root = args.project_root.expanduser().resolve()
    paper = root / args.paper_dir
    errors: list[str] = []
    metadata_path = paper / "论文元数据.json"
    claims_path = paper / "证据清单.json"
    if not metadata_path.is_file() or not claims_path.is_file():
        missing = [str(p) for p in (metadata_path, claims_path) if not p.is_file()]
        print("FAIL 缺少发布元数据：" + "; ".join(missing))
        return 2
    try:
        metadata, evidence = load_json(metadata_path), load_json(claims_path)
    except ValueError as exc:
        print(f"FAIL {exc}")
        return 2
    required_meta = {"paper_kind", "contest_year", "rules_year", "rules_source", "template_class", "model_version", "audit_scope"}
    for key in required_meta - metadata.keys():
        errors.append(f"元数据缺少 {key}")
    if metadata.get("template_class") not in {"template", "draft", "finished_paper"}:
        errors.append("template_class 必须是 template、draft 或 finished_paper")
    if metadata.get("paper_kind") == "submission":
        if metadata.get("contest_year") != metadata.get("rules_year"):
            errors.append("投稿版的 contest_year 与 rules_year 不一致")
        if metadata.get("audit_scope") != "full":
            errors.append("投稿版必须使用 full 审计")
    if not str(metadata.get("rules_source", "")).strip():
        errors.append("rules_source 不能为空")
    claims = evidence.get("claims")
    if not isinstance(claims, list) or not claims:
        errors.append("证据清单至少需要一条 claim")
        claims = []
    groups = ("paper_files", "model_files", "script_files", "run_records", "data_or_output_files")
    for claim in claims:
        name = claim.get("id", "未命名 claim")
        if claim.get("status") != "verified":
            errors.append(f"{name} 未标记为 verified")
        for group in groups:
            paths = claim.get(group)
            if not isinstance(paths, list) or not paths:
                errors.append(f"{name} 缺少 {group}")
                continue
            for relative in paths:
                if not (root / relative).exists():
                    errors.append(f"{name} 路径不存在：{relative}")
    text_parts: list[str] = []
    for path in paper.rglob("*"):
        if path.suffix.lower() in TEXT_SUFFIXES and path.is_file():
            text_parts.append(path.read_text(encoding="utf-8", errors="ignore"))
    paper_text = "\n".join(text_parts)
    for term in metadata.get("legacy_terms", []):
        if term and term in paper_text:
            errors.append(f"论文仍含废弃术语：{term}")
    for term in metadata.get("required_terms", []):
        if term and term not in paper_text:
            errors.append(f"论文缺少必需术语：{term}")
    for match in re.findall(r"(?:\\path|\\texttt)\{([^}]+)\}", paper_text):
        candidate = root / match
        if "/" in match and not candidate.exists():
            errors.append(f"论文附录引用路径不存在：{match}")
    if errors:
        print("FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"PASS {len(claims)} 条结论证据完整；论文类别：{metadata['paper_kind']}；模型：{metadata['model_version']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
