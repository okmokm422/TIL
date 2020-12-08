# フォルダ全体を連番付きZIPファイルにコピーする

import zipfile
import os


def backup_to_zip(folder):

    folder = os.path.abspath(folder)  # folderを絶対パスにする

    # 既存のファイル名からファイル名の連番を決める
    number = 1
    while True:
        # 絶対パスの最後のパス区切り記号より後ろ(=フォルダ名)_number.zip
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    # zipファイルを作成する
    print('Creating {}...'.format(zip_filename))
    # *.zipファイルを文字列として渡し、ZipFileオブジェクトを作成する
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # フォルダのツリーを渡り歩いてその中のファイルを圧縮する
    for foldername, subfolder, filenames in os.walk(folder):
        print('Adding files in {}...'.format(foldername))
        # 現在のフォルダをZIPファイルに追加する
        backup_zip.write(foldername)
        # 現在のフォルダの中の全ファイルをZIPファイルに追加する
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()
