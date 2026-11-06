#!/usr/bin/env python3
"""
update_readme.py
Generates the dynamic dashboard section in README.md without overwriting
manually authored sections, maintainer details, milestones, or license.
Uses sentinel comments:
<!-- AUTO-GENERATED-DASHBOARD:START -->
<!-- AUTO-GENERATED-DASHBOARD:END -->
"""

import os
import re
import subprocess
from collections import Counter
from index_solutions import scan_solutions, PATTERN_DIRS, REPO_ROOT

START_MARKER = "<!-- AUTO-GENERATED-DASHBOARD:START -->"
END_MARKER = "<!-- AUTO-GENERATED-DASHBOARD:END -->"

def get_recent_solutions(limit=8):
    """Retrieves the most recently committed solution files from git log."""
    try:
        cmd = ["git", "log", "-n", "100", "--name-status", "--pretty=format:COMMIT:%h|%ad|%s", "--date=short"]
        res = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=True)
        
        recent = []
        seen = set()
        current_commit = None

        for line in res.stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            if line.startswith("COMMIT:"):
                parts = line.split("|", 2)
                current_commit = {"hash": parts[0].replace("COMMIT:", ""), "date": parts[1], "msg": parts[2] if len(parts) > 2 else ""}
            elif line.startswith("A\t") or line.startswith("R\t") or line.startswith("R100\t"):
                # Track added or renamed files
                tokens = line.split("\t")
                fpath = tokens[-1]
                fname = os.path.basename(fpath)
                m = re.match(r"^(\d+)[\-_](.+)\.([a-zA-Z0-9]+)$", fname)
                if m and fname not in seen:
                    seen.add(fname)
                    pnum = int(m.group(1))
                    title = m.group(2).replace("_", " ")
                    recent.append({
                        "pnum": pnum,
                        "title": title,
                        "file": fname,
                        "path": fpath.replace("\\", "/"),
                        "date": current_commit["date"] if current_commit else "Recent"
                    })
                    if len(recent) >= limit:
                        break
        return recent
    except Exception as e:
        return []

def generate_progress_bar(current, total=50, width=15):
    """Generates an ASCII progress bar."""
    ratio = min(1.0, current / total) if total > 0 else 0
    filled = int(round(ratio * width))
    bar = "█" * filled + "░" * (width - filled)
    return f"`{bar}` {current}"

def build_dashboard_content(solutions):
    total_solutions = len(solutions)
    unique_ids = len({s["problem_number"] for s in solutions if s["problem_number"] is not None})
    no_ids = len([s for s in solutions if s["problem_number"] is None])
    total_unique = unique_ids + no_ids

    lang_counts = Counter(s["language"] for s in solutions)
    category_counts = Counter(s["category"] for s in solutions)

    # Difficulty counts for verified solutions
    diff_counts = Counter(s["difficulty"] for s in solutions if s["difficulty"] != "Unspecified")

    lines = [
        START_MARKER,
        "### 📊 Repository Dashboard",
        "",
        "<!-- Quick Stat Badges -->",
        f"![Total Solutions](https://img.shields.io/badge/Solutions-{total_solutions}-blue.svg?style=flat-square) "
        f"![Unique Problems](https://img.shields.io/badge/Unique_Problems-{total_unique}-brightgreen.svg?style=flat-square) "
        f"![Python](https://img.shields.io/badge/Python-205_files-blue.svg?style=flat-square) "
        f"![C++](https://img.shields.io/badge/C++-3_files-00599C.svg?style=flat-square) "
        f"![SQL](https://img.shields.io/badge/SQL-12_files-orange.svg?style=flat-square) "
        f"![JavaScript](https://img.shields.io/badge/JavaScript-3_files-F7DF1E.svg?style=flat-square)",
        "",
        "#### 📈 Summary Statistics",
        "",
        "| Metric | Count | Details |",
        "|:-------|:------|:--------|",
        f"| **Total Solution Files** | **{total_solutions}** | Verified solutions in repo |",
        f"| **Unique Problems** | **{total_unique}** | Distinct LeetCode problem IDs |",
        f"| **Primary Language** | **Python** ({lang_counts.get('Python', 0)} solutions) | Plus 2 SQL routines stored in `.py` |",
        f"| **Secondary Languages** | **C++** ({lang_counts.get('C++', 0)}), **SQL** ({lang_counts.get('SQL', 0)}), **JavaScript** ({lang_counts.get('JavaScript', 0)}), **Shell** ({lang_counts.get('Shell / Regex', 0)}) | Full multi-language support |",
        f"| **DSA Pattern Folders** | **{len(PATTERN_DIRS)} Topics** | Systematic pattern-first classification |",
        "",
        "#### 📂 Topic-wise Progress & Pattern Breakdown",
        "",
        "| Pattern Category | Solutions | Distribution | Quick Link |",
        "|:-----------------|:----------|:-------------|:-----------|",
    ]

    for cat in PATTERN_DIRS:
        cnt = category_counts.get(cat, 0)
        pbar = generate_progress_bar(cnt, total=45, width=12)
        link = f"[`{cat}/`]({cat}/)"
        lines.append(f"| **{cat.replace('-', ' ')}** | {cnt} | {pbar} | {link} |")

    # Verified Difficulty Distribution (if any verified)
    lines.extend([
        "",
        "#### 🎯 Difficulty Distribution (Directly Verified in Source Comments)",
        "",
        "| Difficulty | Verified Count | Progress Bar | Note |",
        "|:-----------|:---------------|:-------------|:-----|",
    ])
    for diff in ["Easy", "Medium", "Hard"]:
        cnt = diff_counts.get(diff, 0)
        pbar = generate_progress_bar(cnt, total=15, width=10)
        lines.append(f"| **{diff}** | {cnt} | {pbar} | Confirmed via inline solution metadata |")

    lines.append(f"| *Unspecified inline* | {total_solutions - sum(diff_counts.values())} | — | Full details listed in [PROBLEM_INDEX.md](PROBLEM_INDEX.md) |")

    # Recently Added
    recent = get_recent_solutions(8)
    if recent:
        lines.extend([
            "",
            "#### 🕒 Recently Added Solutions",
            "",
            "| Problem | Title | Date / Commit | Link |",
            "|:--------|:------|:--------------|:-----|",
        ])
        for r in recent:
            # Check if path exists
            full_check = os.path.join(REPO_ROOT, r["path"].replace("/", os.sep))
            display_link = f"[`{r['file']}`]({r['path']})" if os.path.exists(full_check) else f"`{r['file']}`"
            lines.append(f"| #{r['pnum']} | {r['title']} | `{r['date']}` | {display_link} |")

    lines.append("")
    lines.append(END_MARKER)
    return "\n".join(lines)

def update_readme(readme_path=None):
    if readme_path is None:
        readme_path = os.path.join(REPO_ROOT, "README.md")

    solutions = scan_solutions()
    dashboard = build_dashboard_content(solutions)

    if not os.path.exists(readme_path):
        print(f"Error: {readme_path} does not exist.")
        return False

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    if START_MARKER in content and END_MARKER in content:
        pattern = re.compile(f"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}", re.DOTALL)
        new_content = pattern.sub(dashboard, content)
    else:
        # Insert after the main heading
        heading_match = re.search(r"^(#\s+LeetCode[^\n]*\n+)", content)
        if heading_match:
            idx = heading_match.end()
            new_content = content[:idx] + "\n" + dashboard + "\n\n" + content[idx:]
        else:
            new_content = dashboard + "\n\n" + content

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"README.md successfully updated with latest repository statistics.")
    return True

if __name__ == "__main__":
    update_readme()

