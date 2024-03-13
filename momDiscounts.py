#this program is very not user friendly but it gets the job done

def testPercent(nonDiscountableAmount, discountableItemPrices:list, percent):

    realPercentApplied = 0

    for i in range(len(discountableItemPrices)):

        realPercentApplied += discountableItemPrices[i] * percent

    return realPercentApplied + nonDiscountableAmount

def main():

    
    itemAmount = int(input("Enter the amount of billing items(only postivie numbers):"))
    itemPrices = [0] * itemAmount
    itemDiscountable = [0] * itemAmount
    desiredFinalDiscount = float(input("What is the total after discounts:"))
    amountDiscountableItems = 0
    discountPricelist = []
    nonDiscountableTotal = 0
    discountableTotal = 0

    for i in range(itemAmount):
        priceOfItem = float(input("What is the price of billable item #" + str(i+1) + " before discounts:"))
        discount = input("Is the item discountable?(y/n)")
        discount.lower()

        if discount == "y":
            itemPrices[i] = priceOfItem
            itemDiscountable[i] = True
            discountableTotal += priceOfItem
            discountPricelist.append(priceOfItem)
            amountDiscountableItems += 1
        else:
            itemPrices[i] = priceOfItem
            itemDiscountable[i] = False
            nonDiscountableTotal += priceOfItem
        print("=================")

    percentToDiscount = (desiredFinalDiscount - nonDiscountableTotal) / discountableTotal

    realTotalAfterPercentApplied = testPercent(nonDiscountableTotal, discountPricelist, percentToDiscount)

    l = 0.0
    r = 0.0
    m = None
    

    if realTotalAfterPercentApplied != desiredFinalDiscount:
        if realTotalAfterPercentApplied > desiredFinalDiscount:
            l =  percentToDiscount
            r = (1.0)
        else:
            l = 0.0
            r = percentToDiscount
        
        while l <= r:

            m = r/l

            newTotal = testPercent(nonDiscountableTotal,discountPricelist, m)

            if newTotal == desiredFinalDiscount:
                print("Your percent you need to apply is:", m)
            elif newTotal > desiredFinalDiscount:
                l = m
            else:
                r = m

            print("m atm:", m)

    else:
        print(percentToDiscount)


if __name__ == "__main__":

    main()
    input("Press Enter to exit...")


