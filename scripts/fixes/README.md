# fixes

Collection of small, one-off scripts for patching specific data issues in resource dumps. Unlike the other folders in `scripts/`, this one isn't a single tool — each script here targets a narrow, self-contained bug or data inconsistency. New fix scripts should be added to this folder and listed in the index below.

## Index

| Script | When to use | Description | Created |
|---|---|---|---|
| [fix_adapter_package_field.py](fix_adapter_package_field.py) | When adapter resources have a `package` field stored as a list instead of a string | Scans a dump folder for adapter resources whose `package` field is a list, and rewrites it to a plain string (keeping the first value, reporting any discarded extras) | 2026-07-02 |

## Conventions

Scripts in this folder generally follow the same pattern:

- Operate on a local dump folder (JSON files per resource) rather than calling the API directly.
- Default to a **dry-run** mode that reports what would change without modifying anything.
- Require an explicit `--fix` (or similar) flag to apply changes in place.
- Print a summary of findings, including anything that needs manual review.

Always run in dry-run mode first and review the output before applying a fix.
