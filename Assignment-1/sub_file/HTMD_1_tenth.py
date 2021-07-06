class HTMD_1:
    def htmd_1():
        unit = int(input("Enter Total Unit : "))
        if unit <= 400:
            p1 = unit * (455/100)
            p5 = p1 
        else:
            p1 = unit  - 400
            p2 = 400 * (455/100)
            p3 = p1 * (445/100)
            p5 = p2+ p3
        demand = int(input("Enter Billing Demand KW : "))
        if demand <= 1000:
            demand = demand * 260
        elif demand > 1000:
            demand = demand * 335
        else:
            demand = demand * 385

        power_factor = int(input("Enter Power factor in percentage % : "))
        while power_factor not in range(1,101):
                print("Invalid percentage!!")
                print("Enter Power factor in percentage % : ")
                power_factor = int(input())
        if power_factor <=100:
            if power_factor >=90 and power_factor <95:
                pow_fact = unit * (0.15/100)
                pow_fact = p1 + pow_fact
            elif power_factor > 95:
                pow_fact = unit * (0.27/100)
                pow_fact = p1 + pow_fact
            else:
                pow_fact = unit * (3/100)
                pow_fact = p1 + pow_fact

        if demand <= 300:
            tou_charge = unit * (80/100)
        else:
            tou_charge = unit * (100/100)
        night_time = int(input("Enter total Night unit : "))
        night_time =  night_time * (30/100)
        cate_10_result = p5 + demand + pow_fact + tou_charge + night_time
        return(cate_10_result)