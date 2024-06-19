import re
import Property
import calculations
def create_property(property):
    #attributes = [price, beds, baths, sqft]
    price = property.find("div",{"data-testid":"card-price"}).string
    
    bedsli = property.find("li",{"data-testid": re.compile("^property-meta-beds")})
    if not bedsli:
        beds = "--"
    else:
        beds = bedsli.find("span",{"data-testid": "meta-value"}).string

    bathsli = property.find("li",{"data-testid": re.compile("^property-meta-baths")})
    if not bathsli:
        baths = "--"
    else:
        baths = bathsli.find("span",{"data-testid": "meta-value"}).string

    sqftli = property.find("li",{"data-testid": re.compile("^property-meta-sqft")})        
    if not sqftli:
        sqft = "--"
    else:
        sqft = sqftli.find("span",{"data-testid": "meta-value"}).string

    addressdiv1 = property.find("div",{"data-testid": re.compile("^card-address-1")}).string
    addressdiv2 = property.find("div",{"data-testid": re.compile("^card-address-2")}).string
    address = addressdiv1 + " " + addressdiv2

    lotli = property.find("li",{"data-testid": re.compile("^property-meta-lot-size")})
    if not lotli:
        lot = "--"
    else:
        lot = lotli.find("span",{"data-testid": "meta-value"}).string
   
    link = property.find("a",{"href"})
    prop = Property.Property(address,price,beds,baths,sqft,lot,link)
    calculations.calculations(prop)
    
    