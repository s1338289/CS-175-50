#CS-175
#VictorDavidson
#Stocks


commisionRatePurchase = float(input("Enter comission Rate on Purchase: "))
commisionRateSale = float(input("Enter comission Rate on sale: "))
numsharespurchased =int(input("Enter number of shares purchased: "))
numsharessold = int(input("Enter number of shares sold: "))
pricepershare = float(input(" Enter purchase price per share: "))
sellpriceforshare = float(input("Enter sell price per share "))

amountpaidForStock = numsharespurchased * pricepershare
purchaseComission = amountpaidForStock * commisionRatePurchase
totalpaid = amountpaidForStock + purchaseComission
stockSoldFor = numsharespurchased * sellpriceforshare
sellingCommision = commisionRatePurchase * stockSoldFor
totalReceived = stockSoldFor - sellingCommision
profitOrLoss = totalReceived - totalpaid
            
print("Amount paid for stock: $", amountpaidForStock)
print("Commission paid on the purchase: $", purchaseComission)
print("Amount the stock sold for: $",stockSoldFor)
print("Commission paid on the sale: $",sellingCommision)
print ("Profit (or loss if negative): $", profitOrLoss)
                        
