print("1- RGP:Residential Purpose(Up to & Including 15 KW")
print("2- For Hospitals, Schools & Religious Purpose")
print("3- Non-RGP : Low Tension Service for Commercial and Industrial Purpose")
print("4- LTP (AG) : Agriculture Service")
print("5- LTMD-1 : for Residential Purpose(Above 15 KW)")
print("6- LTMD-2 : for commercial Industrial purpose(Above 15 KW)")
print("7- SL: for Street Light")
print("8- LEV : LT- Electric Vehicle Charging Stations")
print("9- TMP- for Temporary Supply(Below 100 kw)")
print("10- HTMD-1 : for High Tension Load(100kw and above)")
print("11- HTMD-2 : for High Tension AMC Pumping Stations")
print("12- HTMD-3 : for Temporary Supply(100 kw and above)")
print("13- EV: HT- Electric Vehicle Charging")
print("14- HTMD - Metro Traction")

categoty = int(input("Select any Category number: "))

#1- RGP:Residential Purpose
if categoty == 1 :
    unit = int(input("Enter Total Unit : "))
    if unit <= 50:
        p1 = unit * (320/100)
        p5 = p1 
    elif (unit > 50) and (unit <= 200):
        p1 = unit  - 50
        p2 = 50 * (320/100)
        p3 = p1 * (395/100)
        p5 = p2+ p3
    else:
        p1 = unit - 200
        p2 = 50 * (320/100)
        p3 = 150 * (395/100)
        p4 = p1 * (500/100)
        p5 = p2 + p3 + p4
    # print(p5)
    print("1 : For Single Phase")
    print("3 : For Three Phase")
    phase = int(input("Enter Phase : "))
    if phase == 1:
        fixed_charge =  25
    elif phase == 3:
        fixed_charge =  65
    else:
        print("You not select valid Phase!")
        exit()

    # print(fixed_charge)
    #BPL : Below Poverty Line
    if unit <= 50:
        e_charg = unit * (150/100)
        e_charg_5 = e_charg 
    elif (unit > 50) and (unit <= 200):
        e_charg = unit  - 50
        e_charg_2 = 50 * (150/100)
        e_charg_3 = e_charg * (395/100)
        e_charg_5 = e_charg_2 + e_charg_3
    else:
        e_charg = unit - 200
        e_charg_2 = 50 * (150/100)
        e_charg_3 = 150 * (395/100)
        e_charg_4 = e_charg * (500/100)
        e_charg_5 = e_charg_2 + e_charg_3 + e_charg_4
    # print(e_charg_5)
    fixed_charge_2 = 5
    cate_1_result = p5 + fixed_charge + e_charg_5 + fixed_charge_2
    print(cate_1_result)


#2- For Hospitals, Schools & Religious Purpose
if categoty == 2 :
    unit = int(input("Enter Total Unit : "))
    if unit <=200 :
        p1 = unit * (410/100)
        p = p1
    else:
        p1 = unit - 200
        p2 = 200 * (410/100)
        p3 = p1 * (480/100)
        p5 = p2+ p3
    print("1 : For Single Phase")
    print("3 : For Three Phase")
    phase = int(input("Enter Phase : "))
    if phase == 1:
        fixed_charge =  30
    elif phase == 3:
        fixed_charge =  70
    else:
        print("You not select valid Phase!")
        exit()
    cate_2_result = p5 + fixed_charge
    print(cate_2_result)

#3- Non-RGP : Low Tension Service for Commercial and Industrial Purpose
if categoty == 3 :
    unit = int(input("Enter Total Unit : "))
    p = unit * (460/100)
    kw = int(input("Enter kilowatt between 0 to 15: "))
    if kw <= 5:
        kw_price = 70
    elif kw > 5 and kw <=15:
        kw_price = 90
    elif kw > 15:
        print("You select invalid number for kilowatt")
        exit()
    cate_3_result = p + kw_price
    print(cate_3_result)

#4- LTP (AG) : Agriculture Service
if categoty == 4 :
    unit = int(input("Enter Total Unit : "))
    unit = unit * (340 / 100)
    bhp = int(input("Enter brake horsepower : "))
    bhp = bhp * 10
    cate_4_result = unit + bhp
    print(cate_4_result)

#5- LTMD-1 : for Residential Purpose(Above 15 KW)
if categoty == 5 :
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
    print(cate_5_result)



#6- LTMD-2 : for commercial Industrial purpose(Above 15 KW)
if categoty == 6 :
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
    print(cate_6_result)


#7- SL: for Street Light
if categoty == 7:
    unit = int(input("Enter Total Unit : "))
    cate_7_result = unit * (430 / 100)
    print(cate_7_result)

#8- LEV : LT- Electric Vehicle Charging Stations
if categoty == 8:
    unit = int(input("Enter Total Unit : "))
    fix_chrg = 25 #Rs. 25/month/installation
    cate_8_result =fix_chrg +  unit * (430 / 100)
    print(cate_8_result)

#9- TMP- for Temporary Supply(Below 100 kw)
if categoty == 9:
    unit = int(input("Enter Total Unit : "))
    unit = unit * (510 / 100)
    fix_chrg = 25 * 30 #Rs. 25/kW/Day
    cate_9_result = unit + fix_chrg
    print(cate_9_result)

#10- HTMD-1 : for High Tension Load(100kw and above)
if categoty == 10:
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
    else:
        print("You select more than 100 %")
        exit()

    if demand <= 300:
        tou_charge = unit * (80/100)
    else:
        tou_charge = unit * (100/100)
    night_time = int(input("Enter total Night unit : "))
    night_time =  night_time * (30/100)
    cate_10_result = p5 + demand + pow_fact + tou_charge + night_time
    print(cate_10_result)


#11- HTMD-2 : for High Tension AMC Pumping Stations
if categoty == 11:
    unit = int(input("Enter Total Unit : "))
    unit = unit * (410/100)
    maximum_demand = 100 
    demand = int(input("Enter Billing Demand KW : "))
    if demand <= maximum_demand:
        demand = demand * 225
    else:
        demand = demand * 285
    
    power_factor = int(input("Enter Power factor in percentage % : "))
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
    print(cate_11_result)


#12- HTMD-3 : for Temporary Supply(100 kw and above)
if categoty == 12:
    unit = int(input("Enter Total Unit : "))
    p1 = unit * (705 / 100)
    maximum_demand = 100 
    demand = int(input("Enter Billing Demand KW : "))
    if demand <= maximum_demand:
        demand = demand * (25*30)
    else:
        demand = demand * (30*30)
    
    power_factor = int(input("Enter Power factor in percentage % : "))
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
    cate_12_result = p1 + demand + pow_fact + tou_charge
    print(cate_12_result)

#13- EV: HT- Electric Vehicle Charging
if categoty == 13:
    unit = int(input("Enter Total Unit : "))
    unit = unit * (410 / 100)
    maximum_demand = 100 
    demand = int(input("Enter Billing Demand KW : "))
    if demand <= maximum_demand:
        demand = demand * 25
    else:
        demand = demand * 50
    cate_13_result = unit + demand
    print(cate_13_result)

#14- HTMD - Metro Traction
if categoty == 14:
    unit = int(input("Enter Total Unit : "))
    p1 = unit * (355 / 100)
    maximum_demand = 100 
    demand = int(input("Enter Billing Demand KW : "))
    if demand <= maximum_demand:
        demand = demand * 335
    else:
        demand = demand * 385
    
    power_factor = int(input("Enter Power factor in percentage % : "))
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
    print(cate_14_result)