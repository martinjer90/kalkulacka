print("Vítej v aplikaci kalkulačka.")
cislo_1=int(input("Zadej první číslo:"))
cislo_2=int(input("Zadej druhé číslo:"))
operator=input("zadej operátor(+,-,/,*)")
while True:
    if operator == "+":
        print(cislo_1+cislo_2)
        break
    elif operator == "-":
        print(cislo_1-cislo_2) 
        break  
    elif operator == "/":
        print(cislo_1/cislo_2)  
        break 
    elif operator == "*":
        print(cislo_1*cislo_2)  
        break 
    else:
        print("Toto není operátor!")
        break