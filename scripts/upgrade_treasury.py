from scripts.utils import get_account
from brownie import TreasuryV2, UpgradeableBeacon, BeaconProxy, Contract, Treasury


def main():
    account = get_account()
    treasury_v2 = TreasuryV2.deploy({"from": account})
    beacon = UpgradeableBeacon[-1]
    beacon_proxy = BeaconProxy[-1]
    print(beacon.implementation())
    upgrade_tx = beacon.upgradeTo(treasury_v2.address, {"from": account})
    upgrade_tx.wait(1)
    print(beacon.implementation())

    treasury_v2_proxy = Contract.from_abi(
        "Treasury", beacon_proxy.address, treasury_v2.abi
    )

    print(treasury_v2_proxy.decrement({"from": account}))
    print(treasury_v2_proxy.value())
