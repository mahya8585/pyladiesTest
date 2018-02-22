from unittest import TestCase
from src import unittype

# Unit Testの観点


class TestUnitType(TestCase):
    """
    UnitTestコードをブラッシュアップしよう
    """

    def test_cannot_ride(self):
        """
        0, 116, 196, 197は乗れないと判定される
        :return:
        """
        # 0
        actual = unittype.raging_spirits(116)
        self.assertEqual('乗れない', actual)

        # 116
        actual = unittype.raging_spirits(116)
        self.assertEqual('乗れない', actual)

        # 196
        actual = unittype.raging_spirits(196)
        self.assertEqual('乗れない', actual)

        # 197
        actual = unittype.raging_spirits(116)
        self.assertEqual('乗れない', actual)

    def test_can_ride(self):
        """
        117, 118, 195は乗れると判定される
        :return:
        """
        # 117
        actual = unittype.raging_spirits(117)
        self.assertEqual('乗れる', actual)

        # 118
        actual = unittype.raging_spirits(118)
        self.assertEqual('乗れる', actual)

        # 195
        actual = unittype.raging_spirits(195)
        self.assertEqual('乗れる', actual)

