class LTMD_1:
    def ltmd_1():
        unit = int(input("Enter Total Unit : "))
        demand = int(input("Enter Billing Demand KW : "))
        if demand <= 50 :
            unit = unit * (465/100)
        else:
            unit = unit * (480/100)

        if demand <= 50:
            demand = demand * 150
        elif demand > 50 and demand <= 80:
            demand = demand * 185
        else:
            demand = demand * 245
        
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

        cate_5_result = unit + demand + pow_fact
        return(cate_5_result)
