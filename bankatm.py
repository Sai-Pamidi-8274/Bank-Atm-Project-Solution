class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 600000")

    def withdrawl(self,amount):
        new_amount = 600000 - amount
        print("you have withdrawn this much money "+str(amount) +". Your have this much in your remaining balance "+ str(new_amount))


def main():
    Card_number = input("insert your card number:- ")
    pin_number  = input("enter your pin number (or zip code):- ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1.Check Balance   2.Withdraw Money")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount you want to withdraw:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number please")


if __name__ == "__main__":
    main()