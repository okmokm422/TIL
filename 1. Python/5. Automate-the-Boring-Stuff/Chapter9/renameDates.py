# 米国式日付のファイル名にマッチする正規表現を作る

import shutil
import os
import re

# Regexオブジェクトを生成
date_pattern = re.compile(r"""^(.*?) # 日付の前の全テキスト
                            ((0|1)?\d)- # 月を表す1,2桁の数字（0 or 1 + 数字）
                            ((0|1|2|3)?\d)- # 日を表す1,2桁の文字（0 or 1 or 2 or 3 + 数字）
                            ((19|20)\d\d) # 年を表す4桁の数字（19 or 20 + 数字2桁）
                            (.*?)$ # 日付の後の全テキスト
                            """, re.VERBOSE)

# カレントディレクトリの全ファイルをループする
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)  # 検索対象文字列：amer_filename

    # 日付のないファイルをスキップする
    if mo == None:
        continue

    # ファイル名を部分分解する
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    # 欧米式の日付ファイル名をつくる
    euro_filename = before_part + day_part + '-' + \
        month_part + '-' + year_part + after_part

    # ファイル名を変更する
    print('Renaming "{}" to "{}"...'.format(amer_filename, euro_filename))
    shutil.move(amer_filename, euro_filename)  # ファイル名を変更、上書きされるので注意
