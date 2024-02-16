#this program is very not user friendly but it gets the job done

def main():

    priceOfItem = 0
    itemAmount = int(input("Enter the amount of billing items(only postivie numbers):"))
    desiredFinalDiscount = float(input("What is the total after discounts:"))
    nonDiscountableTotal = 0
    discountableTotal = 0

    for i in range(itemAmount):
        priceOfItem = float(input("What is the price of billable item #" + str(i+1) + "before discounts:"))
        discount = input("Is the item discountable?(y/n)")
        discount.lower()

        if discount == "y":
            discountableTotal += priceOfItem
        else:
            nonDiscountableTotal += priceOfItem
        print("=================")

    percentToDiscount = (desiredFinalDiscount - nonDiscountableTotal) / discountableTotal

    print("your estimated discount percent is:", percentToDiscount)


if __name__ == "__main__":
    main()



