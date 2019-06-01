def main () :
    def create_mail ( recv , bill ) :
        tmp = """{}様
    PT企画の佐藤です。
    今月の請求額は{}円です。
    """
        msg = tmp . format ( recv , bill )
        print ( msg )


    def add_charge ( bill ) :
        return int ( bill * 1.07 )


if __name__ == ("__main__") :
    main ()