from unittest import TestCase
from src import unittype

# Unit Testの観点


class TestC0(TestCase):
    """
    命令網羅
    1処理を1回以上テストしている
    """
    def test_can_ride(self):
        """
        身長が160cmの場合、乗れると判定される
        :return:
        """
        # テスト対象メソッド
        actual = unittype.judge(160)

        self.assertEqual('乗れる', actual)

