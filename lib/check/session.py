from libprobe.asset import Asset
from ..query import query


CMD = '<show><session><info/></session></show>'


async def check_session(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:
    address = config.get('address')
    if not address:
        address = asset.name

    root = await query(asset, asset_config, config, CMD)
    item = {metric.tag: metric.text for metric in root.find('result')}
    item['name'] = 'session'

    return {
        'session': [item]
    }
