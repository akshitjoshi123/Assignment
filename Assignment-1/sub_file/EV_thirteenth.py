class EV:
    def ev():
        unit = int(input("Enter Total Unit : "))
        unit = unit * (410 / 100)
        maximum_demand = 100 
        demand = int(input("Enter Billing Demand KW : "))
        if demand <= maximum_demand:
            demand = demand * 25
        else:
            demand = demand * 50
        cate_13_result = unit + demand
        return(cate_13_result)