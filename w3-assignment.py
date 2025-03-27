def calculate_discount(price, discount_percent):
    discount = (discount_percent / 100) * price
    final_price = price - discount
    if discount_percent >= 20:
        print("Final Price is: ", final_price)
    else:
        print("Final Price is: ", price)

price = float(input("Price: "))
discount_percent = float(input("Discount (%): "))
calculate_discount(price, discount_percent)    