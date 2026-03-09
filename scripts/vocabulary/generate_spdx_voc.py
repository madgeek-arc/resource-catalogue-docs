import json
import requests

SPDX_URL = "https://raw.githubusercontent.com/spdx/license-list-data/main/json/licenses.json"

response = requests.get(SPDX_URL)
data = response.json()

spdx_array = []

for lic in data["licenses"]:
    spdx_array.append({
        "id": f"spdx_license-{lic['licenseId']}",
        "name": lic["name"],
        "description": lic["reference"],  # URL goes here
        "parentId": None,
        "type": "Spdx license",
        "extras": {}
    })

output_file = "../../vocabularies/SPDX_LICENSE.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(spdx_array, f, indent=2, ensure_ascii=False)
