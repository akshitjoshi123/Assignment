#1- RGP:Residential Purpose(Up to & Including 15 KW
class RGP:
    def rgp():
        print("1 : RGP : Residential General Purpose \n2 : BPL : Below Poverty Line\nChoose number : ")
        i = int(input())
        while i not in range(1,3):
            print("Please select valid number!!!\nChoose number : ")
            i = int(input())
        unit = int(input("Enter Total Unit : "))

        if i == 1:
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
            print("1 : For Single Phase\n2 : For Three Phase")
            phase = int(input("Enter Phase : "))
            while phase not in range(1,3):
                print("Please select valid phase!!!\nChoose Phase : ")
                phase = int(input())
            if phase == 1:
                fixed_charge =  25
            elif phase == 2:
                fixed_charge =  65
            cate_1_result = p5 + fixed_charge 
            return(cate_1_result)

        #BPL : Below Poverty Line
        if i == 2:
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
        cate_1_result = e_charg_5 + fixed_charge_2
        return(cate_1_result)


#GLP : General Lighting Purpose
class GPL:
    def gpl():
        unit = int(input("Enter Total Unit : "))
        if unit <=200 :
            p1 = unit * (410/100)
            p5 = p1
        else:
            p1 = unit - 200
            p2 = 200 * (410/100)
            p3 = p1 * (480/100)
            p5 = p2+ p3
        print("1 : For Single Phase\n2 : For Three Phase")
        phase = int(input("Enter Phase : "))
        while phase not in range(1,3):
                print("Please select valid phase!!!\nChoose Phase : ")
                phase = int(input())
        if phase == 1:
            fixed_charge =  30
        elif phase == 2:
            fixed_charge =  70
        
        cate_2_result = p5 + fixed_charge
        return(cate_2_result)

#Non-RGP : Low Tension Service for Commercial and Industrial Purpose
class nonRgp:
    def nonRgp():
        unit = int(input("Enter Total Unit : "))
        p = unit * (460/100)
        kw = int(input("Enter kilowatt between 0 to 15: "))
        while kw not in range(0,16):
                print("you choose more than 15!!\nEnter kilowatt between 0 to 15: ")
                kw = int(input())
        if kw <= 5:
            kw_price = 70
        elif kw > 5 and kw <=15:
            kw_price = 90
        cate_3_result = p + kw_price
        return(cate_3_result)


#LTP (AG) : Agriculture Service
class LTP:
    def ltp():
        unit = int(input("Enter Total Unit : "))
        unit = unit * (340 / 100)
        bhp = int(input("Enter brake horsepower : "))
        bhp = bhp * 10
        cate_4_result = unit + bhp
        return(cate_4_result)


#LTMD-1 : Low Tension Maximum Demand for Residential Purpose
class LTMD1:
    def ltmd1():
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
                print("Invalid percentage!!\nEnter Power factor in percentage % : ")
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


#LTMD-2 : Low Tension Maximum Demand for other than residential purpose
class LTMD2:
    def ltmd2():
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


#LEV : LT- Electric Vehicle Charging Stations
class LEV:
    def lev():
        unit = int(input("Enter Total Unit : "))
        fix_chrg = 25 #Rs. 25/month/installation
        cate_7_result =fix_chrg +  unit * (430 / 100)
        return(cate_7_result)


#SL : Low Tension Tension Street Light Service
class SL:
    def sl():
        unit = int(input("Enter Total Unit : "))
        cate_8_result = unit * (430 / 100)
        return(cate_8_result)


#TMP : Low Tension Temporary Supply 
class TMP:
    def tmp():
        unit = int(input("Enter Total Unit : "))
        unit = unit * (510 / 100)
        fix_chrg = 25 * 30 #Rs. 25/kW/Day
        cate_9_result = unit + fix_chrg
        return(cate_9_result)

#HTMD-1 : High Tension Maximum Demand
class HTMD1:
    def htmd1():
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
                print("Invalid percentage!!\nEnter Power factor in percentage % : ")
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

#HTMD-2 : High Tension Water and Sewage Pumping Stations run by AMC
class HTMD2:
    def htmd2():
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
                print("Invalid percentage!!\nEnter Power factor in percentage % : ")
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

#HTMD-3 : High Tension Maximum Demand Temporary Supply
class HTMD3:
    def htmd3():
        unit = int(input("Enter Total Unit : "))
        p1 = unit * (705 / 100)
        maximum_demand = 100 
        demand = int(input("Enter Billing Demand KW : "))
        if demand <= maximum_demand:
            demand = demand * (25*30)
        else:
            demand = demand * (30*30)
        
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
        cate_12_result = p1 + demand + pow_fact + tou_charge
        return(cate_12_result)

#Electric vehicle charging
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


#HTMD Metro Traction
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