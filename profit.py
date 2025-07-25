#Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss?

costprice = int(input("Enter the cost price: "))
sellingprice = int(input("Enter the selling price: "))
if sellingprice > costprice:
    profit = sellingprice - costprice
    print("Profit is", profit)
else:
    print("Loss is", costprice - sellingprice)