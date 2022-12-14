import phonenumbers
import os
import time
from phonenumbers import carrier, geocoder, timezone

print("#####################################################################################################################################")

print("""
                     .S_sSSs     .S    S.     sSSs_sSSs     .S_sSSs      sSSs    sSSs    sSSs   .S_SSSs     .S_sSSs    
                .SS~YS%%b   .SS    SS.   d%%SP~YS%%b   .SS~YS%%b    d%%SP   d%%SP   d%%SP  .SS~SSSSS   .SS~YS%%b   
                S%S   `S%b  S%S    S%S  d%S'     `S%b  S%S   `S%b  d%S'    d%S'    d%S'    S%S   SSSS  S%S   `S%b  
                S%S    S%S  S%S    S%S  S%S       S%S  S%S    S%S  S%S     S%|     S%S     S%S    S%S  S%S    S%S  
                S%S    d*S  S%S SSSS%S  S&S       S&S  S%S    S&S  S&S     S&S     S&S     S%S SSSS%S  S%S    S&S  
                S&S   .S*S  S&S  SSS&S  S&S       S&S  S&S    S&S  S&S_Ss  Y&Ss    S&S     S&S  SSS%S  S&S    S&S  
                S&S_sdSSS   S&S    S&S  S&S       S&S  S&S    S&S  S&S~SP  `S&&S   S&S     S&S    S&S  S&S    S&S  
                S&S~YSSY    S&S    S&S  S&S       S&S  S&S    S&S  S&S       `S*S  S&S     S&S    S&S  S&S    S&S  
                S*S         S*S    S*S  S*b       d*S  S*S    S*S  S*b        l*S  S*b     S*S    S&S  S*S    S*S  
                S*S         S*S    S*S  S*S.     .S*S  S*S    S*S  S*S.      .S*P  S*S.    S*S    S*S  S*S    S*S  
                S*S         S*S    S*S   SSSbs_sdSSS   S*S    S*S   SSSbs  sSS*S    SSSbs  S*S    S*S  S*S    S*S  
                S*S         SSS    S*S    YSSP~YSSY    S*S    SSS    YSSP  YSS'      YSSP  SSS    S*S  S*S    SSS  
                SP                 SP                  SP                                         SP   SP          
                Y                  Y                   Y                                          Y    Y           
#####################################################################################################################################
""")

print("Phone Scan is a simple tool that allows you to scan Mobile phone numbers\n"
"and display the operators associated with the number\n")

print("-----------------------------------------")
print("1 - China(+86)")
print("2 - United KingDom(+44)")
print("3 - France(+33)")
print("4 - Spain(+34)")
print("5 - Portugu??s(+351)")
print("6 - Brazil(+55)")
print("7 - Germany(+49)")
print("8 - India(+91)")
print("9 - Japan(+81)")
print("10 - Korea(+82)")
print("11 - Poland(+48)")
print("12 - Ukraine(+380)")
print("13 - United State Of America(+1)")
print("14 - Exit")
print("")
print("-----------------------------------------")
print("")
option = input("Please Chose a Phone number :  ")
print("")
print("")

