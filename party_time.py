"""
Cheeky Smiles owns a party hosting company and wants to create a more efficient way to charge customers for hosting parties. Cheeky Smiles has decided to write a python algorithm that can automatically give customers prices. 
The party price starts at $100 for the basic package. The customers can pay extra for any addons.  

Addons Price List:
Bouncy House (bh): $50
Slip & Slide (ss): $40
Yard Sign (ys): $35
Pizza (p): $10 per pizza
Burger (b): $2 per burger
Soda (s): $.50 per soda
Cake (c): $15
Cupcakes (cc): $.25 per cupcake

"""

def party_price(addons):
    base_price = 100
    price = base_price

    if "bh" in addons:
        price = price + 50

    if "ss" in addons:
        price = price + 40

    if "ys" in addons:
        price = price + 35

    if "p" in addons:
        for p in addons:
            price = price + 10

    if "b" in addons:
        for b in addons:
            price = price + 2

    if "s" in addons:
        for s in addons:
            price = price + .5

    if "c" in addons:
        price = price + 15

    if "cc" in addons:
        for cc in addons:
            price = price + .25

     price = "{:.2f}".format(price)

    printed_price = "The total price is $" + str(price) + "."
    
    return printed_price
