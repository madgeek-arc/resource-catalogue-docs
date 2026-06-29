# migrate_v5_to_v6.py

Migrates a directory of exported v5 JSON resource files to the v6 schema in place.

**What it does:**
- Normalises resource statuses (`approved` / `rejected` / `pending`)
- Removes deprecated fields (`migrationStatus`, `transferContactInformation`, `resourceExtras`)
- Moves `catalogueId` from the resource payload to the bundle level
- Replaces `node` with `nodePID` on every resource
- Updates resource IDs and cross-references using the prefix mapping defined at the top of the script
- Applies resource-type-specific field renames, additions, and removals
- Renames folders: `deployable_service` → `deployable_application`, `provider` → `organisation`
- Deletes folders no longer part of v6 (draft folders, helpdesk, monitoring, catalogue, etc.)
- Removes `schema.json` files from all remaining folders
- Reports duplicate IDs and catalogues requiring manual follow-up

> **Note:** Catalogue is no longer a standalone resource type in v6 — it is modelled as a Service. Automatic migration is not possible; the catalogue folder is deleted and manual intervention is required for non-default catalogues.

**Before running**, open the script and review/update:
- `resource_type_mapping` — old-to-new ID prefix mapping for your instance
- `contact` — default creator/main-contact written to all resources
- `publishingDate` — search for `"2026-03-15"` and update if needed
- `publicContacts` — placeholder email written to all resources

**Arguments:**

| Argument | Description |
|---|---|
| `-p / --path` | Path to the root directory containing the exported v5 resource folders |
| `-c / --catalogue` | Default catalogue ID (resources in this catalogue get `catalogueId` set to `null`) |
| `-n / --node` | Node PID to assign to all migrated resources (e.g. `21.15999/node1`) |
| `--dry-run` | Preview all changes without writing, renaming, or deleting anything |

A timestamped backup of the input directory is created automatically before any changes are made.

## Run
```
python3 migrate_v5_to_v6.py -p [path/to/folder] -c [catalogue_id] -n [node_pid]
python3 migrate_v5_to_v6.py -p [path/to/folder] -c [catalogue_id] -n [node_pid] --dry-run
```
