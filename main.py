from libprobe.probe import Probe
from lib.check.interface import CheckInterface
from lib.check.route import CheckRoute
from lib.check.session import CheckSession
from lib.check.system import CheckSystem
from lib.check.tunnel import CheckTunnel
from lib.check.vpn import CheckVpn
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckInterface,
        CheckRoute,
        CheckSession,
        CheckSystem,
        CheckTunnel,
        CheckVpn,
    )

    probe = Probe("paloalto", version, checks)

    probe.start()
