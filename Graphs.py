import xlrd
import pandas as pd
import matplotlib.pyplot as plt
print("welcome to DashBoard")
print("\nPress 1 if you want to see single rate and 2 for comparision(Predictions will be shown in both for the next few days):")
n = int(input())
if(n == 1):
    print("Enter the Country you Want to See Rates Of:")
    s = str(input())
    s = s + ".xlsx"
    loc = s
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    a = []
    b = []
    for i in range(1,sheet.nrows):
        if(sheet.cell_value(i,2)!="ND"):
            a.append(sheet.cell_value(i,0))
            b.append(float(sheet.cell_value(i,2)))
    plt.xlabel("Day")
    plt.ylabel("Rate")
    plt.plot(a,b)
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
        loc = s
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        a = []
        b = []
        for i in range(1,sheet.nrows):
            if(sheet.cell_value(i,2)!="ND"):
                a.append(sheet.cell_value(i,0))
                b.append(float(sheet.cell_value(i,2)))
        plt.xlabel("Day")
        plt.ylabel("Rate")
        plt.plot(a,b,label = j)
    plt.legend()    
    plt.show()
