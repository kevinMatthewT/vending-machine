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
HundredDollarsAMT=int(x/10000)
x=x%10000

FiftyDollarsAMT=int(x/5000)
x=x%5000

TwentyDollarsAMT=int(x/2000)
x=x%2000

TenDollarsAMT=int(x/1000)
x=x%1000

FiveDollarsAMT=int(x/500)
x=x%500

OneDollarAMT=int(x/100)
x=x%100

FiftyCentAMT=int(x/50)
x=x%50

TwentyCentAMT=int(x/20)
x=x%20

TenCentAMT=int(x/10)

#print if they exist
print("Your have:")
if HundredDollarsAMT >0:
    print(f"{HundredDollarsAMT} $100 Dollar bills")
else:
    pass

if FiftyDollarsAMT >0:
    print(f"{FiftyDollarsAMT} $50 Dollar bills")
else:
    pass

if  TwentyDollarsAMT>0:
    print(f"{TwentyDollarsAMT} $20 Dollar bills")
else:
    pass

if  TenDollarsAMT>0:
    print(f"{TenDollarsAMT} $10 Dollar bills")
else:
    pass

if  FiveDollarsAMT>0:
    print(f"{FiftyDollarsAMT} $5 Dollar bills")
else:
    pass

if  OneDollarAMT>0:
    print(f"{OneDollarAMT} $1 Dollar bills")
else:
    pass

if  FiftyCentAMT>0:
    print(f"{FiftyCentAMT} 50 Cent coins")
else:
    pass

if  TwentyCentAMT>0:
    print(f"{TwentyCentAMT} 20 Cent coins")
else:
    pass

if  TenCentAMT>0:
    print(f"{TenCentAMT} 10 Cent coins")
else:
    pass
