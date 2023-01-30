from libprobe.probe import Probe
from lib.check.paloalto import check_paloalto
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'paloalto': check_paloalto
    }

    probe = Probe("paloalto", version, checks)

    probe.start()
