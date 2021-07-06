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
                print("Please select valid phase!!!")
                print("Choose Phase : ")
                phase = int(input())
        if phase == 1:
            fixed_charge =  30
        elif phase == 2:
            fixed_charge =  70
        
        cate_2_result = p5 + fixed_charge
        return(cate_2_result)
