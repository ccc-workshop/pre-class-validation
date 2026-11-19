"""Simple house rules for SQL files. Runs locally and in GitHub Actions.

Rules:
  1. The first line is a comment that starts with "-- Purpose:".
  2. No "SELECT *" - list the columns you need.
  3. The file ends with a semicolon.
"""
import pathlib
import re
import sys

problems = []
for path in sorted(pathlib.Path("sql").rglob("*.sql")):
    text = path.read_text(encoding="utf-8").strip()
    lines = text.splitlines()
    if not lines or not lines[0].startswith("-- Purpose:"):
        problems.append(f"{path}: first line must be a '-- Purpose:' comment")
    if re.search(r"select\s+\*", text, re.IGNORECASE):
        problems.append(f"{path}: avoid SELECT * - list the columns")
    if not text.endswith(";"):
        problems.append(f"{path}: must end with a semicolon")

if problems:
    print("SQL check FAILED:")
    for p in problems:
        print("  - " + p)
    sys.exit(1)
print("SQL check passed")
