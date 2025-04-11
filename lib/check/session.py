from libprobe.asset import Asset
from ..query import query
from ..utils import to_int, to_bool


CMD = '<show><session><info/></session></show>'


async def check_session(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:
    address = config.get('address')
    if not address:
        address = asset.name

    root = await query(asset, asset_config, config, CMD)
    obj = root.find('result')
    item = {} if obj is None else {metric.tag: metric.text for metric in obj}

    return {
        'session': [{
            'name': 'session',
            'age-accel-en': to_bool(item.get('age-accel-en')),
            'age-accel-thresh': to_int(item.get('age-accel-thresh')),
            'age-accel-tsf': to_int(item.get('age-accel-tsf')),
            'age-scan-ssf': to_int(item.get('age-scan-ssf')),
            'age-scan-thresh': to_int(item.get('age-scan-thresh')),
            'age-scan-tmo': to_int(item.get('age-scan-tmo')),
            'cps': to_int(item.get('cps')),
            'dis-def': to_int(item.get('dis-def')),
            'dis-sctp': to_int(item.get('dis-sctp')),
            'dis-tcp': to_int(item.get('dis-tcp')),
            'dis-udp': to_int(item.get('dis-udp')),
            'dp': item.get('dp'),
            'hw-offload': to_bool(item.get('hw-offload')),
            'hw-udp-offload': to_bool(item.get('hw-udp-offload')),
            'icmp-unreachable-rate': to_int(item.get('icmp-unreachable-rate')),
            'ipv6-fw': to_bool(item.get('ipv6-fw')),
            'kbps': to_int(item.get('kbps')),
            'max-pending-mcast': to_int(item.get('max-pending-mcast')),
            'num-active': to_int(item.get('num-active')),
            'num-bcast': to_int(item.get('num-bcast')),
            'num-gtpc': to_int(item.get('num-gtpc')),
            'num-gtpu-active': to_int(item.get('num-gtpu-active')),
            'num-gtpu-pending': to_int(item.get('num-gtpu-pending')),
            'num-http2-5gc': to_int(item.get('num-http2-5gc')),
            'num-icmp': to_int(item.get('num-icmp')),
            'num-imsi': to_int(item.get('num-imsi')),
            'num-installed': to_int(item.get('num-installed')),
            'num-max': to_int(item.get('num-max')),
            'num-mcast': to_int(item.get('num-mcast')),
            'num-pfcpc': to_int(item.get('num-pfcpc')),
            'num-predict': to_int(item.get('num-predict')),
            'num-sctp-assoc': to_int(item.get('num-sctp-assoc')),
            'num-sctp-sess': to_int(item.get('num-sctp-sess')),
            'num-tcp': to_int(item.get('num-tcp')),
            'num-udp': to_int(item.get('num-udp')),
            'oor-action': item.get('oor-action'),
            'pps': to_int(item.get('pps')),
            'strict-checksum': to_bool(item.get('strict-checksum')),
            'sw-cutthrough': to_bool(item.get('sw-cutthrough')),
            'tcp-cong-ctrl': to_int(item.get('tcp-cong-ctrl')),
            'tcp-diff-syn-rej': to_bool(item.get('tcp-diff-syn-rej')),
            'tcp-no-refresh-fin-rst':
                to_bool(item.get('tcp-no-refresh-fin-rst')),
            'tcp-nonsyn-rej': to_bool(item.get('tcp-nonsyn-rej')),
            'tcp-reject-siw-enable':
                to_bool(item.get('tcp-reject-siw-enable')),
            'tcp-reject-siw-thresh': to_int(item.get('tcp-reject-siw-thresh')),
            'tcp-strict-rst': to_bool(item.get('tcp-strict-rst')),
            'tmo-5gcdelete': to_int(item.get('tmo-5gcdelete')),
            'tmo-cp': to_int(item.get('tmo-cp')),
            'tmo-def': to_int(item.get('tmo-def')),
            'tmo-icmp': to_int(item.get('tmo-icmp')),
            'tmo-sctp': to_int(item.get('tmo-sctp')),
            'tmo-sctpcookie': to_int(item.get('tmo-sctpcookie')),
            'tmo-sctpinit': to_int(item.get('tmo-sctpinit')),
            'tmo-sctpshutdown': to_int(item.get('tmo-sctpshutdown')),
            'tmo-tcp': to_int(item.get('tmo-tcp')),
            'tmo-tcp-delayed-ack': to_int(item.get('tmo-tcp-delayed-ack')),
            'tmo-tcp-unverif-rst': to_int(item.get('tmo-tcp-unverif-rst')),
            'tmo-tcphalfclosed': to_int(item.get('tmo-tcphalfclosed')),
            'tmo-tcphandshake': to_int(item.get('tmo-tcphandshake')),
            'tmo-tcpinit': to_int(item.get('tmo-tcpinit')),
            'tmo-tcptimewait': to_int(item.get('tmo-tcptimewait')),
            'tmo-udp': to_int(item.get('tmo-udp')),
            'tunnel-accel': to_bool(item.get('tunnel-accel')),
            'vardata-rate': to_int(item.get('vardata-rate')),
        }]
    }
