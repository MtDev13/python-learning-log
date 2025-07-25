#辞書へのデータの追加

print("---カフェのメニューに新しいアイテムを追加する---")

フードメニュー = {
    "パスタ":"サーモンのクリームソース",
    "サンドイッチ":"海老とアボカド",
    "ケーキセット":"選べるケーキとドリンク"
}
print(f"追加前のフードニュー:{フードメニュー}")

#新しいメニュー「日替わりパスタ」を追加する
フードメニュー["日替わりパスタ"] = "きのこの和風ソース"

#「日替わりサンドイッチ」を追加する
フードメニュー["日替わりサンドイッチ"] = "照り焼きチキンと具沢山タルタル"

#「焼きたてアップルパイ」を追加する
フードメニュー["焼きたてアップルパイ"] = "りんごとカスタードのパイ"

#「季節のケーキ」を追加する
フードメニュー["季節のケーキ"] = "瀬戸内レモンチーズケーキ"

print(f"フードメニューを更新しました！:{フードメニュー}")
