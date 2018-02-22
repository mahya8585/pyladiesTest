# Unit Testの観点

"""
レイジングスピリッツ制限チェックシステム
身長を入力してもらい、レイジングスピリッツに乗れるか否かを返却する。
117cm未満の場合は乗れない。
196cm以上の場合は乗れない。
"""


def raging_spirits(height):
    if 117 <= height and height < 196:
        return '乗れる'
    else:
        return '乗れない'

