# 基本的に1テスト1観点
# "条件" と "期待値" は1対1になるよう明記する

user = {
    1: {'name': 'Mickey', 'type': 'ネズミ'},
    2: {'name': 'Minnie', 'type': 'ネズミ'},
    3: {'name': 'Daisy', 'type': 'アヒル'}
}


def extract_user(user_id):
    return user[user_id]

