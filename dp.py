weight = float(input('How many pounds does your package weigh? '))

#ground shipping
if weight <= 2:
    gs_price = 20.00 + (weight * 1.50)
elif weight <= 6:
    gs_price = 20.00 + (weight * 3.00)
elif weight <= 10:
    gs_price = 20.00 + (weight * 4.00)
else:
    gs_price = 20.00 + (weight * 4.75)

#ground shipping premium
gsp_price = 125.00

#drone shipping
if weight <= 2:
    ds_price = weight * 4.50
elif weight <= 6:
    ds_price = weight * 9.00
elif weight <= 10:
    ds_price = weight * 12.00
else:
    ds_price = weight * 14.25
ds_price = round(ds_price, 2)

shipping_options = [gs_price, gsp_price, ds_price]
shipping_options.sort() #sorted list of prices

print()

print(f"A package that weighs {weight} pounds will cost: \n${gs_price} with Ground Shipping\n${gsp_price} with Ground Shipping 'Premium'\n${ds_price} with Drone Shipping")

print()

if shipping_options[0] == gs_price:
    method = 'ground shipping'
elif shipping_options[0] == gsp_price:
    method = 'ground shipping premium'
else:
    method = 'drone shipping'


print(f"The cheapest method to ship your item is using {method.title()}. It will cost ${shipping_options[0]}.")