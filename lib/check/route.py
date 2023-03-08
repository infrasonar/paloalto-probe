from libprobe.asset import Asset
from ..query import query


CMD = '<show><routing><route/></routing></show>'


async def check_route(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:
    address = config.get('address')
    if not address:
        address = asset.name

    root = await query(asset, asset_config, config, CMD)
    items = [
        {metric.tag: metric.text for metric in item if metric.text is not None}
        for item in root.find('result')]

    return {
        'route': [
            {
                'name': str(i),
                'destination': item.get('destination'),
                'flags': item.get('flags', '').strip(),
                'nexthop': item.get('nexthop'),
                'route-table': item.get('route-table'),
                'virtual-router': item.get('virtual-router'),
            }
            for i, item in enumerate(items)
        ]
    }
