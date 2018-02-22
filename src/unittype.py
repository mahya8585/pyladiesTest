# Unit Testの観点

"""
アトラクション乗車制限チェックシステム
身長を入力し、アトラクションに乗れるか否かを返却する。
117〜195cmの人だけ乗れる。
"""


def raging_spirits(height):
    if 117 <= height and height < 196:
        return '乗れる'
    else:
        return '乗れない'

