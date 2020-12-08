# トレースバックを文字列として受け取る

def spam():
    bacon()


def bacon():
    raise Exception('これはエラーメッセージです。')


spam()
