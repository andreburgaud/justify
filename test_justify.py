"""Justify tests"""

import unittest

import justify

LOREM_IPSUM_50 = """\
Lorem ipsum dolor sit amet, consectetur adipiscing
elit,  sed  do eiusmod tempor incididunt ut labore
et  dolore  magna aliqua. Ut enim ad minim veniam,
quis  nostrud exercitation ullamco laboris nisi ut
aliquip  ex  ea commodo consequat. Duis aute irure
dolor  in  reprehenderit  in  voluptate velit esse
cillum  dolore eu fugiat nulla pariatur. Excepteur
sint  occaecat  cupidatat  non  proident,  sunt in
culpa  qui  officia  deserunt  mollit  anim id est
laborum."""


class JustifyTest(unittest.TestCase):
    """Main Justify test case"""

    def test_get_separators(self):
        """List of separators"""
        separators = justify.get_separators(
            space_count=2, sep_count=4, padding_count=2, shuffle=False
        )
        assert separators == ["    ", "    ", "   ", "   "]

    def test_get_separators_shuffle(self):
        """List of separators with shuffle"""
        separators = justify.get_separators(
            space_count=2, sep_count=4, padding_count=2, shuffle=True
        )
        assert sorted(separators, key=len) == ["   ", "   ", "    ", "    "]

    def test_interleave(self):
        """Interleave words and separators"""
        words = ["un", "deux", "trois", "quatre"]
        separators = ["  ", "   ", "  "]
        expected = "un  deux   trois  quatre"
        assert expected == justify.interleave(words, separators)

    def test_justify(self):
        """Justify"""
        section = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
            "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud "
            "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure "
            "dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
            "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia "
            "deserunt mollit anim id est laborum."
        )
        justified_text = justify.justify(section, shuffle=False, columns=50)
        assert justified_text == LOREM_IPSUM_50


if __name__ == "__main__":
    unittest.main()  # run all tests
