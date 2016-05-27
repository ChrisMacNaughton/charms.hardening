import sys
import mock

# mock out some charmhelpers libraries as they have apt install side effects
charmhelpers = mock.MagicMock()
sys.modules['charmhelpers'] = charmhelpers
sys.modules['charmhelpers.core'] = charmhelpers.core
sys.modules['charmhelpers.core.hookenv'] = charmhelpers.core.hookenv
sys.modules['charmhelpers.core.host'] = charmhelpers.core.host
sys.modules['charmhelpers.core.templating'] = charmhelpers.core.templating
sys.modules['charmhelpers.contrib'] = charmhelpers.contrib
sys.modules['charmhelpers.contrib.hardening'] = charmhelpers.contrib.hardening
sys.modules['charmhelpers.contrib.hardening.utils'] = (
    charmhelpers.contrib.hardening.utils)
sys.modules['charmhelpers.contrib.hardening.templating'] = (
    charmhelpers.contrib.hardening.templating)
sys.modules['charmhelpers.contrib.network'] = charmhelpers.contrib.network
sys.modules['charmhelpers.contrib.network.ip'] = (
    charmhelpers.contrib.network.ip)
sys.modules['charmhelpers.fetch'] = charmhelpers.fetch
sys.modules['charmhelpers.cli'] = charmhelpers.cli
sys.modules['charmhelpers.contrib.hahelpers'] = charmhelpers.contrib.hahelpers
sys.modules['charmhelpers.contrib.hahelpers.cluster'] = (
    charmhelpers.contrib.hahelpers.cluster)
