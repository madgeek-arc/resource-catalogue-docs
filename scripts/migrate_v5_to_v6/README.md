# migrate_v5_to_v6.py

Transforms a directory of exported v5 JSON resource files to conform to the v6 schema, in place. For the full list of transformations applied and detailed notes on catalogue handling, refer to the docstring at the top of [migrate_v5_to_v6.py](migrate_v5_to_v6.py).

> **Note:** Catalogue is no longer a standalone resource type in v6 — it is modelled as a Service. Automatic migration is not possible; the catalogue folder is deleted and manual intervention is required for non-default catalogues.

---

## Step 1 — Export data from v5

Call `GET /api/dump/` on the v5 instance, passing an `Authorization: Bearer <token>` header. This returns a `.zip` file containing all resource type folders and their JSON files. Extract it locally — the extracted directory is what you pass to `-p` argument in the script.

Expected directory structure after extraction:
```
<path>/
  adapter/
  configuration_template/
  configuration_template_instance/
  datasource/
  deployable_service/
  interoperability_record/
  provider/
  resource_interoperability_record/
  service/
  training_resource/
```

## Step 2 — Configure the script

Before running, open `migrate_v5_to_v6.py` and review/update:
- `resource_type_mapping` — old-to-new ID prefix mapping for your instance
- `contact` — default creator/main-contact written to all resources
- `publishingDate` — search for `"2026-03-15"` and update if needed
- `publicContacts` — placeholder email written to all resources

## Step 3 — Run

**Arguments:**

| Argument | Description |
|---|---|
| `-p / --path` | Path to the root directory containing the extracted v5 resource folders |
| `-c / --catalogue` | Default catalogue ID (resources in this catalogue get `catalogueId` set to `null`) |
| `-n / --node` | Node PID to assign to all migrated resources (e.g. `21.15999/node1`) |
| `--dry-run` | Preview all changes without writing, renaming, or deleting anything |

A timestamped backup of the input directory is created automatically at `<path>_backup_YYYYMMDD_HHMMSS/` before any changes are made.

Run with `--dry-run` first and review the output before proceeding:

```
python3 migrate_v5_to_v6.py -p [path/to/folder] -c [catalogue_id] -n [node_pid] --dry-run
```

Once satisfied:

```
python3 migrate_v5_to_v6.py -p [path/to/folder] -c [catalogue_id] -n [node_pid]
```

## Step 4 — Restore data into v6

Re-zip the migrated directory and POST it to `POST /api/restore/` on the v6 instance, passing an `Authorization: Bearer <token>` header.
