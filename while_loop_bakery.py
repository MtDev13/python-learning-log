import random

パン棚 = ["食パン","バゲット","サンドイッチ","アップルパイ","揚げたてカレーパン"]

選んだパンのリスト = []
見たパンの数 = 0

print("いらしゃいませ！どのパンになさいますか？（ランダムにパンを選びます！）")

while len(パン棚) > 0:
    選んだパン = random.choice(パン棚)
    見たパンの数 += 1

    
    if 選んだパン == "食パン":
        print(f"[{見たパンの数}個目]あ、{選んだパン}は今日はパスで！次、次！")
        パン棚.remove(選んだパン)
        continue

    選んだパンのリスト.append(選んだパン)
    パン棚.remove(選んだパン)

    if 選んだパン == "揚げたてカレーパン":
        print(f"[{見たパンの数}個目]やった！{選んだパン}だ！これにする！もう他は見なくていいや！")
        break

    else:
         print(f"[{見たパンの数}個目]{選んだパン}がある！これも美味しそう…")

print("\nお会計はこちらです！ありがとうございました！")
print(f"今日選んだパンたち:{選んだパンのリスト}")
