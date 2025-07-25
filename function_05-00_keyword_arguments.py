#キーワード引数

#デフォルト引数を使った献立関数を「キーワード引数」でも使えるようにする
def decide_todays_menu_with_keyword(main_dish,side_dish,soup="味噌汁"):
    
    print(f"\n今日の献立が決定しました！")
    print(f"    - メイン:{main_dish}")
    print(f"    - 副菜:{side_dish}")
    print(f"    - 汁物:{soup}")

    menu_summary = f"【メイン:{main_dish} / 副菜:{side_dish} / 汁物:{soup}】"
    return menu_summary

#--------------------------------------------------
#実際の動作パターン
#--------------------------------------------------

print("---献立パターンA(順番通り、普通の呼び出し)---")
献立A = decide_todays_menu_with_keyword("鶏の唐揚げ","キャベツの千切り","味噌汁")
print(f"→献立Aの概要:{献立A}")

print(f"\n---献立パターンB(★キーワード引数で順番をバラバラに！)---")
献立B = decide_todays_menu_with_keyword(side_dish="福神漬け",soup="ラッシー",main_dish="カレー") #引数の名前を使って値を渡す
print(f"→献立Bの概要:{献立B}")

print(f"---献立パターンc(★デフォルト引数とキーワード引数を組み合わせる！)---")
献立C = decide_todays_menu_with_keyword(side_dish="ほうれん草のおひたし",main_dish="サバの味噌煮")
print(f"→献立Cの概要:{献立C}")
