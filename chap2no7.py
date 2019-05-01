def main():
    text = input("年齢は？")
    if text.isdigit():
        age = int(text)
        if age < 20 :
            print("未成年")
            
if __name__ == "__main__":
    main()