from brownie import accounts, network, config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['ganache-local', 'development', 'mainnet-fork']

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print(accounts[0].balance())
        return accounts[0]
    if id:
        return accounts.load(id)
    
    return accounts.add(config['wallets']['from_key'])
   