from sub_file.RGP_first import RGP
from sub_file.GLP_second import GPL
from sub_file.non_RGP_third import non_RGP
from sub_file.LTP_fourth import LTP
from sub_file.LTMD_1_fifth import LTMD_1
from sub_file.LTMD_2_sixth import LTMD_2
from sub_file.SL_seventh import SL
from sub_file.LEV_eighth import LEV
from sub_file.TMP_ninth import TMP
from sub_file.HTMD_1_tenth import HTMD_1
from sub_file.HTMD_2_eleventh import HTMD_2
from sub_file.HTMD_3_twelfth import HTMD_3
from sub_file.EV_thirteenth import EV
from sub_file.HTMD_fourteenth import HTMD

class main():
    
    if __name__ == "__main__":

        try:
            print("1- RGP:Residential Purpose(Up to & Including 15 KW\n2- For Hospitals, Schools & Religious Purpose\n3- Non-RGP : Low Tension Service for Commercial and Industrial Purpose\n4- LTP (AG) : Agriculture Service\n5- LTMD-1 : for Residential Purpose(Above 15 KW)\n6- LTMD-2 : for commercial Industrial purpose(Above 15 KW)\n7- SL: for Street Light\n8- LEV : LT- Electric Vehicle Charging Stations\n9- TMP- for Temporary Supply(Below 100 kw)\n10- HTMD-1 : for High Tension Load(100kw and above)\n11- HTMD-2 : for High Tension AMC Pumping Stations\n12- HTMD-3 : for Temporary Supply(100 kw and above)\n13- EV: HT- Electric Vehicle Charging\n14- HTMD - Metro Traction\nChoose number : ")
            i = int(input())
            while i not in range(1,15):
                print("Please select valid number!!!\nChoose number : ")
                i = int(input())

            dict = {
            1: ['RGP','rgp()'],
            2: ['GPL','gpl()'],
            3: ['non_RGP','non_rgp()'],
            4: ['LTP','ltp()'],
            5: ['LTMD_1','ltmd_1()'],
            6: ['LTMD_2','ltmd_2()'],
            7: ['SL','sl()'],
            8: ['LEV','lev()'],
            9: ['TMP','tmp()'],
            10: ['HTMD_1','htmd_1()'],
            11: ['HTMD_2','htmd_2()'],
            12: ['HTMD_3','htmd_3()'],
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