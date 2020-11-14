username = input("username : ")
password = input("password : ")
if username == "Member" and password == "1234":
    print("-----Wellcome Member-----")
    print("-----Choose your order-----")
    print("apple    15 THB/piece")
    print("banana   5  THB/piece")
    print("orange   10 THB/piece")
    print("-----Add to cart-----")
    QuantityApple = int(input("Quantity of apple : "))
    QuantityBanana = int(input("Quantity of banana : "))
    QuantityOrange = int(input("Quantity of orange : "))
    PriceApple = 15 * QuantityApple
    PriceBanana = 5 * QuantityBanana
    PriceOrange = 10 * QuantityOrange
    total = PriceApple + PriceBanana + PriceOrange
    print("Total amount : ", total)
else:
    print("!!!you are not allowed!!!")

