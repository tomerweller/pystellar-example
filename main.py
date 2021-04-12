import requests
from stellar_sdk import Server, Keypair, TransactionBuilder, Network

horizon = Server("https://horizon-testnet.stellar.org")

# create keys
sender_keypair = Keypair.random()
receiver_keypair = Keypair.random()

# create accounts
url = 'https://friendbot.stellar.org'
sender_create_response = requests.get(url, params={'addr': sender_keypair.public_key})
print("create sender account", sender_create_response)
receiver_create_response = requests.get(url, params={'addr': receiver_keypair.public_key})
print("create receiver account", receiver_create_response)

# load sender account
sender_account = horizon.load_account(sender_keypair.public_key)
print("get sender account", sender_account)

# make payment
base_fee = horizon.fetch_base_fee()
transaction = (TransactionBuilder(
    source_account=sender_account,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
    base_fee=base_fee,
).append_payment_op(receiver_keypair.public_key, "5.0", "XLM").build())
transaction.sign(sender_keypair)
paymnet_response = horizon.submit_transaction(transaction)
print("payment tx id", paymnet_response["id"])
