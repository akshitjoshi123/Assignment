class TMP:
    def tmp():
        unit = int(input("Enter Total Unit : "))
        unit = unit * (510 / 100)
        fix_chrg = 25 * 30 #Rs. 25/kW/Day
        cate_9_result = unit + fix_chrg
        return(cate_9_result)
