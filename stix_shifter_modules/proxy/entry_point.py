from stix_shifter_utils.utils.entry_point_base import EntryPointBase
from .stix_transmission.proxy_connector import Connector
from .stix_translation.proxy_translator import Translator

class EntryPoint(EntryPointBase):

    def __init__(self, connection={}, configuration={}, options={}):
        super(EntryPoint, self).__init__(options)

        if connection:
            connector = Connector(connection, configuration)
            is_async = connector.is_async()
            self.set_async(is_async)
            self.setup_transmission_basic(connector)
        else:
            self.add_dialect('default', Translator(), None, True)