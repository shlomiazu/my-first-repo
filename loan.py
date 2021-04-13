# det the loan deatils 
money_owed = float(input("how much money do you owe, in ILS?\n")) #50000
apr = float(input("what is the annual percentage rate?\n")) #3%
payment = float(input("What will yoyr montly payment be , in ILS?\n")) #1000
months = int(input("how many months do you want to see result for ?\n")) #24

#divide apr by 100 to make is a orecent ' then divide by 12 to make it monthly
monthly_rate = apr/100/12

for i in range(months):
   #add in  interest
   interest_paid = money_owed * monthly_rate
   money_owed = money_owed + interest_paid

   if (money_owed - payment < 0):
     print("the last payment is", money_owed)
     print("you paid off loan in", i+1, "months")
     break

  # make payment 
   money_owed = money_owed - payment

  # prinyt the result after this month
   print("paid", payment, "of which", interest_paid, "was interest.", end= ' ')
   print("now i owe", money_owed)