if option == "1":
    print("China")
    print("??????????????????????????????, +86xxx")
    mobileno = input("??????????????????????????????????????? : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "cn"))
    print(geocoder.description_for_number(mobileno, "cn"))
    print("?????????????????????: ", phonenumbers.is_valid_number(mobileno))
    print("clean the screen in 3s")
    t = (3)
    time.sleep(3)
    os.system('clear')
    if mobileno != phonenumbers:
        os.system("exit")

if option == "2":
    print("United KingDom")
    print("you must enter the number with your country code, +44xxx")
    mobileno = input("Enter mobile number : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "en"))
    print(geocoder.description_for_number(mobileno, "en"))
    print("Valid mobile number: ", phonenumbers.is_valid_number(mobileno))
    print("clean the screen in 3s")
    t = (3)
    time.sleep(3)
    os.system('clear')
    if mobileno != phonenumbers:
        os.system("exit")

if option == "3":
    print("France")
    print("il faut saisir le num??ro avec l'indicatif du pays, +33xxx")
    mobileno = input("Entrez le num??ro de t??l??phone portable : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "fr"))
    print(geocoder.description_for_number(mobileno, "fr"))
    print("Num??ro de portable valide: ", phonenumbers.is_valid_number(mobileno))
    print("nettoie l'??cran en 3s")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "4":
    print("Spain")
    print("debes ingresar el n??mero con el c??digo del pa??s, +34xxx")
    mobileno = input("Introduce el n??mero de m??vil : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "es"))
    print(geocoder.description_for_number(mobileno, "es"))
    print("N??mero de m??vil v??lido: ", phonenumbers.is_valid_number(mobileno))
    print("limpia la pantalla en 3s")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "5":
    print("Portugu??s")
    print("voc?? deve digitar o n??mero com o c??digo do pa??s, +34xxx")
    mobileno = input("Digite o n??mero do celular : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "pt"))
    print(geocoder.description_for_number(mobileno, "pt"))
    print("N??mero de celular v??lido: ", phonenumbers.is_valid_number(mobileno))
    print("tela limpa em 3s")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "6":
    print("Brazil")
    print("voc?? deve digitar o n??mero com o c??digo do pa??s, +55xxx")
    mobileno = input("Digite o n??mero do celular : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "br"))
    print(geocoder.description_for_number(mobileno, "br"))
    print("N??mero de celular v??lido: ", phonenumbers.is_valid_number(mobileno))
    print("tela limpa em 3s")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "7":
    print("Germany")
    print("Sie m??ssen die Nummer mit der Landesvorwahl eingeben, +49xxx")
    mobileno = input("Handynummer eingeben : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "de"))
    print(geocoder.description_for_number(mobileno, "de"))
    print("G??ltige Handynummer: ", phonenumbers.is_valid_number(mobileno))
    print("reinigt den Bildschirm in 3s")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "8":
    print("India")
    print("???????????? ???????????? ????????? ????????? ?????? ????????? ???????????? ???????????? ???????????? ????????????, +91xxx")
    mobileno = input("?????????????????? ???????????? ???????????? ???????????? : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "in"))
    print(geocoder.description_for_number(mobileno, "in"))
    print("????????? ?????????????????? ????????????: ", phonenumbers.is_valid_number(mobileno))
    print("3s . ????????? ????????????????????? ?????? ????????? ????????????")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "9":
    print("Japan")
    print("???????????????????????????????????????????????????????????????, +81xxx")
    mobileno = input("????????????????????? : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "jp"))
    print(geocoder.description_for_number(mobileno, "jp"))
    print("???????????????????????????: ", phonenumbers.is_valid_number(mobileno))
    print("3 ?????????????????????????????????")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "10":
    print("Korea")
    print("?????? ????????? ?????? ????????? ???????????? ?????????, +82xxx")
    mobileno = input("????????? ????????? ??????????????? : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "kr"))
    print(geocoder.description_for_number(mobileno, "kr"))
    print("????????? ????????? ??????: ", phonenumbers.is_valid_number(mobileno))
    print("3????????? ?????? ??????")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "11":
    print("Poland")
    print("musisz wpisa?? numer z kodem kraju, +48xxx")
    mobileno = input("Wpisz numer telefonu kom??rkowego : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "pl"))
    print(geocoder.description_for_number(mobileno, "pl"))
    print("Prawid??owy numer telefonu kom??rkowego: ", phonenumbers.is_valid_number(mobileno))
    print("wyczy???? ekran w 3s")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "12":
    print("Ukraine")
    print("?????????????????? ???????????? ?????????? ???? ?????????? ????????????, +380xx")
    mobileno = input("?????????????? ?????????? ???????????????????? ???????????????? : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "ua"))
    print(geocoder.description_for_number(mobileno, "ua"))
    print("?????????????? ?????????? ????????????????????: ", phonenumbers.is_valid_number(mobileno))
    print("???????????????? ?????????? ???? 3 ??????????????")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        print("??????????, ?????????????? ?????????? ???? ?? ?????????????? ????????????????")
    os.system("exit")

if option == "13":
    print("United State of America")
    print("you must enter the number with your country code, +1xxx")
    mobileno = input("Enter mobile number : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "us"))
    print(geocoder.description_for_number(mobileno, "us"))
    print("Valid mobile number: ", phonenumbers.is_valid_number(mobileno))
    print("clean the screen in 3s")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "14":
    print("Exit")
    os.system('clear')
    os.system('exit')












