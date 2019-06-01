def main () :
    def create_mail ( recv , bill ) :
        tmp = """{}様
    PT企画の佐藤です。
    今月の請求額は{}円です。
    """
        msg = tmp . format ( recv , bill )
        print ( msg )


    create_mail ( "山本" , 40000 )    

if __name__ == ("__main__") :
    main ()