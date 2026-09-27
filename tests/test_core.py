import unittest
from core.semver import SemVer

class TestSemVer(unittest.TestCase):
    def test_version_comparisons(self):
        self.assertTrue(SemVer.is_newer("v2.1.0", "v2.0.9"))
        self.assertTrue(SemVer.is_newer("1.0.1", "1.0.0"))
        self.assertFalse(SemVer.is_newer("1.0.0", "1.0.0"))
        self.assertFalse(SemVer.is_newer("0.9.9", "1.0.0"))
        self.assertEqual(SemVer.compare("v3.4.5", "3.4.5"), 0)

if __name__ == "__main__":
    unittest.main()
