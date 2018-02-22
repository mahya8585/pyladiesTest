from unittest import TestCase
from src import unittype

# Unit Testの観点


class TestLv(TestCase):
    """
    限界値分析
    各同値グループ同士の境界値のテストを行う
    """
    def test_cannot_ride_too_short_0(self):
        """
        身長が0cmの場合、乗れないと判定される
        :return:
        """
        # テスト対象メソッド
        actual = unittype.raging_spirits(0)

        self.assertEqual('乗れない', actual)

    def test_cannot_ride_too_short_116(self):
        """
        身長が116cmの場合、乗れないと判定される
        :return:
        """
        # テスト対象メソッド
        actual = unittype.raging_spirits(116)

        self.assertEqual('乗れない', actual)

    def test_can_ride_117(self):
        """
        身長が117cmの場合、乗れないと判定される
        :return:
        """
        # テスト対象メソッド
        actual = unittype.raging_spirits(117)

        self.assertEqual('乗れる', actual)

    def test_can_ride_118(self):
        """
        身長が118cmの場合、乗れると判定される
        :return:
        """
        # テスト対象メソッド
        actual = unittype.raging_spirits(118)

        self.assertEqual('乗れる', actual)

    def test_can_ride_195(self):
        """
        身長が195cmの場合、乗れないと判定される
        :return:
        """
        # テスト対象メソッド
        actual = unittype.raging_spirits(195)

        self.assertEqual('乗れる', actual)

    def test_cannot_ride_too_tall_196(self):
        """
        身長が196cmの場合、乗れないと判定される
        :return:
        """
        # テスト対象メソッド
        actual = unittype.raging_spirits(196)

        self.assertEqual('乗れない', actual)


