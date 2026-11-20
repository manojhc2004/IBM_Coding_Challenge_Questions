"""1. 
	• Happy Hour Discount: If the purchase time is between 10:00 PM and 11:00 PM (inclusive of 10:00 PM, exclusive of 11:00 PM), a 30% discount is applied to the sum of all item prices.
    
	• Night Owl BOGO Discount: If the purchase time is between 11:00 PM and 12:00 AM (inclusive of 11:00 PM, exclusive of 12:00 AM), a Buy One Get One (BOGO) offer applies only if the cart contains exactly 2 items. Under this offer, the customer is only charged for the highest-priced item (the cheaper item becomes free). If the cart contains fewer than 2 or more than 2 items during this hour, no discount is applied from this rule.
	• If the purchase happens at any other time, no base time-based discount is applied.

2. Value-Based Loyalty Discount (Stackable):
	• After applying any applicable time-based discount from Step 1, if the intermediate bill amount is greater than or equal to ₹1000, a flat discount of ₹100 is deducted. This applies at all times of the day.

3. Logistics & Delivery Fee:
	• If the customer is enrolled as a Prime Member, the delivery fee is ₹0 (Free).
	• If the customer is a Non-Prime Member, a flat delivery fee of ₹40 is added to the final bill after all discounts have been computed.
"""



def ecommerce(prices,times, isprime):

    total = sum(prices)
    N = len(prices)
     
    if ("22:00" <= times <= "23:00"):
        total = round(total * 0.70 )
    
    if ("23:00" <= times <= "23:59"):

        if N == 2:
            total = max(prices)
    
    if (total > 1000):

        total-=100
    
    
    if (isprime == False):
        total+= 40
    

    return total







print(ecommerce([600, 600], "22:30", True))