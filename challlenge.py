def main(): 
    text = input("1or2を入力せよ")
    number = int(text)
    if number == 1 :
        for j in range(0,3) :
            for i in range(0, 3):
                if (j >= i) :
                    print("*",end="")
            print()    

    else:
        print('1以外')





if __name__ == "__main__":
    main()





"""


for j in range(0,3):
    
        for i in range(0,3):
            print("* ",end="")
        print()


print_2
*_1
1
*
**
***
2
  *
 **
***
"""