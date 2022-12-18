import json
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
from algosdk.future.transaction import AssetConfigTxn, wait_for_confirmation
from algosdk.mnemonic import to_private_key

algod_address = "https://testnet-api.algonode.cloud"
algod_client = algod.AlgodClient("",algod_address)

def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print(f"My address: {address}")
    print(f"My private key: {private_key}")
    print(f"My passphrase: {mnemonic.from_private_key(private_key)}")

def createASA(asset_creator_address, private_key):
    txn = AssetConfigTxn(
        sender=asset_creator_address,
        sp=algod_client.suggested_params(),
        total=1000,
        default_frozen=False,
        unit_name="CRAP",
        asset_name="crap token",
        manager=asset_creator_address,
        reserve=asset_creator_address,
        freeze=asset_creator_address,
        clawback=asset_creator_address,
        url="https://www",
        decimals=0
    )

    signed_txn = txn.sign(private_key)

    #send the transaction to the network and retrieve the txid.
    try:
        txid = algod_client.send_transaction(signed_txn)
        print(f"Signed transaction with txID: {txid}")
        # Wait for the transaction to be confirmed
        confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
        print(f"TXID: {txid}")
        print(f"Result confirmed in round: {confirmed_txn['confirmed-round']}")
    except Exception as e:
        print(e)

    # Retrieve the asset ID of the newly created asset by first ensuring that the creation transaction is confirmed, then grabbing the asset id from the transaction
    print(f"Transaction information: {json.dumps(confirmed_txn, indent=4)}")

# Generate Account with generate_algorand_keypair()
my_address = 'QJVE44BJNYCLLXFIMBQ373ZGAPX7O37MJTQ2QTUSWBTC6MDVOE6VW4CIGY'
passphrase = "hurt misery useless picture where valley program metal solution tattoo whip damp raw debris sustain pave carry clutch group upon weapon conduct lemon abandon tower"

my_private_key = to_private_key(passphrase)

# With the above information fund account with dispenser.

# Then create ASA with createASA(), passing in the address and private key