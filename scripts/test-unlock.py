import os
from eth_keyfile.keyfile import load_keyfile, decode_keyfile_json
from web3 import Web3
from eth_account import Account
from rich.console import Console


console = Console()
ipc_path = os.path.join(
    os.getcwd(),
    "node1",
    "geth.ipc"
)

provider    = Web3(
    Web3.IPCProvider(
        ipc_path=ipc_path
    )
)
keyfile_path    = console.input("Enter keyfile path: ")
password   = console.input("Enter password: ")
keyfile_path_real   = os.path.join(
    os.getcwd(),
    keyfile_path
)