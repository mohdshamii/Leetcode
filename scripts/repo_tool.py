#!/usr/bin/env python3
"""
repo_tool.py
Unified Developer CLI for LeetCode Repository Management.
Commands:
  index            - Generate/refresh PROBLEM_INDEX.md
  duplicates       - Scan for duplicate problem IDs and collision risks
  validate         - Static Python syntax audit across all solution files
  check-links      - Verify internal relative links across README and docs
  update-readme    - Regenerate the live repository dashboard in README.md
  verify-inventory - Cryptographic SHA-256 verification of all files against manifest
  all              - Run full audit suite (all checks + index + readme update)
"""

import sys
import argparse
from index_solutions import scan_solutions, generate_index_markdown
from detect_duplicates import run_duplicate_report
from validate_syntax import validate_all_python_files
from check_readme_links import run_link_check
from update_readme import update_readme
from verify_inventory import verify_full_inventory

def main():
    parser = argparse.ArgumentParser(description="LeetCode Repository Architect & Verification Suite")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    subparsers.add_parser("index", help="Scan solutions and generate PROBLEM_INDEX.md")
    subparsers.add_parser("duplicates", help="Scan for duplicate problem numbers and filenames")
    subparsers.add_parser("validate", help="Validate Python syntax across all .py files")
    subparsers.add_parser("check-links", help="Validate all internal links in README and docs")
    subparsers.add_parser("update-readme", help="Update the dynamic dashboard in README.md")
    subparsers.add_parser("verify-inventory", help="Run cryptographic SHA-256 manifest audit")
    subparsers.add_parser("all", help="Execute complete indexing and verification suite")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "index":
        sols = scan_solutions()
        generate_index_markdown(sols)
    elif args.command == "duplicates":
        ok = run_duplicate_report()
        sys.exit(0 if ok else 1)
    elif args.command == "validate":
        validate_all_python_files()
    elif args.command == "check-links":
        ok = run_link_check()
        sys.exit(0 if ok else 1)
    elif args.command == "update-readme":
        update_readme()
    elif args.command == "verify-inventory":
        ok = verify_full_inventory()
        sys.exit(0 if ok else 1)
    elif args.command == "all":
        print("\n" + "=" * 60)
        print("          RUNNING COMPLETE REPOSITORY SUITE")
        print("=" * 60)
        
        print("\n[STEP 1/6] Cryptographic Inventory Audit...")
        inv_ok = verify_full_inventory()
        
        print("\n[STEP 2/6] Scanning and Indexing Solutions...")
        sols = scan_solutions()
        generate_index_markdown(sols)
        
        print("\n[STEP 3/6] Detecting Duplicates and Variations...")
        dup_ok = run_duplicate_report()
        
        print("\n[STEP 4/6] Validating Python Syntax...")
        validate_all_python_files(sols)
        
        print("\n[STEP 5/6] Updating README.md Dashboard...")
        update_readme()
        
        print("\n[STEP 6/6] Verifying Markdown Links...")
        links_ok = run_link_check()
        
        print("\n" + "=" * 60)
        if inv_ok and dup_ok and links_ok:
            print("ALL REPOSITORY CHECKS PASSED PERFECTLY!")
        else:
            print("SOME CHECKS RETURNED WARNINGS OR REQUIRED ATTENTION.")
        print("=" * 60 + "\n")

if __name__ == "__main__":
    main()

