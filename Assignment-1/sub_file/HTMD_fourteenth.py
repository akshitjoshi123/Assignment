class HTMD:
    def htmd():
        unit = int(input("Enter Total Unit : "))
        p1 = unit * (355 / 100)
        maximum_demand = 100 
        demand = int(input("Enter Billing Demand KW : "))
        if demand <= maximum_demand:
            demand = demand * 335
        else:
            demand = demand * 385
        
        power_factor = int(input("Enter Power factor in percentage % : "))
        while power_factor not in range(1,101):
            print("Invalid percentage!!\nEnter Power factor in percentage % : ")
            power_factor = int(input())
        if power_factor <=100:
            if power_factor >=90 and power_factor <95:
                pow_fact = unit * (0.15/100)
                pow_fact = p1 - pow_fact
            elif power_factor > 95:
                pow_fact = unit * (0.27/100)
                pow_fact = p1 - pow_fact
            else:
                pow_fact = unit * (3/100)
                pow_fact = p1 + pow_fact
        else:
            print("You select more than 100 %")
            exit()

        tou_charge = unit * (60/100)
        night_time = int(input("Enter total Night unit : "))
        night_time =  night_time * (30/100)
        cate_14_result = p1 + demand + pow_fact + tou_charge + night_time
        return(cate_14_result)