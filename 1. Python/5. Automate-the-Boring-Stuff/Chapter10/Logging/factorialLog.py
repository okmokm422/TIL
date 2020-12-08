import logging

# 情報を保持するLogRrecordオブジェクトの表示方法を指定
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

# basicConfig()のフォーマットに基づいてログを１行出力
logging.debug('プログラム開始')


def factorial(n):
    # ログを１行出力
    logging.debug('factorial({})開始'.format(n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        # ログをn+1回出力
        logging.debug('i = {}, total = {}'.format(i, total))
    logging.debug('factorial({})終了'.format(n))
    return total


print(factorial(5))
logging.debug('プログラム終了')
