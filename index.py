#may need to check first if anything seems odd cause this is what i understood
#ps i may be gon from 2-4pm
x=eval(input("How much money is left?(Format all numbers) $"))

#convert to cents
x=x*100

#base values
Fifty=50
Twenty=20
Ten=10

#conversion to find how many coins is possible
FiftyAMT=int(x/50)
#remaining for to 20 cent
x=x%50

TwentyAMT=int(x/20)
x=x%20

TenAMT=int(x/10)

print(f"you have {FiftyAMT} 50 coins, {TwentyAMT} 20 coins ,{TenAMT} 10 coins")
#note: do we have to make an extra for "if no fifty coins then remaining goes to 20 cent"
