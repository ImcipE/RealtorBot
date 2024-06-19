def create_property(property):
    #attributes = [price, beds, baths, sqft]
    attributes = []
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

    print(price)
    print(beds)
    print(baths)
    print(sqft)