menu = {
    "Dosa": 50,
    "Cold Coffee": 40,
    "Noodles": 60 ,
    "Maggi":60 ,
    "Coffee": 30,
    "Pizza ": 80,
    "Vada Pav ": 20,
    "Pava bhaji ":100
}

print("\n Welcome to HIGHWAY Cafeee")

print("menu card :\n")
for item in menu:
    print(item.title(), "-RS", menu[item])

    total = 0
    order = 0

    while True:
        food = input("\n Enter item name:").lower()

        if food in menu:

            quty = int (input("Enter the Quentity :"))

            price = menu [food] * quty
            total += price
        
        if food in order:

            order [food] = order [food] + quty

        else:
            order[food] = quty

            print("\n Item added Successfully ")
            print("price = RS ", price)

        more = input("\n Do you want to order more ? (yes/no) :").lower()
        if more != "yes":
            break

print("\n Your Order :")
for item in order:
    print(item.title(), "-", order[item], "quantity")

print("\n Total Amount = RS ", total)