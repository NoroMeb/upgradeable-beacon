from scripts.utils import get_account, encode_function_data
from brownie import Treasury, UpgradeableBeacon, BeaconProxy, Contract


def main():
    account = get_account()
    treasury = Treasury.deploy({"from": account})
    beacon = UpgradeableBeacon.deploy(treasury.address, {"from": account})
    treasury_encoded_initializer_function = encode_function_data(
        treasury.initialize, 200
    )
    beacon_proxy = BeaconProxy.deploy(
        beacon.address, treasury_encoded_initializer_function, {"from": account}
    )

    treasury_proxy = Contract.from_abi("Treasury", beacon_proxy.address, treasury.abi)
    print(treasury_proxy.value())
    print(treasury.value())
