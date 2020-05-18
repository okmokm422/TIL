# ログをファイルに出力

import logging

# filenameにファイルパスを指定
logging.basicConfig(filename='logfile/logger.log', level=logging.DEBUG)

logging.info('error {}'.format('outputting error'))
logging.info('warning %s %s' % ('was', 'outputted'))
logging.info('info %s %s', 'test', 'test')