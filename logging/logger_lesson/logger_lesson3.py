# loggingのフォーマット調整

import logging

# ログレベルをGEBUGに変更
logging.basicConfig(level=logging.DEBUG)

# 従来の出力
logging.info('error {}'.format('outputting error'))
logging.info('warning %s %s' % ('was', 'outputted'))
logging.info('info %s %s', 'test', 'test')