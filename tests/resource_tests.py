import unittest
from resources import ManifestQueryReader
class  ManifestQueryReaderTestCase(unittest.TestCase):
    def test_get_retrieve_import_manifest(self):
        self.assertIsNotNone(ManifestQueryReader().get_retrieve_import_manifest())

if __name__ == '__main__':
    unittest.main()
