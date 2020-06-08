mport pandas as pd 
import matplotlib.pyplot as plt
print("welcome to DashBoard")
print("\nPress 1 if you want to see single rate and 2 for comparision:")
n = int(input())
if(n == 1):
    print("Enter the Country you Want to See Rates Of:")
    s = str(input())
    s = s + ".xlsx"
    df = pd.read_excel(s)
    loc = s
    date = list(df[df.columns[1]])
    rate = list((df[df.columns[2]]))
    rates= []
    for item in rate:
        rates.append(float(item))
    plt.xlabel("Dates")
    plt.ylabel("Rate")
    plt.plot(date,rates)
    plt.xticks(date[0:-1:999], rotation=25)
    plt.show()
elif (n == 2):
    print("Type the number of currency:")
    n = int(input())
    print("Type the Names:")
    while(n>0):
        n = n - 1
        s = str(input())
        j = s
        s = s + ".xlsx"
        df = pd.read_excel(s)
        loc = s
        date = list(df[df.columns[1]])
        rate = list((df[df.columns[2]]))
        rates = []
        for item in rate:
            rates.append(float(item))
        plt.xlabel("Dates")
        plt.ylabel("Rate")
        plt.plot(date,rates,label = j)
    plt.xticks(date[0:-1:999], rotation=25)
    plt.legend()    
    plt.show()
