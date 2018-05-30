# phytonでアプリケーションログのcsv出力を変更する。
# アプリケーションログ、システムログ等のメッセージ部分がcsv出力で
# 改行コードにより1行1データとならないのを解決する。

import csv
import re
import os

print("処理開始")

# ファイル調整
read_file_path = input("変換したいイベントログ（txt形式またはcsv形式)の絶対パスを入力してください：")

# 出力ファイル加工
dict, ext = os.path.splitext(read_file_path)
write_file_path = dict + "_fileFormat" + ext

# debug
#read_file_path = "E:\\ユーザー\\Documents\\21_プログラム\\phtyon\\application_log.csv"
#write_file_path = "E:\\ユーザー\\Documents\\21_プログラム\\phtyon\\application_log_fileFormat.csv"

# 行頭検索正規表現
expr = '^(重大|警告|詳細|エラー|情報),.*$'
before_line = ""

# 読み込み/書き込みファイルを開く
f = open(read_file_path, 'r', encoding='utf-8')
fw = open(write_file_path, 'w', encoding='utf-8', newline="\r\n")

# 読み込みファイルを１行づつループし、１行の第１列が出力レベルの場合のみ新しいファイルに書き込む
for line in f:
    line_match = re.search(expr, line)
    if line_match is not None:
        # 正規表現にマッチする場合
        fw.write(before_line+'\n')
        before_line = line_match.group()
    else:
        # 正規表現にマッチしない場合
        before_line = before_line + ' ' + line.rstrip('\n')

# 最終行を書き込む
fw.write(before_line+'\n')

# 読み込み/書き込みファイルを閉じる
f.close
fw.close

print(write_file_path+'を出力しました')
print("処理終了")
