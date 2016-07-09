import sys
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
""".strip() + "\n"


class TestBannerComment(unittest.TestCase):
    def test_banner_comment_as_str(self):
        result = banner_comment("hello", print_to_stdout=False)
        self.assertEqual(EXPECTED, result)

    def test_banner_comment_printed(self):
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        result = banner_comment("hello")
        self.assertIsNone(result)
        self.assertEqual(EXPECTED, sys.stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
