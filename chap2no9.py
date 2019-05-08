def main () :
    text = input ("年齢は？")
    if text . isdigit () :
        age = int (text)
        if age < 20 :
            print ("未成年")
        elif age < 65 :
            print ("成人")
        else :
            print ("高齢者")

if __name__ == ("__main__") :
    main()



"""
未成年
(義務教育期間中の未成年)
成人
高齢者
"""