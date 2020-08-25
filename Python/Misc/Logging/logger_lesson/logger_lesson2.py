# ログレベルの変更

import logging

# ログレベルをdebugに変更
logging.basicConfig(level=logging.DEBUG)

logging.critical('critilcal')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')