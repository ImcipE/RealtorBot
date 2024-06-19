from xlwt import Workbook
import datetime
class Property:
    listOfProperties = []
    
    def __init__(self,address,price,beds,baths,sqft,lot,link):
        self.address = address
        self.price = price
        self.beds = beds
        self.baths = baths
        self.sqft = sqft
        self.lot = lot
        self.link = link
        
        Property.listOfProperties.append(self)
    
    def setCalculations(self,cashInvested,totalExpenses,rent,netOperatingIncome,mortgage,mortgageInt,annualNOCF,CoC,capRate,recoup):
        
        self.cashInvested = cashInvested
        self.totalExpenses = totalExpenses
        self.rent = rent
        self.netOperatingIncome = netOperatingIncome
        self.mortgage = mortgage
        self.mortgageInt = mortgageInt
        self.annualNOCF = annualNOCF
        self.CoC = CoC
        self.capRate = capRate
        self.recoup = recoup

    @classmethod
    def writeInformation(cls):
        print("total len")
        print(len(cls.listOfProperties))
        

        wb = Workbook()
        sheet1 = wb.add_sheet('Single Family Homes')
        sheet1.write(0,0, 'Address')
        sheet1.write(0,1, 'Price')
        sheet1.write(0,2, 'Beds')
        sheet1.write(0,3, 'Baths')
        sheet1.write(0,4, 'Sqft')
        sheet1.write(0,5, 'Lot')
        sheet1.write(0,6, 'Cash Invested')
        sheet1.write(0,7, 'Total Expenses')
        sheet1.write(0,8, 'Rent')
        sheet1.write(0,9, 'Net Operating Income/mo')
        sheet1.write(0,10, 'Mortgage')
        sheet1.write(0,11, 'Cash Flow/yr')
        sheet1.write(0,12, 'Cash on Cash')
        sheet1.write(0,13, 'Cap Rate')
        sheet1.write(0,14, 'Years to Recoup')
        sheet1.write(0,15, 'Realtor.com Link')

        sheet2 = wb.add_sheet('Multi Family Homes')
        sheet2.write(0,0, 'Address')
        sheet2.write(0,1, 'Price')
        sheet2.write(0,2, 'Beds')
        sheet2.write(0,3, 'Baths')
        sheet2.write(0,4, 'Sqft')
        sheet2.write(0,5, 'Lot')
        sheet2.write(0,6, 'Cash Invested')
        sheet2.write(0,7, 'Total Expenses')
        sheet2.write(0,8, 'Rent')
        sheet2.write(0,9, 'Net Operating Income/mo')
        sheet2.write(0,10, 'Mortgage')
        sheet2.write(0,11, 'Cash Flow/yr')
        sheet2.write(0,12, 'Cash on Cash')
        sheet2.write(0,13, 'Cap Rate')
        sheet2.write(0,14, 'Years to Recoup')
        sheet2.write(0,15, 'Realtor.com Link')
        for i in range(1,len(cls.listOfProperties)+1):
            j=i-1
            sheet2.write(i,0, cls.listOfProperties[j].address)
            sheet2.write(i,1, cls.listOfProperties[j].price)
            sheet2.write(i,2, cls.listOfProperties[j].beds)
            sheet2.write(i,3, cls.listOfProperties[j].baths)
            sheet2.write(i,4, cls.listOfProperties[j].sqft)
            sheet2.write(i,5, cls.listOfProperties[j].lot)
            sheet2.write(i,6, cls.listOfProperties[j].cashInvested)
            sheet2.write(i,7, cls.listOfProperties[j].totalExpenses)
            sheet2.write(i,8, cls.listOfProperties[j].rent)
            sheet2.write(i,9, cls.listOfProperties[j].netOperatingIncome)
            sheet2.write(i,10, cls.listOfProperties[j].mortgageInt)
            sheet2.write(i,11, cls.listOfProperties[j].annualNOCF)
            sheet2.write(i,12, cls.listOfProperties[j].CoC)
            sheet2.write(i,13, cls.listOfProperties[j].capRate)
            sheet2.write(i,14, cls.listOfProperties[j].recoup)
            sheet2.write(i,15, cls.listOfProperties[j].link)
            i+=1
        wb.save('Reports\\report '+str(datetime.date.today())+'.xls' )
    