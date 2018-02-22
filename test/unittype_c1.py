from unittest import TestCase
from src import unittype

# Unit Testの観点


class TestC1(TestCase):
    """
    分岐網羅
    分岐が存在する場合は分岐ケース全てのテストを1回以上行なっている
    """
    def test_can_ride(self):
        """
        身長が160cmの場合、乗れると判定される
        :return:
        """
        # テスト対象メソッド
        actual = unittype.raging_spirits(160)

        self.assertEqual('乗れる', actual)

    def test_cannot_ride(self):
        """
        身長が100cmの場合、乗れないと判定される
        :return:
        """
        # テスト対象メソッド
        actual = unittype.raging_spirits(100)

        self.assertEqual('乗れない', actual)

