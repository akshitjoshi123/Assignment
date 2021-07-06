class HTMD_2:
    def htmd_2():
        unit = int(input("Enter Total Unit : "))
        unit = unit * (410/100)
        maximum_demand = 100 
        demand = int(input("Enter Billing Demand KW : "))
        if demand <= maximum_demand:
            demand = demand * 225
        else:
            demand = demand * 285
        
        power_factor = int(input("Enter Power factor in percentage % : "))
        while power_factor not in range(1,101):
                print("Invalid percentage!!")
                print("Enter Power factor in percentage % : ")
                power_factor = int(input())
        if power_factor <=100:
            if power_factor >=90 and power_factor <95:
                pow_fact = unit * (0.15/100)
                pow_fact = unit + pow_fact
            elif power_factor > 95:
                pow_fact = unit * (0.27/100)
                pow_fact = unit + pow_fact
            else:
                pow_fact = unit * (3/100)
                pow_fact = unit + pow_fact

        tou_charge = unit * (60/100)
        night_time = int(input("Enter total Night unit : "))
        night_time =  night_time * (30/100)
        cate_11_result = unit + demand + pow_fact + tou_charge + night_time
        return(cate_11_result)
