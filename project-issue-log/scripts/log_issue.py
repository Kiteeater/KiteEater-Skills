#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


DEFAULT_LOG_PATH = Path("docs/project-issue-log.md")


@dataclass
class IssueEntry:
    title: str
    category: str
    status: str
    problem: str
    solution: str
    impact: str
    follow_up: str | None
    timestamp: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Append a structured issue entry to docs/project-issue-log.md."
    )
    parser.add_argument("--workspace", required=True, help="Workspace root path.")
    parser.add_argument("--title", required=True, help="Short issue title.")
    parser.add_argument("--category", required=True, help="Issue category.")
    parser.add_argument("--status", required=True, help="Current status.")
    parser.add_argument("--problem", required=True, help="Problem summary.")
    parser.add_argument("--solution", required=True, help="Fix or decision summary.")
    parser.add_argument("--impact", required=True, help="Why it matters.")
    parser.add_argument("--follow-up", dest="follow_up", help="Optional next step.")
    parser.add_argument(
        "--log-path",
        default=str(DEFAULT_LOG_PATH),
        help="Path relative to the workspace root. Default: docs/project-issue-log.md",
    )
    return parser.parse_args()


def ensure_log_file(log_path: Path) -> None:
    if log_path.exists():
        return

    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(
        "# Project Issue Log\n\n"
        "Persistent notes for notable project problems, decisions, and fixes.\n\n",
        encoding="utf-8",
    )


def build_entry(entry: IssueEntry) -> str:
    lines = [
        f"## {entry.timestamp} - {entry.title}",
        "",
        f"- Category: {entry.category}",
        f"- Status: {entry.status}",
        f"- Problem: {entry.problem}",
        f"- Solution: {entry.solution}",
        f"- Impact: {entry.impact}",
    ]
    if entry.follow_up:
        lines.append(f"- Follow-up: {entry.follow_up}")
    lines.append("")
    return "\n".join(lines)


def append_entry(log_path: Path, entry: IssueEntry) -> None:
    current = log_path.read_text(encoding="utf-8")
    separator = "" if current.endswith("\n\n") else ("\n" if current.endswith("\n") else "\n\n")
    log_path.write_text(current + separator + build_entry(entry), encoding="utf-8")


def main() -> int:
    args = parse_args()
    workspace = Path(args.workspace).expanduser().resolve()
    if not workspace.exists():
        raise SystemExit(f"Workspace does not exist: {workspace}")
    log_path = workspace / args.log_path

    ensure_log_file(log_path)

    entry = IssueEntry(
        title=args.title.strip(),
        category=args.category.strip(),
        status=args.status.strip(),
        problem=args.problem.strip(),
        solution=args.solution.strip(),
        impact=args.impact.strip(),
        follow_up=args.follow_up.strip() if args.follow_up else None,
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M"),
    )
    append_entry(log_path, entry)
    print(f"Appended entry to {log_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
