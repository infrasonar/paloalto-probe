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
    api_key = asset_config['secret']

    url_params = urlencode({
        'type': 'op',
        'cmd': cmd,
        'key': api_key,
    })
    url = f'https://{address}/api/{url_params}'

    async with aiohttp.ClientSession() as session:
        async with session.post(url, ssl=False) as resp:
            resp.raise_for_status()

            xml = await resp.text()
            tree = ET.fromstring(xml)
            status = tree.attrib['status']
            assert status == 'success', f'response status: {status}'

            return tree
