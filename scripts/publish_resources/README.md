# publish_resources.py

Publishes approved, active resources to their public endpoints. For each resource type, the script fetches all approved and active resources, checks whether they are already public (skipping them if so), and posts the remaining ones to the public API.

**Resource types covered:** adapter, catalogue, datasource, deployable_application, interoperability_record, organisation, resource_interoperability_record, service, training_resource

**Arguments:**

| Argument | Description |
|---|---|
| `baseurl` | Base URL of the API (e.g. `https://api.example.com`) |
| `token` | Bearer token for authentication |
| `--dry-run` | Fetch and report what would be posted, without making any changes |

## Run

Always do a dry run first and review the output before proceeding with the actual run.

```
python3 publish_resources.py [baseurl] [token] --dry-run
```

Once you have verified the output:

```
python3 publish_resources.py [baseurl] [token]
```
