import aiohttp
import xml.etree.ElementTree as ET
from urllib.parse import urlencode
from libprobe.asset import Asset


async def query(
        asset: Asset,
        asset_config: dict,
        check_config: dict,
        cmd: str) -> ET.Element:

    address = check_config.get('address')
    if not address:
        address = asset.name
    assert asset_config, 'missing credentials'

    global_protect = check_config.get('global_protect', False)
    port = ':4443' if global_protect and ':' not in address else ''

    api_key = asset_config['secret']
    headers = {
        'X-PAN-KEY': api_key,
    }
    url = f'https://{address}{port}/api/?type=op&cmd={cmd}'

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, ssl=False) as resp:
            assert resp.status // 100 == 2, \
                f'response status code: {resp.status}; reason: {resp.reason}'

            xml = await resp.text()
            tree = ET.fromstring(xml)
            status = tree.attrib['status']
            assert status == 'success', f'response status: {status}'

            return tree
