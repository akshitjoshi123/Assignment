class LEV:
    def lev():
        unit = int(input("Enter Total Unit : "))
        fix_chrg = 25 #Rs. 25/month/installation
        cate_8_result =fix_chrg +  unit * (430 / 100)
        return(cate_8_result)
