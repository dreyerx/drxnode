import os
import json
from pathlib import Path
from rich.console import Console
from web3 import Web3, HTTPProvider

provider = Web3(
    HTTPProvider(
        "http://localhost:8545"
    )
)
console  = Console()

def get_keystore(folder_path):
    console.log("start crawl keystore from path")
    data = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if str(file).startswith("UTC--"):
                p   = Path(root)
                console.log(f"found keystore from {p.parent.name}")
                file_path   = os.path.join(root,file)
                with open(file_path, "r") as File:
                    keystore_content    = json.loads(File.read())
                    data.append({
                        "node": p.parent.name,
                        "content": keystore_content
                    })
    return data

def get_passwords(folder_path):
    console.log("start crawl password from path")
    passwords = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if str(file).startswith("password"):
                file_path   = os.path.join(root, file)
                with open(file_path, "r") as File:
                    paswd = File.read()
                    passwords.append(paswd)
    return passwords

def unlock(keystores: list, passwords: list):
    for keystore in keystores:
        console.log(f"start brute force for {keystore['node']}")
        for password in passwords:
            try:
                private_key = provider.eth.account.decrypt(keystore['content'], password)
                console.log(f"found for node {keystore['node']}, password {password} private_key {provider.to_hex(private_key)}")
                break
            except ValueError:
                console.log(f"mismatch password for keystore {keystore['node']}")

def main():
    root_path   = os.getcwd()
    console.log(f"root path {root_path}")
    keystores   = get_keystore(root_path)
    console.log(f"found {len(keystores)} keystores")
    passwords   = get_passwords(root_path)
    console.log(f"found {len(passwords)} passwords")

    unlock(keystores, passwords)

if __name__ == "__main__":
    main()