#!/usr/bin/env python3
"""
check_readme_links.py
Validates all relative links in README.md, PROBLEM_INDEX.md, and docs/*.md
to guarantee zero broken internal references.
"""

import os
import re
import sys
import urllib.parse

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def check_file_links(file_path):
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Match standard markdown links: [label](url)
    # Ignore images ![alt](url) or external http(s) / mailto links
    link_pattern = re.compile(r'(?<!\!)\[([^\]]+)\]\(([^)]+)\)')
    file_dir = os.path.dirname(file_path)

    broken_links = []
    total_links = 0

    for match in link_pattern.finditer(content):
        label = match.group(1)
        raw_target = match.group(2).strip()

        # Skip web links, anchors only, or mailto
        if raw_target.startswith(("http://", "https://", "mailto:", "#")):
            continue

        total_links += 1
        # Split target into path and optional anchor
        target_path_part = raw_target.split("#")[0]
        target_path_part = urllib.parse.unquote(target_path_part)

        if not target_path_part:
            continue

        resolved_path = os.path.normpath(os.path.join(file_dir, target_path_part))

        if not os.path.exists(resolved_path):
            broken_links.append({
                "source_file": os.path.relpath(file_path, REPO_ROOT),
                "link_label": label,
                "target": raw_target,
                "resolved_path": os.path.relpath(resolved_path, REPO_ROOT)
            })

    return total_links, broken_links

def run_link_check():
    print("=" * 60)
    print("         INTERNAL MARKDOWN LINK INTEGRITY AUDIT")
    print("=" * 60)

    target_files = [
        os.path.join(REPO_ROOT, "README.md"),
        os.path.join(REPO_ROOT, "PROBLEM_INDEX.md"),
    ]

    docs_dir = os.path.join(REPO_ROOT, "docs")
    if os.path.isdir(docs_dir):
        for fname in os.listdir(docs_dir):
            if fname.endswith(".md"):
                target_files.append(os.path.join(docs_dir, fname))

    overall_total = 0
    all_broken = []

    for tf in target_files:
        if not os.path.exists(tf):
            continue
        rel_tf = os.path.relpath(tf, REPO_ROOT)
        count, broken = check_file_links(tf)
        overall_total += count
        all_broken.extend(broken)
        status = f"[OK] ({count} links verified)" if not broken else f"[FAIL] ({len(broken)} broken)"
        print(f"{rel_tf:35s}: {status}")

    print("-" * 60)
    print(f"Total internal links verified: {overall_total}")
    print(f"Total broken links: {len(all_broken)}")

    if all_broken:
        print("\nBroken links details:")
        for b in all_broken:
            print(f"  Source: {b['source_file']}")
            print(f"    Label:  '{b['link_label']}'")
            print(f"    Target: '{b['target']}' (Looked at: {b['resolved_path']})")
        print("=" * 60)
        return False

    print("=" * 60)
    return True

if __name__ == "__main__":
    success = run_link_check()
    sys.exit(0 if success else 1)

