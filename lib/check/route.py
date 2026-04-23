from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query


CMD = '<show><routing><route/></routing></show>'


class CheckRoute(Check):
    key = 'route'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        root = await query(asset, local_config, config, CMD)
        items = [
            {metric.tag: metric.text
             for metric in item if metric.text is not None}
            for item in root.findall('result/entry')]

        return {
            'route': [
                {
                    'name': str(i),
                    'destination': item.get('destination'),
                    'flags': item['flags'].strip() if 'flags' in item else
                    None,
                    'nexthop': item.get('nexthop'),
                    'route-table': item.get('route-table'),
                    'virtual-router': item.get('virtual-router'),
                }
                for i, item in enumerate(items)
            ]
        }
