def main():
    text = ("年齢は？")
    if text . isdigit():
        age = int( text )
    if age < 20 :
        plint("未成年")

if __name__ == "__main__":
    main()
    

"""
def main():
    text = input("年齢は？”)
    age = int(text)
    if age < 20:
        print("未成年")
    elif age <= 64 :
        print("成人")
    else :
        print("高齢者")


if __name__ == "__main__":
    main()
"""