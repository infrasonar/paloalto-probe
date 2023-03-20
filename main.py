from libprobe.probe import Probe
from lib.check.interface import check_interface
from lib.check.route import check_route
from lib.check.session import check_session
from lib.check.system import check_system
from lib.check.tunnel import check_tunnel
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'interface': check_interface,
        'route': check_route,
        'session': check_session,
        'system': check_system,
        'tunnel': check_tunnel,
    }

    probe = Probe("paloalto", version, checks)

    probe.start()
