def main ()
    import chap4func
    date = [ { "name" : "Yamamoto" , "bill" : "40000" , "crg" : True } , { "name" : "Yoshida" , "bill" : "25000" , "crg" : False } ]
    for rec in date :
        bill = rec [ "bill" ]
        if rec [ "crg" ] :
            bill chap4func.add_charge (bill)
        chap4func.create_mail ( rec[ "name" ] , bill )
if __name__ == ("__main__") :
    main ()