#辞書からのデータの削除とカウント、一覧の取得

print("---辞書から不要なメニューを削除する(del / pop)---")

フードメニュー = {
    "パスタ":"サーモンのクリームソース",
    "サンドイッチ":"海老とアボカド",
    "ケーキセット":"選べるケーキとドリンク",
    "日替わりパスタ":"きのこの和風ソース",
    "日替わりサンドイッチ":"照り焼きチキンと具沢山タルタル",
    "焼きたてアップルパイ":"りんごとカスタードのパイ",
    "季節のケーキ":"瀬戸内レモンチーズケーキ"
}
print(f"削除前のフードメニュー:{フードメニュー}")

#1.del文を使って削除する
#delは指定したキーとその値をまとめて辞書から削除する

#「日替わりパスタ」を削除する
del フードメニュー["日替わりパスタ"]
print(f"本日の日替わりパスタは終了しました！\n現在のメニュー:{フードメニュー}")

#2.pop()メソッドを使って削除する
#popは指定したキーの要素を削除し、その値を返す

#「日替わりサンドイッチ」を削除して、その内容を確認する
削除されたサンドイッチの内容 = フードメニュー.pop("日替わりサンドイッチ")
print(f"本日の日替わりサンドイッチは終了しました！（不足材料:{削除されたサンドイッチの内容})\n現在のメニュー:{フードメニュー}")

print("\n---辞書にメニューがいくつあるか数える(len)---")

現在のメニュー数 = len(フードメニュー)
print(f"現在注文可能なメニューは、全部で「{現在のメニュー数}個」です！")

print("\n---キーや値だけをまとめて取り出す---")

#キーだけをまとめて取得する(.keys()メソッド)
メニュー名の一覧 = フードメニュー.keys()
print(f"メニュー名の一覧:{メニュー名の一覧}")

#★「dict_keys」をリストに変換
print(f"メニュー名リスト:{list(メニュー名の一覧)}")

#値だけをまとめて取得する(.values()メソッド)
メニュー内容の一覧 = フードメニュー.values()
print(f"メニュー内容の一覧:{メニュー内容の一覧}")

#★「dict_values」をリストに変換
print(f"メニュー内容リスト:{list(メニュー内容の一覧)}")
