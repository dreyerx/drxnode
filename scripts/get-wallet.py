import os
import json
from pathlib import Path

def get_addresses_from_keystore(folder_path):
    addresses = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.startswith('UTC--'):
                p = Path(root)
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    keystore_data = json.load(f)
                    address = keystore_data.get('address')
                    if address:
                        addresses[p.parent.name] = address
    return addresses

folder_path = os.getcwd()
print (folder_path)
addresses = get_addresses_from_keystore(folder_path)
for node, address in addresses.items():
    print(f"Node: {node} Address: {address}")
