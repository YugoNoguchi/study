def main () :
    text = input ("年齢は？")
    if not text . isdigit () :
        プログラム中断
    age = int (text)
    if age < 20 :
        if age >= 6 and age <=15 :
                print ("義務教育期間中の未成年")
        elif age <=5 :
                print ("幼児")
        else :
                print ("未成年")
    elif age < 65 :
            print ("成人")
    else :
            print ("高齢者")
if __name__ == ("__main__") :
    main()



"""
未成年
(義務教育期間中の未成年)6_15
成人
高齢者
[プログラム中断]
[インデント省略]
上記に挑戦
"""