from libprobe.asset import Asset
from ..query import query


CMD = '<show><running><tunnel><flow><all/></flow></tunnel></running></show>'


async def check_tunnel(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:
    address = config.get('address')
    if not address:
        address = asset.name

    root = await query(asset, asset_config, config, CMD)
    gateway = [
        {metric.tag: len(metric) if metric.tag == 'users' else metric.text
         for metric in itm}
        for itm in root.find('result/GlobalProtect-Gateway')]
    ipsec = [
        {metric.tag: metric.text for metric in itm}
        for itm in root.find('result/IPSec')]
    sslvpn = [
        {metric.tag: metric.text for metric in itm}
        for itm in root.find('result/SSL-VPN')]

    return {
        'gateway': [gateway],
        'ipsec': [ipsec],
        'sslvpn': [sslvpn]
    }
