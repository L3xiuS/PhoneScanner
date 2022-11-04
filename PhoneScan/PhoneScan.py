#!/usr/bin/venv python3.10
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
"and display the telephone operators associated with the number\n")

print("-----------------------------------------")
print("1 - China(+86)")
print("2 - United KingDom(+44)")
print("3 - France(+33)")
print("4 - Spain(+34)")
print("5 - Português(+351)")
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
    print("你需要这种类型的号码, +86xxx")
    mobileno = input("输入带有国家代码的手机号码 : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "cn"))
    print(geocoder.description_for_number(mobileno, "cn"))
    print("有效的手机号码: ", phonenumbers.is_valid_number(mobileno))
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
    print("il faut saisir le numéro avec l'indicatif du pays, +33xxx")
    mobileno = input("Entrez le numéro de téléphone portable : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "fr"))
    print(geocoder.description_for_number(mobileno, "fr"))
    print("Numéro de portable valide: ", phonenumbers.is_valid_number(mobileno))
    print("nettoie l'écran en 3s")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "4":
    print("Spain")
    print("debes ingresar el número con el código del país, +34xxx")
    mobileno = input("Introduce el número de móvil : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "es"))
    print(geocoder.description_for_number(mobileno, "es"))
    print("Número de móvil válido: ", phonenumbers.is_valid_number(mobileno))
    print("limpia la pantalla en 3s")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "5":
    print("Português")
    print("você deve digitar o número com o código do país, +34xxx")
    mobileno = input("Digite o número do celular : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "pt"))
    print(geocoder.description_for_number(mobileno, "pt"))
    print("Número de celular válido: ", phonenumbers.is_valid_number(mobileno))
    print("tela limpa em 3s")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "6":
    print("Brazil")
    print("você deve digitar o número com o código do país, +55xxx")
    mobileno = input("Digite o número do celular : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "br"))
    print(geocoder.description_for_number(mobileno, "br"))
    print("Número de celular válido: ", phonenumbers.is_valid_number(mobileno))
    print("tela limpa em 3s")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "7":
    print("Germany")
    print("Sie müssen die Nummer mit der Landesvorwahl eingeben, +49xxx")
    mobileno = input("Handynummer eingeben : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "en"))
    print(geocoder.description_for_number(mobileno, "en"))
    print("Gültige Handynummer: ", phonenumbers.is_valid_number(mobileno))
    print("reinigt den Bildschirm in 3s")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "8":
    print("India")
    print("आपको अपने देश कोड के साथ नंबर दर्ज करना होगा, +91xxx")
    mobileno = input("मोबाइल नंबर दर्ज करें : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "en"))
    print(geocoder.description_for_number(mobileno, "en"))
    print("वैध मोबाइल नंबर: ", phonenumbers.is_valid_number(mobileno))
    print("3s . में स्क्रीन को साफ करें")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "9":
    print("Japan")
    print("国コードを含む番号を入力する必要があります, +81xxx")
    mobileno = input("携帯番号を入力 : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "en"))
    print(geocoder.description_for_number(mobileno, "en"))
    print("有効な携帯電話番号: ", phonenumbers.is_valid_number(mobileno))
    print("3 秒で画面をきれいにする")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "10":
    print("Korea")
    print("국가 코드가 있는 번호를 입력해야 합니다, +82xxx")
    mobileno = input("휴대폰 번호를 입력하세요 : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "en"))
    print(geocoder.description_for_number(mobileno, "en"))
    print("유효한 휴대폰 번호: ", phonenumbers.is_valid_number(mobileno))
    print("3초만에 화면 청소")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "11":
    print("Poland")
    print("musisz wpisać numer z kodem kraju, +48xxx")
    mobileno = input("Wpisz numer telefonu komórkowego : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "en"))
    print(geocoder.description_for_number(mobileno, "en"))
    print("Prawidłowy numer telefonu komórkowego: ", phonenumbers.is_valid_number(mobileno))
    print("wyczyść ekran w 3s")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "12":
    print("Ukraine")
    print("необхідно ввести номер із кодом країни, +380xx")
    mobileno = input("Введіть номер мобільного телефону : ")
    mobileno = phonenumbers.parse(mobileno)
    print(mobileno)
    print(timezone.time_zones_for_number(mobileno))
    print(carrier.name_for_number(mobileno, "en"))
    print(geocoder.description_for_number(mobileno, "en"))
    print("Дійсний номер мобільного: ", phonenumbers.is_valid_number(mobileno))
    print("очистити екран за 3 секунди")
    t = (3)
    time.sleep(3)
    os.system('clear')
    os.system("exit")
    if mobileno != phonenumbers:
        print("Схоже, наданий рядок не є номером телефону")
    os.system("exit")

if option == "13":
    print("United State of America")
    print("you must enter the number with your country code, +1xxx")
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
    os.system("exit")
    if mobileno != phonenumbers:
        os.system("exit")

if option == "14":
    print("Exit")
    os.system('clear')
    os.system('exit')












