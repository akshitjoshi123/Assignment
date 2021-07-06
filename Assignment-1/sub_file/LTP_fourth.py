class LTP:
    def ltp():
        unit = int(input("Enter Total Unit : "))
        unit = unit * (340 / 100)
        bhp = int(input("Enter brake horsepower : "))
        bhp = bhp * 10
        cate_4_result = unit + bhp
        return(cate_4_result)