#!/usr/bin/env python3
"""
Migrates resources to public by:
1. For each type in ENDPOINT_MAP, fetching all resources via GET /{endpoint}/bundle/all
2. Posting each resource to POST /public/{endpoint}/add
"""

import argparse
import requests

# Maps resource type name -> (get_path, post_path)
# get_path: used for GET /{get_path}/bundle/all
# post_path: used for POST /public/{post_path}/add
ENDPOINT_MAP = {
    "adapter":                         ("adapter",                        "adapter"),
    "catalogue":                       ("catalogue",                      "catalogue"),
    "configuration_template":          ("configurationTemplate",          "configurationTemplate"),
    "configuration_template_instance": ("configurationTemplateInstance",  "configurationTemplateInstance"),
    "datasource":                      ("datasource",                     "datasource"),
    "deployable_application":          ("deployableApplication",          "deployableApplication"),
    "interoperability_record":         ("interoperabilityRecord",         "interoperabilityRecord"),
    "organisation":                    ("provider",                       "provider"),
    "resource_interoperability_record":("resourceInteroperabilityRecord", "resourceInteroperabilityRecord"),
    "service":                         ("service",                        "service"),
    "training_resource":               ("trainingResource",               "trainingResource"),
}


def get_all_resources(base_url: str, headers: dict, endpoint: str) -> list:
    resources = []
    from_idx = 0
    quantity = 10000
    while True:
        url = f"{base_url}/{endpoint}/bundle/all?status=approved&active=true"
        resp = requests.get(url, headers=headers, params={"from": from_idx, "quantity": quantity})
        resp.raise_for_status()
        data = resp.json()
        page = data.get("results", [])
        resources.extend(page)
        total = data.get("total", 0)
        from_idx += len(page)
        if from_idx >= total or not page:
            break
    return resources


def check_public(base_url: str, headers: dict, post_path: str, resource_id: str) -> str:
    url = f"{base_url}/public/{post_path}/{resource_id}"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return "skip"
    if resp.status_code == 404:
        return "post"
    return f"error:{resp.status_code} {resp.text[:200]}"


def post_public(base_url: str, headers: dict, post_path: str, resource: dict) -> dict:
    url = f"{base_url}/public/{post_path}/add"
    resp = requests.post(url, json=resource, headers={**headers, "Content-Type": "application/json"})
    resp.raise_for_status()
    return resp.json()


def main():
    parser = argparse.ArgumentParser(description="Publish approved active resources to their public endpoints")
    parser.add_argument("baseurl", help="Base URL (e.g. https://api.example.com)")
    parser.add_argument("token", help="Bearer token for authentication")
    parser.add_argument("--dry-run", action="store_true", help="Fetch only, do not POST")
    args = parser.parse_args()

    base_url = args.baseurl.rstrip("/")
    headers = {"Authorization": f"Bearer {args.token}", "Accept": "application/json"}

    for name, (get_path, post_path) in ENDPOINT_MAP.items():

        print(f"\n[{name}] Fetching from GET /{get_path}/bundle/all?status=approved&active=true ...")
        try:
            resources = get_all_resources(base_url, headers, get_path)
        except requests.HTTPError as e:
            print(f"  ERROR fetching: {e}")
            continue

        print(f"  Got {len(resources)} resource(s)")

        ok = 0
        skipped = 0
        errors = 0
        for resource in resources:
            raw_id = resource.get("id", "")
            public_id = raw_id[:-2]  # strip trailing "00"

            action = check_public(base_url, headers, post_path, public_id)

            if action.startswith("error:"):
                print(f"  ERROR checking {public_id}: {action[6:]}")
                errors += 1
                continue

            if action == "skip":
                skipped += 1
                continue

            if args.dry_run:
                print(f"  [dry-run] would POST {public_id} to /public/{post_path}/add")
                ok += 1
                continue

            try:
                post_public(base_url, headers, post_path, resource)
                ok += 1
            except requests.HTTPError as e:
                print(f"  ERROR posting {public_id}: {e} — {e.response.text[:200]}")
                errors += 1

        print(f"  Done: {ok} posted, {skipped} skipped, {errors} errors")

    print("\nFinished.")


if __name__ == "__main__":
    main()
