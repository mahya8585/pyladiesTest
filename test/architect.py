from unittest import TestCase
from src import architect


# 基本的に1テスト1観点
# "条件" と "期待値" は1対1になるよう明記する
# に合わせた形に書き直そう！


class TestExtract(TestCase):

    def test_get_id_1(self):
        """
        IDが1の場合、下記のデータが取得できること
        - name : Mickey
        - type : ネズミ
        :return:
        """
        # テスト対象メソッド
        actual = architect.extract_user(1)

        # データkeyはnameとtypeを保持していること
        expected_key = ['name', 'type']
        for key in expected_key:
            self.assertTrue(key in actual)

        # 名前がMickeyであること
        self.assertEqual('Mickey', actual['name'])

        # typeがネズミであること
        self.assertEqual('ネズミ', actual['type'])

    def test_not_get(self):
        """
        存在しないIDの場合、データが取得できないこと
        :return:
        """
        actual = architect.extract_user(0)

        # 取得できないこと
        self.assertIsNone(actual)
