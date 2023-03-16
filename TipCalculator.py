#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to tip calculator.")
total_bill=float(input("What was the total bill? $"))
percent=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_count=int(input("How many people to split the bill ? "))
#temp=total_bill*(1+percent/100)
temp=total_bill+(total_bill*(percent/100))
payable=temp/people_count
netpayable="{:.2f}".format(payable)
print(f"Each person should pay: ${netpayable}")