import aiohttp
import xml.etree.ElementTree as ET
from libprobe.asset import Asset
from .connector import get_connector


async def query(
        asset: Asset,
        local_config: dict,
        config: dict,
        cmd: str) -> ET.Element:

    address = config.get('address')
    if not address:
        address = asset.name
    assert local_config, 'missing credentials'

    global_protect = config.get('global_protect', False)
    port = ':4443' if global_protect and ':' not in address else ''

    api_key = local_config['secret']
    headers = {
        'X-PAN-KEY': api_key,
    }
    url = f'https://{address}{port}/api/?type=op&cmd={cmd}'

    async with aiohttp.ClientSession(connector=get_connector()) as session:
        async with session.post(url, headers=headers, ssl=False) as resp:
            assert resp.status // 100 == 2, \
                f'response status code: {resp.status}; reason: {resp.reason}'

            xml = await resp.text()
            tree = ET.fromstring(xml)
            status = tree.attrib['status']
            assert status == 'success', f'response status: {status}'

            return tree
