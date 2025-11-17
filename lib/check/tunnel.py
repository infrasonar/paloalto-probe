from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query


CMD = '<show><running><tunnel><flow><all/></flow></tunnel></running></show>'


class CheckTunnel(Check):
    key = 'tunnel'

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        root = await query(asset, local_config, config, CMD)
        gateway = [
            {metric.tag: len(metric) if metric.tag == 'users' else metric.text
             for metric in itm}
            for itm in root.findall('result/GlobalProtect-Gateway/entry')]
        ipsec = [
            {metric.tag: metric.text for metric in itm}
            for itm in root.findall('result/IPSec/entry')]
        sslvpn = [
            {metric.tag: metric.text for metric in itm}
            for itm in root.findall('result/SSL-VPN/enty')]

        return {
            'gateway': gateway,
            'ipsec': ipsec,
            'sslvpn': sslvpn,
        }
