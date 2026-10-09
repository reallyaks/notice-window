import unittest
from pathlib import Path

from notice_window.engine import find_notices, render

TEXT = Path("samples/contract.txt").read_text()


class NoticeTests(unittest.TestCase):
    def test_finds_the_four_windows(self):
        notices = find_notices(TEXT)
        self.assertEqual([item.days for item in notices], [30, 10, 60, 5])
        self.assertEqual(notices[1].kind, "business")

    def test_does_not_invent_a_ninety_day_notice(self):
        self.assertNotIn(90, [item.days for item in find_notices(TEXT)])

    def test_committed_report(self):
        self.assertEqual(render(find_notices(TEXT), "contract.txt"), Path("samples/notices.md").read_text())


if __name__ == "__main__":
    unittest.main()
