from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query


CMD = '<show><interface>all</interface></show>'


class CheckInterface(Check):
    key = 'interface'

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        root = await query(asset, local_config, config, CMD)
        obj = root.find('result/ifnet')
        itms = [] if obj is None else [
            {metric.tag: metric.text
             for metric in itm if metric.text is not None}
            for itm in obj]

        return {
            'interface': itms
        }
