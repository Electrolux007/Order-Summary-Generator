# ORDER SUMMARY GENERATOR

# Inquire about product details from customer first 
def collect_and_process_details():
    product_name = input("Product name: ").strip().capitalize()
    review = input ("Product review: ").replace(":)", "🙂").replace(":(", "🙁")
    unit_price = (input ("Product Price in $: "))
    quantity = int(input("Quantity: "))
    discount = input("Discount in %: ")
    weight = input("Weight in KG: ")
    
    # Then process details from customer
    link = product_name.lower().replace(" ", "-")
    subtotal = float(unit_price.removeprefix("$")) * quantity
    discount_to_decimal = float(discount.removesuffix("%"))/100
    discounted_price = subtotal * discount_to_decimal
    shipping = float(weight.lower().removesuffix("kg")) * 4.50
    total = (subtotal - discounted_price) + shipping

    #Now to print the final summary
    print (f"Product: {product_name}")
    print (f"Link: {link}")
    print (f"Review: {review}")
    print (f"Subtotal: ${subtotal:.2f}")
    print (f"Discount: ${discounted_price:.2f}")
    print (f"Shipping: ${shipping:.2f}")
    print (f"Total: ${total:.2f}")
    
collect_and_process_details()
    


