from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query


CMD = '<show><vpn><ike-sa /></vpn></show>'


class CheckVpn(Check):
    key = 'vpn'

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        address = config.get('address')
        if not address:
            address = asset.name

        root = await query(asset, local_config, config, CMD)
        itms = [
            {metric.tag: metric.text
             for metric in itm if metric.text is not None}
            for itm in root.findall('result/entry')]

        return {
            'vpn': itms
        }
