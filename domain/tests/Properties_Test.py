import unittest
import domain.Properties as p
import logging
import sys
import uuid

from test_helper.Helper import do_profile

logger = logging.getLogger()
logger.level = logging.INFO
logger.addHandler(logging.StreamHandler(sys.stdout))


class Properties_Test(unittest.TestCase):

    @do_profile
    def _create_prop(self):
        prop = p.Properties()
        id = str(uuid.uuid1())
        prop.add_property("id", id)
        propString = prop.to_string()
        logging.getLogger().info(propString)        
        return propString == 'id -> '+ id

    def test_CreateProperties(self):
        assert(self._create_prop())

        
if __name__ == '__main__':
    unittest.main()
