def main ():
    text = input("年齢は？")
    age = int (text)
    if age <= 5 or age >= 65 :
        print("幼児もしくは高齢者")
if __name__ == "__main__":
    main()