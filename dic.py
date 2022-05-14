cdic = {
'－':'全角ハイフンマイナス',
'-':'半角ハイフンマイナス',
'‐':'全角ハイフン',
'−':'全角マイナス',
'‒':'フィギュアダッシュ',
'—':'全角ダッシュ',
'–':'二分ダッシュ',
'―':'ホリゾンタルバー',
'ー':'全角長音',
'ｰ':'半角長音',
'─':'罫線',
'━':'罫線',
'一':'いち'
}

s=input("Input is ")
while s != "":
    for s_i in s:
        if s_i in cdic:
            print(s_i," is ",cdic[s_i])
        else:
            print(s_i," is not in cdic")
    s=input("Input is ")

