import mon_module_de_stckg
import datetime
andro_androany = datetime.date.today()
print("VOLA SISA: {}".format(mon_module_de_stckg.vola_sisa))
# with open("variable_p.txt", "r") as file_r:
#     contenue = file_r.read()
#     print(contenue)
#     file_r.close()

safidy = ""
vola_ampiassaina = 0
vola_sisa = 0  
vola_ananana = float(input("Ampidiro ny vola ananao: "))
    
while safidy != "tsia":
    vola_ampiassaina = float(input("Ampidiro ny vola ilainao: "))
    antony = input("Ampidiro ny antony ilanao vola: ")
    vola_sisa = vola_ananana - vola_ampiassaina
    safidy = input("Mbola hampiasa vola ve enao(eny/tsia)?: ")
    with open("fandaniana.txt", "a+") as file:
        file.write("Date: {} | Vola ananako: {} | Vola sisa: {} \n".format(andro_androany, vola_ananana, vola_sisa))
        file.write("Motif: {} \n".format(antony))
        file.write("\n")
        file.close()
    
with open("mon_module_de_stckg.py", "w+") as file_s_variable:
     file_s_variable.write("vola_sisa = {}".format(vola_sisa))
     file_s_variable.close()