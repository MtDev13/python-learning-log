#データの基礎

print("---データを入れる「箱」と「中身の種類」---")

#1.文字列(str)という種類のデータを箱に入れる
#「ハンバーグ」という文字を'おかずA'という箱に入れる
おかずA = "ハンバーグ"
おかずB = "マッシュポテト"
print(f"最初のおかずは{おかずA}です。")
print(f"次のおかずは{おかずB}です。")

#2.整数(int)という種類のデータを箱に入れる
#「おかずの個数」という数を'個数'という箱に入れる
個数 = 2
お弁当箱の数 = 1
print(f"おかずの数は{個数}個です。")
print(f"お弁当箱は{お弁当箱の数}個あります。")

#3.浮動小数点(float)という種類のデータを箱に入れる
#「おかずの重さ」という小数点以下の数字を'重さ'という箱に入れる
重さ = 50.5
print(f"おかずの重さは{重さ}グラムです。")

#4.真偽値(bool)という種類のデータを箱に入れる
#「お弁当が完成したか」という状態を'完成'という箱に入れる
完成 = False
具材はあるか = True
print(f"お弁当は完成していますか？{完成}")
print(f"具材はありますか？{具材はあるか}")

print("\n---箱の中身の「種類(データ型)」の確認---")

#Pythonは、箱の中に入っているデータがどんな「種類」なのかを教えてくれる
print(f"'おかずA'の種類は:{type(おかずA)}")
print(f"'個数'の種類は:{type(個数)}")
print(f"'重さ'の種類は:{type(重さ)}")
print(f"'完成'の種類は:{type(完成)}")
