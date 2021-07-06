class RGP():
    def rgp():
        print("1 : RGP : Residential General Purpose \n2 : BPL : Below Poverty Line")
        print("Choose number : ")
        i = int(input())
        while i not in range(1,3):
            print("Please select valid number!!!")
            print("Choose number : ")
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
            # print(p5)
            print("1 : For Single Phase\n2 : For Three Phase")
            phase = int(input("Enter Phase : "))
            while phase not in range(1,3):
                print("Please select valid phase!!!")
                print("Choose Phase : ")
                phase = int(input())
            if phase == 1:
                fixed_charge =  25
            elif phase == 2:
                fixed_charge =  65
            # else:
            #     print("You not select valid Phase!")
            #     exit()
            cate_1_result = p5 + fixed_charge 
            return(cate_1_result)

        # print(fixed_charge)
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