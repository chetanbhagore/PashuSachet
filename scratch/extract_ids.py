import subprocess
import re
import json

content = subprocess.check_output(['git', 'show', 'HEAD:index.html']).decode('utf-8')
ids = re.findall(r'id=[\'"]([^\'"]+)[\'"]', content)
unique_ids = sorted(list(set(ids)))
print(f"Found {len(unique_ids)} IDs from HEAD:index.html")
with open('scratch/all_ids.json', 'w', encoding='utf-8') as f:
    json.dump(unique_ids, f, indent=2)
print("Saved scratch/all_ids.json")
