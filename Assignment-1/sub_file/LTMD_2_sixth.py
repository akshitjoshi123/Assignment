class LTMD_2:
    def ltmd_2():
        unit = int(input("Enter Total Unit : "))
        demand = int(input("Enter Billing Demand KW : "))
        if demand <= 50 :
            unit = unit * (480/100)
        else:
            unit = unit * (500/100)

        if demand <= 50:
            demand = demand * 175
        elif demand > 50 and demand <= 80:
            demand = demand * 230
        else:
            demand = demand * 300
        power_factor = int(input("Enter Power factor in percentage % : "))
        while power_factor not in range(1,101):
                print("Invalid percentage!!\Enter Power factor in percentage % : ")
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

        cate_6_result = unit + demand + pow_fact
        return(cate_6_result)

