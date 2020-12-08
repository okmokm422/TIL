# Tracebackをテキストファイルに書き込む

import traceback

try:
    raise Exception('これはエラーメッセージです。')

except:
    error_file = open('errorInfo.txt', 'w')
    error_file.write(traceback.format_exc())
    error_file.close()
    print('トレースバック情報をerrorInfo.txtに書きました。')
