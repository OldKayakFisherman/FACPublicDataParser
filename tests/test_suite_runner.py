
import unittest


if __name__ == '__main__':

    from resource_test import ManifestQueryReaderTestCase

    suite1 = unittest.TestLoader().loadTestsFromTestCase(ManifestQueryReaderTestCase)

    master_suite = unittest.TestSuite([suite1])

    unittest.TextTestRunner(verbosity=2).run(master_suite)

