import unittest
from resources import ManifestQueryReader


class ManifestQueryReaderTestCase(unittest.TestCase):
    def test_get_retrieve_import_manifest(self):
        assert ManifestQueryReader().get_retrieve_import_manifest() is not None
    def test_get_insert_manifest(self):
        assert  ManifestQueryReader().get_insert_manifest() is not None

if __name__ == '__main__':
    unittest.main()
