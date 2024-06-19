from mortgage import Loan
from decimal import Decimal
from re import sub

def calculations(prop):
    beds = int(prop.beds)
    rent = 500 * beds
       
    # #Loan Info
    interest= 0.06
    term = 30
    downPaymentPercent = 0.25
    closingCostsPercent = 0.05
    initialRepair = 0
    vacancyRate = .1
    capExRate = 0.07
    maintenanceRate = 0.07
    propertyTaxes = 130
    insurance = 40

    if prop.price.isnumeric():
        price = int(prop.price.strip('$').replace(',',''))
    else:
        price = 100000
    downPayment = round(price * downPaymentPercent,2)
    loanAmount = price - downPayment
    closingCosts = closingCostsPercent * price
    cashInvested = downPayment + initialRepair + closingCosts

    #Monthly Expenses
    vacancy = vacancyRate * rent
    capEx = capExRate * rent
    maintenance = maintenanceRate * rent
    totalExpenses = vacancy + capEx + maintenance + propertyTaxes + insurance

    #Calculations
    netOperatingIncome = rent - totalExpenses
    mortgage = str(Loan(loanAmount, interest, term).monthly_payment)
    mortgageInt = round(int(Decimal(sub(r'[^\d.]','',mortgage))),2)
    netOperatingCashFlow = round(netOperatingIncome - mortgageInt,2)
    annualNOCF = round(netOperatingCashFlow * 12,2)
    CoC = round(annualNOCF / cashInvested * 100,2)
    propValue = round(price + initialRepair,2)
    capRate = round(annualNOCF / propValue * 100,2)
    recoup = round(100 / CoC,2)

    prop.setCalculations(cashInvested,totalExpenses,rent,netOperatingIncome,mortgage,mortgageInt,annualNOCF,CoC,capRate,recoup)
#'Realtor.com Link'
