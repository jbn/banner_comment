import unittest
from banner_comment import banner_comment


EXPECTED = """
###############################################################################
#                             _          _ _                                  #
#                            | |__   ___| | | ___                             #
#                            | '_ \ / _ \ | |/ _ \                            #
#                            | | | |  __/ | | (_) |                           #
#                            |_| |_|\___|_|_|\___/                            #
#                                                                             #
###############################################################################
"""


class TestBannerComment(unittest.TestCase):
    def test_banner_comment(self):
        result = banner_comment("hello")
        self.assertEqual(EXPECTED.strip()+"\n", result)


if __name__ == '__main__':
    unittest.main()
