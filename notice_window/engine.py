"""Find notice windows in a contract. Phrase rules only. Not legal advice."""
from __future__ import annotations

import re
from dataclasses import dataclass

PAREN_RE = re.compile(
    r"\((?P<days>\d{1,3})\)\s*(?P<kind>calendar|business)?\s*days?'?(?:\s+prior)?(?:\s+written)?\s+notice",
    re.IGNORECASE,
)
PLAIN_RE = re.compile(
    r"(?<!\()\b(?P<days>\d{1,3})\s*(?P<kind>calendar|business)?\s*days?'?(?:\s+prior)?(?:\s+written)?\s+notice",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Notice:
    days: int
    kind: str
    text: str


def find_notices(text: str) -> list[Notice]:
    found: list[tuple[int, Notice]] = []
    occupied: list[tuple[int, int]] = []
    for pattern in (PAREN_RE, PLAIN_RE):
        for match in pattern.finditer(text):
            span = (match.start(), match.end())
            if any(not (span[1] <= start or span[0] >= end) for start, end in occupied):
                continue
            occupied.append(span)
            kind = (match.group("kind") or "days").lower()
            found.append((span[0], Notice(int(match.group("days")), kind, match.group(0))))
    found.sort(key=lambda item: item[0])
    return [item[1] for item in found]


def render(notices: list[Notice], source: str) -> str:
    lines = [
        f"# Notice windows — {source}",
        "",
        "Matched phrases only. This does not say whether the window is enforceable.",
        "",
        "| Days | Kind | Phrase |",
        "| --- | --- | --- |",
    ]
    if not notices:
        lines.append("| — | — | none |")
    for notice in notices:
        lines.append(f"| {notice.days} | {notice.kind} | {notice.text} |")
    lines.append("")
    return "\n".join(lines)
