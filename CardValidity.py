from datetime import datetime
def validCardNo(cardNo):
    nVal = 0
    isSecond = False
    for i in range(len(cardNo) - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
        if isSecond:
            d = d * 2
        nVal += (d//10) + (d%10)
        isSecond = not isSecond
    if (nVal % 10 == 0):
        print("Valid Card Number")
        return True
    else:
        print("Invalid Card Number")
        return False

def validName(name):
    if len(name)<=32 and all(map(lambda x: x.lower().isalpha(), name.split())):
        print("Valid Name")
        return True
    else:
        print("Invalid Name")
        return False

def validCVV(cvv):
    if len(cvv)==3 and int(cvv) in range(1,1000):
        print("Valid CVV")
        return True
    else:
        print("Invalid CVV")
        return False

def validDate(date):
    try:
        expMonth, expYear = map(int, date.split("/"))
    except:
        print("Invalid date")
        return False
    today = datetime.now()
    month = today.month
    year = today.year%100
    if expYear>year or (expYear == year and expMonth >= month):
        print("Valid Date")
        return True
    else:
        print("Expired Date")
        return False

def check(cardNo, date, cvv, name):
    if all( [ validCardNo(cardNo), validName(name), validCVV(cvv), validDate(date) ] ):
        print("Valid Card")
        return True
    else:
        print("Invalid Card")
        return False

if __name__ == "__main__":
    print("Card1:",)
    check("4016870202644910", "06/21", "451", "Ramu Yadav")
    print("Card2:",)
    check("4016870202644912", "06/21", "451", "Ramu Yadav")
