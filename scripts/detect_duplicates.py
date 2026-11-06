#!/usr/bin/env python3
"""
detect_duplicates.py
Scans the repository to identify duplicate problem IDs, duplicate filenames,
and multiple solution implementations.
"""

import os
import re
import sys
from collections import defaultdict
from index_solutions import scan_solutions, REPO_ROOT

def analyze_duplicates(solutions):
    pnum_map = defaultdict(list)
    filename_map = defaultdict(list)

    for s in solutions:
        pnum = s["problem_number"]
        fname = s["filename"]
        if pnum is not None:
            pnum_map[pnum].append(s)
        filename_map[fname].append(s)

    multiple_solutions = {k: v for k, v in pnum_map.items() if len(v) > 1}
    duplicate_filenames = {k: v for k, v in filename_map.items() if len(v) > 1}

    return multiple_solutions, duplicate_filenames

def run_duplicate_report(verbose=True):
    solutions = scan_solutions()
    multi_sols, dup_names = analyze_duplicates(solutions)

    print("=" * 60)
    print("        DUPLICATE & MULTI-SOLUTION REPORT")
    print("=" * 60)
    print(f"Total solution files scanned: {len(solutions)}")
    print(f"Problems with multiple solutions: {len(multi_sols)}")
    print(f"Duplicate identical filenames across folders: {len(dup_names)}")
    print("-" * 60)

    if multi_sols:
        print("\n[+] Problems with Multiple Solutions / Languages:")
        for pnum in sorted(multi_sols.keys()):
            sols = multi_sols[pnum]
            print(f"  Problem #{pnum}:")
            for s in sols:
                print(f"    - [{s['category']}] {s['filename']} ({s['language']})")
    else:
        print("\nNo problem numbers have multiple solutions.")

    if dup_names:
        print("\n[!] WARNING: Identical filenames located in multiple directories:")
        for fname, sols in dup_names.items():
            print(f"  File: {fname}")
            for s in sols:
                print(f"    - {s['rel_path']}")
    else:
        print("\n[OK] Zero filename collisions across directories.")

    print("=" * 60)
    return len(dup_names) == 0

if __name__ == "__main__":
    success = run_duplicate_report()
    sys.exit(0 if success else 1)

