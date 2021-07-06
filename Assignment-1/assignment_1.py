from sub_file.subFile import *

class main():
    
    if __name__ == "__main__":

        try:
            print("1- RGP:Residential Purpose(Up to & Including 15 KW\n2- For Hospitals, Schools & Religious Purpose\n3- Non-RGP : Low Tension Service for Commercial and Industrial Purpose\n4- LTP (AG) : Agriculture Service\n5- LTMD-1 : for Residential Purpose(Above 15 KW)\n6- LTMD-2 : for commercial Industrial purpose(Above 15 KW)\n7- LEV : LT- Electric Vehicle Charging Stations\n8- SL: for Street Light\n9- TMP- for Temporary Supply(Below 100 kw)\n10- HTMD-1 : for High Tension Load(100kw and above)\n11- HTMD-2 : for High Tension AMC Pumping Stations\n12- HTMD-3 : for Temporary Supply(100 kw and above)\n13- EV: HT- Electric Vehicle Charging\n14- HTMD - Metro Traction\nChoose number : ")
            i = int(input())
            while i not in range(1,15):
                print("Please select valid number!!!\nChoose number : ")
                i = int(input())

            dict = {
            1: ['RGP','rgp()'],
            2: ['GPL','gpl()'],
            3: ['nonRgp','nonRgp()'],
            4: ['LTP','ltp()'],
            5: ['LTMD1','ltmd1()'],
            6: ['LTMD2','ltmd2()'],
            7: ['LEV','lev()'],
            8: ['SL','sl()'],
            9: ['TMP','tmp()'],
            10: ['HTMD1','htmd1()'],
            11: ['HTMD2','htmd2()'],
            12: ['HTMD3','htmd3()'],
            13: ['EV','ev()'],
            14: ['HTMD','htmd()']
            }
            object = eval(dict[i][0])
            print(eval('object.' + dict[i][1]))

        except ValueError as e:
            print("Opps!!! You select a String!")
        except Exception as e:
            print("Something went Wrong!")

obj = main()