#Cashier

#products
bread_types = { "taftoon": 2, "sangak": 3, "garlic bread": 4, "pita": 3, "barbari": 3

}

basket = []
total = []


clients_answer = input((f"Hi and welcome to Super Tehran.\nHere we have many delicious types of bread. Here are your options and the prices {bread_types}\n what would you like to buy today?  "))

while clients_answer != "thats it":
    if clients_answer in bread_types:
        basket.append(clients_answer)
        clients_answer = input("Okay i will add that to your basket, is their anything else you would like to buy? "
              "Type 'thats it' to end   ").lower()

    else: #if items not available
        clients_answer =  input("sorry we do not have that in are store, is their anything else you would like to buy: "
        "Type 'thats it' to end   ").lower()


print(f"Okay you have {basket} in your basket ")

clients_answer = input("Is the ir anything else you would like to buy: ")

while clients_answer != "thats it":
    if clients_answer in bread_types:
        basket.append(clients_answer)
        clients_answer = input("Okay i will add that to your basket, is their anything else you would like to buy? "
              "Type 'thats it' to end   ").lower()

#order total
for items in basket:
    total.append(bread_types[items])
amount_to_pay = sum(total)

print(f"okay your total is {amount_to_pay}")

