from libprobe.asset import Asset
from ..query import query


CMD = '<show><interface>all</interface></show>'


async def check_interface(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:
    address = config.get('address')
    if not address:
        address = asset.name

    root = await query(asset, asset_config, config, CMD)
    obj = root.find('result/ifnet')
    itms = [] if obj is None else [
        {metric.tag: metric.text for metric in itm if metric.text is not None}
        for itm in obj]

    return {
        'interface': itms
    }
