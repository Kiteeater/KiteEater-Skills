#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


DEFAULT_LOG_PATH = Path("docs/architecture-tradeoff-log.md")
DEFAULT_HEADER = (
    "# Architecture Tradeoff Log\n\n"
    "Persistent notes for structural issues, design trade-offs, rejected options, and final decisions.\n\n"
)


@dataclass
class TradeoffEntry:
    title: str
    status: str
    impact_scope: str
    discovery: str
    current_state: str
    chosen_solution: str
    tradeoffs: str
    rejected_options: list[str]
    final_outcome: str
    follow_up: str | None
    timestamp: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Append a structured architecture tradeoff entry to docs/architecture-tradeoff-log.md."
    )
    parser.add_argument("--workspace", required=True, help="Workspace root path.")
    parser.add_argument("--title", required=True, help="Short decision title.")
    parser.add_argument("--status", required=True, help="Current status: open, partial, resolved, or temporary.")
    parser.add_argument("--impact-scope", required=True, help="Affected modules, layers, or workflows.")
    parser.add_argument("--discovery", required=True, help="What was discovered and where it appeared.")
    parser.add_argument("--current-state", required=True, help="Current structure or constraint.")
    parser.add_argument("--chosen-solution", required=True, help="What was changed or decided.")
    parser.add_argument("--tradeoffs", required=True, help="Why this path won and what cost it introduced.")
    parser.add_argument(
        "--rejected-option",
        dest="rejected_options",
        action="append",
        required=True,
        help="A rejected option and why it lost. Pass more than once for multiple options.",
    )
    parser.add_argument("--final-outcome", required=True, help="Whether the issue is resolved and what remains true.")
    parser.add_argument("--follow-up", dest="follow_up", help="Optional follow-up or risk to watch.")
    parser.add_argument(
        "--log-path",
        default=str(DEFAULT_LOG_PATH),
        help="Path relative to the workspace root. Default: docs/architecture-tradeoff-log.md",
    )
    return parser.parse_args()


def ensure_log_file(log_path: Path) -> None:
    if log_path.exists():
        return

    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(DEFAULT_HEADER, encoding="utf-8")


def normalize(value: str) -> str:
    return value.strip()


def build_rejected_options(options: list[str]) -> list[str]:
    lines = ["### 5. Rejected Options"]
    for option in options:
        lines.append(f"- {option}")
    return lines


def build_entry(entry: TradeoffEntry) -> str:
    lines = [
        f"## [{entry.timestamp}] {entry.title}",
        "",
        f"- Status: {entry.status}",
        f"- Impact Scope: {entry.impact_scope}",
        "",
        "### 1. Discovery",
        entry.discovery,
        "",
        "### 2. Current State",
        entry.current_state,
        "",
        "### 3. Chosen Solution",
        entry.chosen_solution,
        "",
        "### 4. Trade-offs And Understanding",
        entry.tradeoffs,
        "",
        *build_rejected_options(entry.rejected_options),
        "",
        "### 6. Final Outcome",
        entry.final_outcome,
        "",
        "### 7. Follow-up",
        entry.follow_up or "None right now.",
        "",
    ]
    return "\n".join(lines)


def append_entry(log_path: Path, entry: TradeoffEntry) -> None:
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

    rejected_options = [normalize(option) for option in args.rejected_options if normalize(option)]
    if not rejected_options:
        raise SystemExit("At least one --rejected-option is required.")

    entry = TradeoffEntry(
        title=normalize(args.title),
        status=normalize(args.status),
        impact_scope=normalize(args.impact_scope),
        discovery=normalize(args.discovery),
        current_state=normalize(args.current_state),
        chosen_solution=normalize(args.chosen_solution),
        tradeoffs=normalize(args.tradeoffs),
        rejected_options=rejected_options,
        final_outcome=normalize(args.final_outcome),
        follow_up=normalize(args.follow_up) if args.follow_up else None,
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M"),
    )
    append_entry(log_path, entry)
    print(f"Appended entry to {log_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
