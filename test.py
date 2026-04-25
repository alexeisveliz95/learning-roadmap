def apply_discount(price, discount):
    if not isinstance(price, int) or not isinstance(price, float):
        return "The price should be a number"

    elif not isinstance(discount, int) or not isinstance(discount, float):
        return "The discount should be a number"

    elif price <= 0:
        return "The price should be greater than 0"

    elif discount <= 0 or discount > 100:
        return "The discount should be between 0 and 100"
        
    else:
        return price - (price * discount / 100)
    
apply_discount(5, "4")