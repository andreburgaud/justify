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

LOREM_IPSUM_50_ZDE = """\
Lorem_ipsum_dolor_sit_amet,_consectetur_adipiscing
elit,  sed  do eiusmod tempor incididunt ut labore
et  dolore  magna aliqua. Ut enim ad minim veniam,
quis  nostrud exercitation ullamco laboris nisi ut
aliquip  ex  ea commodo consequat. Duis aute irure
dolor  in  reprehenderit  in  voluptate velit esse
cillum  dolore eu fugiat nulla pariatur. Excepteur
sint  occaecat  cupidatat  non  proident,  sunt in
culpa  qui  officia  deserunt  mollit  anim id est
laborum."""

LOREM_IPSUM_100_ZDE = """\
Loremipsumdolorsitametconsecteturadipiscingelitseddoeiusmodtemporincididuntutlab
ore et  dolore  magna aliqua. Ut enim ad minim veniam,
quis  nostrud exercitation ullamco laboris nisi ut
aliquip  ex  ea commodo consequat. Duis aute irure
dolor  in  reprehenderit  in  voluptate velit esse
cillum  dolore eu fugiat nulla pariatur. Excepteur
sint  occaecat  cupidatat  non  proident,  sunt in
culpa  qui  officia  deserunt  mollit  anim id est
laborum."""

LOREM_IPSUM_LONG_URL_ZDE = """\
Lorem ipsum dolor sit amet, consectetur adipiscing
elit,  sed  do eiusmod tempor incididunt ut labore
et  dolore  magna aliqua. Ut enim ad minim veniam,
quis  nostrud exercitation ullamco laboris nisi ut
aliquip  ex  ea commodo consequat. Duis aute irure
dolor  in  reprehenderit  in  voluptate velit esse
https://www.example.com/:w:/p/conanthebarbaria/ET35mABuneBNiPXVvqq_dl8Bo_RDoji-RnctWnmf6oplTA?e=joQWLS
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

    def test_justify_zde(self):
        """Justify: one line no space and same length as columns"""

        # Zero division Error in version 0.4.0 when len(line) == columns and no space
        justified_text = justify.justify(LOREM_IPSUM_50_ZDE, shuffle=False, columns=50)
        assert justified_text == LOREM_IPSUM_50_ZDE

    def test_justify_long_line(self):
        """Justify: one line no space and same length as columns"""

        # Zero division Error in version 0.4.0 when len(line) == columns and no space
        justified_text = justify.justify(LOREM_IPSUM_50_ZDE, shuffle=False, columns=30)
        expected_first_line = "Lorem_ipsum_dolor_sit_amet,_co"
        assert expected_first_line == justified_text.split()[0]

    def test_justify_line_long_url(self):
        """Justify: long url"""

        # Zero division Error in version 0.7.0 when no space in a long line
        justified_text = justify.justify(LOREM_IPSUM_LONG_URL_ZDE, shuffle=False, columns=50)
        expected_first_line = "Lorem ipsum dolor sit amet, consectetur adipiscing"
        assert expected_first_line == justified_text.split('\n')[0]

if __name__ == "__main__":
    unittest.main()  # run all tests
