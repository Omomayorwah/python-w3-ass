def calculate_discount(price, discount_percent):
    price = float(input("Price: "))
    discount_percent = float(input("Discount (%): "))
    discount = (discount_percent / float(100)) * price
    final_price = price - discount 
    if discount_percent >= 20:
        print("Final Price is: ", final_price)
    else: print("Final Price is: ", price)

calculate_discount(100,20)
    