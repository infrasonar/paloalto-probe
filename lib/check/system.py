from libprobe.asset import Asset
from ..utils import datetime_to_timestamp, datefmt_to_timestamp, uptime_seconds
from ..query import query


CMD = '<show><system><info/></system></show>'


async def check_system(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:
    address = config.get('address')
    if not address:
        address = asset.name

    root = await query(asset, asset_config, config, CMD)
    item = {metric.tag: metric.text for metric in root.find('result/system')}
    return {
        'system': [{
            'name': 'system',
            'hostname': item.get('hostname'),
            'ip-address': item.get('ip-address'),
            'public-ip-address': item.get('public-ip-address'),
            'netmask': item.get('netmask'),
            'default-gateway': item.get('default-gateway'),
            'is-dhcp': item.get('is-dhcp'),
            'ipv6-address': item.get('ipv6-address'),
            'ipv6-link-local-address': item.get('ipv6-link-local-address'),
            'mac-address': item.get('mac-address'),
            'time': datefmt_to_timestamp(item.get('time'), '%c'),
            'uptime': uptime_seconds(item.get('uptime')),
            'devicename': item.get('devicename'),
            'family': item.get('family'),
            'model': item.get('model'),
            'serial': item.get('serial'),
            'cloud-mode': item.get('cloud-mode'),
            'sw-version': item.get('sw-version'),
            'global-protect-client-package-version':
                item.get('global-protect-client-package-version'),
            'device-dictionary-version': item.get('device-dictionary-version'),
            'device-dictionary-release-date':
                datetime_to_timestamp(
                    item.get('device-dictionary-release-date')),
            'app-version': item.get('app-version'),
            'app-release-date':
                datetime_to_timestamp(item.get('app-release-date')),
            'av-version': item.get('av-version'),
            'av-release-date':
                datetime_to_timestamp(item.get('av-release-date')),
            'threat-version': item.get('threat-version'),
            'threat-release-date':
                datetime_to_timestamp(item.get('threat-release-date')),
            'wf-private-version': item.get('wf-private-version'),
            'wf-private-release-date': item.get('wf-private-release-date'),
            'url-db': item.get('url-db'),
            'wildfire-version': item.get('wildfire-version'),
            'wildfire-release-date':
                datetime_to_timestamp(item.get('wildfire-release-date')),
            'wildfire-rt': item.get('wildfire-rt'),
            'url-filtering-version': item.get('url-filtering-version'),
            'global-protect-datafile-version':
                item.get('global-protect-datafile-version'),
            'global-protect-datafile-release-date':
                item.get('global-protect-datafile-release-date'),
            'global-protect-clientless-vpn-version':
                item.get('global-protect-clientless-vpn-version'),
            'logdb-version': item.get('logdb-version'),
            'platform-family': item.get('platform-family'),
            'vpn-disable-mode': item.get('vpn-disable-mode'),
            'multi-vsys': item.get('multi-vsys'),
            'operational-mode': item.get('operational-mode'),
            'advanced-routing': item.get('advanced-routing'),
            'device-certificate-status': item.get('device-certificate-status'),
        }]
    }
