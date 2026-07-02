"""
Normalise the 'package' field on adapter resources.

The field was incorrectly stored as a list in some records. This script finds
every adapter whose package value is a list and converts it to a plain string.

Multi-value handling
--------------------
If the list contains more than one entry, only the FIRST value is kept and the
rest are discarded. This is intentional: the schema expects a single package URL,
and no automated heuristic can reliably pick the "correct" one from multiple
candidates. The discarded values are reported so they can be reviewed manually.

Usage:
    python3 fix_adapter_package_field.py <dump_folder>            # dry-run (default)
    python3 fix_adapter_package_field.py <dump_folder> --dry-run  # explicit dry-run
    python3 fix_adapter_package_field.py <dump_folder> --fix      # apply fixes in place
"""

import argparse
import json
import os
import sys
from pathlib import Path


def scan(dump_path: str, apply: bool = False) -> list[dict]:
    adapter_dir = Path(dump_path) / "adapter"
    if not adapter_dir.is_dir():
        print(f"[WARN] No 'adapter' folder found under {dump_path}", file=sys.stderr)
        return []

    findings = []

    for json_file in sorted(adapter_dir.glob("*.json")):
        if json_file.name == "schema.json":
            continue
        try:
            raw = json_file.read_text(encoding="utf-8")
            wrapper = json.loads(raw)
            payload = json.loads(wrapper["payload"])
        except (json.JSONDecodeError, KeyError, UnicodeDecodeError) as exc:
            print(f"[WARN] Skipping {json_file.name}: {exc}", file=sys.stderr)
            continue

        adapter = payload.get("adapter", {})
        package = adapter.get("package")

        if not isinstance(package, list):
            continue

        kept = package[0] if package else ""
        discarded = package[1:]

        if apply:
            adapter["package"] = kept
            wrapper["payload"] = json.dumps(payload, ensure_ascii=False)
            json_file.write_text(
                json.dumps(wrapper, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

        findings.append({
            "file": json_file.name,
            "resource_id": payload.get("id") or wrapper.get("id", "unknown"),
            "kept": kept,
            "discarded": discarded,
        })

    return findings


def _print_report(findings: list[dict], applied: bool) -> None:
    if not findings:
        print("No adapter files with a list-type 'package' field found.")
        return

    mode = "Fixed" if applied else "Would fix"
    prefix = "" if applied else "[DRY RUN] "
    multi = [f for f in findings if f["discarded"]]

    print(f"{prefix}Found {len(findings)} adapter(s) with a list 'package' field:\n")

    for f in findings:
        print(f"  File     : {f['file']}")
        print(f"  Resource : {f['resource_id']}")
        print(f"  {mode}  : {f['kept']!r}")
        if f["discarded"]:
            print(f"  Dropped  : {f['discarded']}")
        print()

    if multi:
        print(f"  NOTE: {len(multi)} file(s) had multiple values — only the first was kept.")
        print(f"  Review dropped values above before proceeding.\n")

    verb = "Fixed" if applied else "Would fix"
    print(f"Summary: {verb} {len(findings)} file(s).")
    if not applied:
        print("Run with --fix to apply changes.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert adapter 'package' field from list to string."
    )
    parser.add_argument("dump_path", help="Path to the dump folder")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--dry-run", action="store_true", default=True,
        help="Show what would be changed without modifying files (default)",
    )
    group.add_argument(
        "--fix", action="store_true", default=False,
        help="Apply the conversion in place",
    )
    args = parser.parse_args()

    if not os.path.isdir(args.dump_path):
        print(f"Error: '{args.dump_path}' is not a directory", file=sys.stderr)
        sys.exit(1)

    findings = scan(args.dump_path, apply=args.fix)
    _print_report(findings, applied=args.fix)


if __name__ == "__main__":
    main()
