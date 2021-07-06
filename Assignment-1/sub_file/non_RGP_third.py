class non_RGP:
    def non_rgp():
        unit = int(input("Enter Total Unit : "))
        p = unit * (460/100)
        kw = int(input("Enter kilowatt between 0 to 15: "))
        while kw not in range(1,16):
                print("you choose more than 15!!")
                print("Enter kilowatt between 0 to 15: ")
                kw = int(input())
        if kw <= 5:
            kw_price = 70
        elif kw > 5 and kw <=15:
            kw_price = 90
        cate_3_result = p + kw_price
        return(cate_3_result)
