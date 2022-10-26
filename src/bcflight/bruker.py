import logging
_logger = logging.getLogger(__name__)

try:
    from hyperspy.io_plugins.bruker import *
    _logger.info("Using bruker.py original hyperspy code")
except:
    from bcflight.third_party.bruker import *
    _logger.info("Using patched bruker.py code")
