from unittest import TestCase
from src import unittype

# Unit Testの観点


class TestC2(TestCase):
    """
    条件網羅
    複数の条件が存在している場合、全ての条件の組み合わせのテストを行うこと

    同値分割
    同じ出力(入力)でグループ化し、そのグループの中の代表値でテストを行うこと
    """
    def test_can_ride(self):
        """
        身長が160cmの場合、乗れると判定される
        :return:
        """
        # テスト対象メソッド
        actual = unittype.raging_spirits(160)

        self.assertEqual('乗れる', actual)

    def test_cannot_ride_too_tall(self):
        """
        身長が200cmの場合、乗れないと判定される
        :return:
        """
        # テスト対象メソッド
        actual = unittype.raging_spirits(200)

        self.assertEqual('乗れない', actual)

    def test_cannot_ride_too_short(self):
        """
        身長が200cmの場合、乗れないと判定される
        :return:
        """
        # テスト対象メソッド
        actual = unittype.raging_spirits(200)

        self.assertEqual('乗れない', actual)
