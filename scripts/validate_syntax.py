#!/usr/bin/env python3
"""
validate_syntax.py
Validates Python syntax across all repository .py solution files without executing them.
Reports syntax errors, malformed tokens, and special cases (e.g. SQL statements inside .py files).
"""

import os
import ast
import sys
from index_solutions import scan_solutions, REPO_ROOT

# Known non-python contents or intentional syntax quirks preserved for repository fidelity
KNOWN_EXCEPTIONS = {
    "Database/176_2ndHighestSalary.py": "SQL query stored in .py file",
    "Database/177_nth_highest_salary.py": "SQL CREATE FUNCTION stored in .py file",
}

def validate_all_python_files(solutions=None):
    if solutions is None:
        solutions = scan_solutions()

    py_solutions = [s for s in solutions if s["extension"] == ".py"]
    print("=" * 60)
    print("          PYTHON SYNTAX VALIDATION AUDIT")
    print("=" * 60)
    print(f"Total Python files found: {len(py_solutions)}")
    
    valid_count = 0
    errors = []
    known_errors = []

    for s in py_solutions:
        rel_path = s["rel_path"]
        fpath = s["full_path"]

        try:
            with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
            ast.parse(content, filename=s["filename"])
            valid_count += 1
        except SyntaxError as se:
            if rel_path in KNOWN_EXCEPTIONS:
                known_errors.append({
                    "rel_path": rel_path,
                    "line": se.lineno,
                    "msg": se.msg,
                    "reason": KNOWN_EXCEPTIONS[rel_path]
                })
            else:
                errors.append({
                    "rel_path": rel_path,
                    "line": se.lineno,
                    "msg": se.msg,
                    "text": se.text.strip() if se.text else ""
                })

    print(f"Valid Python files passing ast.parse: {valid_count}")
    print(f"Known format exceptions (e.g., SQL in .py): {len(known_errors)}")
    print(f"Preserved original files with syntax issues: {len(errors)}")
    print("-" * 60)

    if known_errors:
        print("\n[i] Known format exceptions:")
        for ke in known_errors:
            print(f"  - {ke['rel_path']} (Line {ke['line']}): {ke['reason']}")

    if errors:
        print("\n[!] Original user solution syntax notes (preserved as-is per safety rules):")
        for err in errors:
            print(f"  - {err['rel_path']}: Line {err['line']} -> {err['msg']}")
            if err["text"]:
                print(f"      Code: {err['text']}")

    print("=" * 60)
    # Return true if script ran and accurately classified files
    return True

if __name__ == "__main__":
    validate_all_python_files()

