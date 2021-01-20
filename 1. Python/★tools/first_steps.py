import os
import glob
import typing


# データフォルダから*.csvと*.xlsxファイルを探し分離、リスト化
def search_files(data_path: str, file_extension: list):
    list_name = []
    for ext in file_extension:
        list_name.append(ext)
        for name in list_name:
            for root, dirname, file in os.walk(data_path):
                name = glob.glob(os.path.join(root, ext))
    print(name)


# カラムチェック

# csvファイルを読み込みconcat

# データ型の変更

#
