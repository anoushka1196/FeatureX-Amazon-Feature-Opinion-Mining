Asin = []
wc=[]
phonerating = []

def setAsinValue(Value):
    Asin.clear()
    Asin.append(Value)

def getAsinValue():
    return Asin[0]

def setWordCloud(wordcloud):
    #wc.clear()
    wc.append(wordcloud)

def setPhone(rating):
    phonerating.append(rating)

def getPhone():
    len1 = len(phonerating)
    return phonerating[len1-1]

def getWordCloud():
    len1 = len(wc)
    return wc[len1-1]

def getPhoneName(asin):
    import price
    if (asin=='B01LW9P0H4'):
        return 'Moto Z Play'
    elif (asin=='B071WDBTW1'):
        return 'Moto G5'
    elif (asin=='B079SGQNPN'):
        return 'Moto G Play'
    elif (asin=='B079YM4RXS'):
        return 'Moto Z'
    elif (asin=='B06Y137TLR'):
        return 'Samsung Galaxy S8'
    elif (asin=='B06Y15G61T'):
        return 'Samsung Galaxy S8+'
    elif (asin=='B079JSZ1Z2'):
        return 'Samsung Galaxy S9'
    elif (asin=='B01M7O431L'):
        return 'Samsung S7 Edge'
    else:
        nm=price.ReadName(asin)
        if (nm):
            return nm
        else:
            return "--"

def getAsinCompare(name):
    if (name == 'Moto Z Play'):
        return 'B01LW9P0H4'
    elif (name == 'Moto G5'):
        return 'B071WDBTW1'
    elif (name == 'Moto G Play'):
        return 'B079SGQNPN'
    elif (name == 'Moto Z'):
        return 'B079YM4RXS'
    elif (name=='Samsung Galaxy S8'):
        return 'B06Y137TLR'
    elif (name=='Samsung Galaxy S8+'):
        return 'B06Y15G61T'
    elif (name=='Samsung Galaxy S9'):
        return 'B079JSZ1Z2'
    elif (name=='Samsung S7 Edge'):
        return 'B01M7O431L'

##For Analysis
#Feature Relevancy
l =['battery','camera','screen','display','design','processor','memory','size','price','audio','sound','speaker','speed','touch','touchscreen','battery life','shape','card','condition','charger','OS','headphone','performance','cost','software','hardware','mod','stylus','case','video','fingerprint sensor','sensor','fingerprint scanner','bluetooth','connectivity']
def check(feature):
    if feature in l:
        return 'relevant'
    else:
        return 'irrelevant'

###For rating comparision
avg_amazon =[]
avg_product=[]

def set_Ama_avg(asin):
    import csv
    import math
    csv_name = "Datasets/"+asin+"_folder/"+ asin + ".csv"
    mycsv = open(csv_name,"r", encoding="ascii", errors="ignore")
    csv_f = csv.reader(mycsv)
    sum=0
    count =0
    for row in csv_f:
        sum = sum + int(row[5])
        count +=1
    avg = sum/count
    avg_amazon.append(round(avg,2))

def set_Prod_avg(avg):
    avg_product.append(avg)

def get_Prod_avg():
    return avg_product[0]

def get_Amazon_avg():
    return avg_amazon[0]

def getPrice(asin):
    import price
    if (asin=='B01LW9P0H4'):
        return '$337.14'
    elif (asin=='B071WDBTW1'):
        return '$189.99'
    elif (asin=='B079SGQNPN'):
        return '$118.99'
    elif (asin=='B079YM4RXS'):
        return '$279.99'
    elif (asin=='B06Y137TLR'):
        return '$579.00'
    elif (asin=='B06Y15G61T'):
        return '$639.60'
    elif (asin=='B079JSZ1Z2'):
        return '$719.99'
    elif (asin=='B01M7O431L'):
        return '$309.99'
    else:
        cost=price.ReadAsin(asin)
        if(cost):
           return cost
        else:
            return "--"