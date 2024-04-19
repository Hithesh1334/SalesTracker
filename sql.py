import mysql.connector as sql 
from datetime import date
import pandas as pd

conn = sql.connect(
    host = "localhost",
    user = "root",
    database = "Rfs"
)
c = conn.cursor()
date = date.today()


def updateNetProfit(newDueAmount,newTotalCash):
    c.execute("select * from NetProfit;")
    currNetProfit = c.fetchall()
    currNetProfit = pd.DataFrame(currNetProfit)
    currNetProfit = currNetProfit.iloc[-1][0]

    newNetProfit = ( newTotalCash -newDueAmount )
    c.execute('INSERT INTO netprofit(profitAmt,date) VALUES(%s,%s);',(int(newNetProfit),date))
    conn.commit()


def fetchTotalStockData():
    c.execute("SELECT * FROM totalstock;")
    data = c.fetchall()
    return data

def fetchDueAmountData():
    c.execute("SELECT * FROM dueamount;")
    data = c.fetchall()
    return data

def fetchNetProfit():
    c.execute("SELECT * FROM netprofit;")
    data = c.fetchall()
    return data

def fetchTotalCash():
    c.execute("SELECT * FROM totalcash;")
    data = c.fetchall()
    return data

def fetchPaymentTo():
    c.execute("SELECT * FROM paymentTo;")
    data = c.fetchall()
    return data

def fetchLogData():
    c.execute("SELECT * FROM totalsales;")
    data = c.fetchall()
    # totalCahs = fetchTotalCash()
    # # totalCash = totalCash.iloc[-1][0]
    # newTotalCash = data + totalCash
    # c.execute('INSERT INTO totalcash(cashAmt,date) VALUES(%s,%s);',(int(newTotalCash),date))
    # conn.commit()

    # dueAmount = fetchDueAmountData()
    # dueAmount = pd.DataFrame(dueAmount)
    # dueAmount = dueAmount.iloc[-1][0]

    # newNetProfit = newTotalCash - int(dueAmount)
    # # c.execute('INSERT INTO netprofit(profitamt,date) VALUES(%s,%s);',(int(newTotalCash),date))
    # # conn.commit()

    return data

def addTodaysEntry(entry):
    c.execute('INSERT INTO totalsales(saleAmt,date) VALUES(%s,%s);',(int(entry),date))
    conn.commit()
    

def addOnlinePayment(entry):
    c.execute('INSERT INTO phonepaycash(totalamount,date) VALUES(%s,%s);',(int(entry),date))
    conn.commit()

def addPaymentTo(name,entry):
    c.execute('INSERT INTO paymentto(amountgivento,amountgiven,date) VALUES(%s,%s,%s);',(name,int(entry),date))
    conn.commit()

    #updating dueAmount table
    c.execute("select * from dueamount;")
    dueAmount = c.fetchall()
    dueAmount = pd.DataFrame(dueAmount)
    oldDueAmount = dueAmount.iloc[-1][0]
    newDueAmount = oldDueAmount - int(entry) 
    print(newDueAmount)
    c.execute('INSERT INTO dueamount(dueAmt,date) VALUES(%s,%s);',(int(newDueAmount),date))
    conn.commit()

    #updating totalcash table
    c.execute("select * from totalcash;")
    totalCash = c.fetchall()
    totalCash = pd.DataFrame(totalCash)
    oldtotalCash = totalCash.iloc[-1][0]
    newtotalCash = oldtotalCash - int(entry) 
    print(newtotalCash)
    c.execute('INSERT INTO totalcash(cashAmt,date) VALUES(%s,%s);',(int(newtotalCash),date))
    conn.commit()

    updateNetProfit(newDueAmount,newtotalCash)



def addHomeExpenditure(reason,name,entry):
    c.execute('INSERT INTO exprelatedtohome(reason,givento,amountgiven,date) VALUES(%s,%s,%s,%s);',(reason,name,int(entry),date))
    conn.commit()

def addLoriBhado(name,entry):
    c.execute('INSERT INTO paymentto(amountgivento,amountgiven,date) VALUES(%s,%s,%s);',(name,int(entry),date))
    conn.commit()

def addOtherPayment(name,entry):
    c.execute('INSERT INTO paymentto(amountgivento,amountgiven,date) VALUES(%s,%s,%s);',(name,int(entry),date))
    conn.commit()

