
drinks={
    "Water":1,
    "Pepsi":2,
    "Coke":3,
    "Fanta":4,
    "Coffee":5,
}

def getUserDrink(validDrinks):
    while True:
        drinkInput= input("Choose a drink by typing it's name: ")
        if drinkInput in validDrinks:
            return drinkInput
        else:
            print("Invalid drink selection, please input the name as stated")

def getBalance(drinkPrice):
    balance=0
    while drinkPrice > balance:
        try:
            print(f"Price of Drink: RM {drinkPrice}    Current balance: RM {balance}")
            balanceInput= int(input("Insert your notes by typing it's value: "))
            if balanceInput > 0:
                balance+=balanceInput
            else: 
                print("Invalid value, please enter a non-negative and non-zero value")
        except:
            print("Invalid value, please do not use decimals")
    return balance

def getChange(totalBalance, drinkPrice):
    notes= [100,50,20,10,5,1]
    notesIndex=0
    returnNotes=[]
    change= totalBalance - drinkPrice
    print(f"Price of Drink: RM {drinkPrice}    Total Balance: RM {totalBalance}     Total Change: RM {change}")
    while change > 0 :
        if change >= notes[notesIndex]:
            change -= notes[notesIndex]
            returnNotes.append(notes[notesIndex])
        else:
            notesIndex+=1
    return returnNotes

for drink , price in drinks.items():
    print(f"{drink}: RM {price}")

validDrinks=list(drinks.keys())

userDrink=getUserDrink(validDrinks)
totalBalance=getBalance(drinks[userDrink]) 
changeList=getChange(totalBalance, drinks[userDrink])
print(f"returning notes {changeList}")







