# Assignment 9 day 13 (24.02.25) 
# Design a python program of minimum 100 LOC for implementing a suuper market and also with GST calculation.

# Supermarket Billing System with GST Calculation

# def display_products(products):
#     print("\nAvailable Products:")
#     print("{:<10} {:<20} {:<10} {:<10}".format("Code", "Name", "Price", "GST%"))
#     print("-" * 50)
#     for code, details in products.items():
#         print("{:<10} {:<20} {:<10.2f} {:<10}".format(code, details['name'], details['price'], details['gst']))

# def calculate_bill(cart, products):
#     subtotal = 0
#     gst_total = 0
#     print("\nBilling Details:")
#     print("{:<20} {:<10} {:<10} {:<10}".format("Product", "Qty", "Price", "GST Amt"))
#     print("-" * 50)
#     for code, qty in cart.items():
#         product = products[code]
#         price = float(product['price']) * qty
#         gst_amount = (float(product['gst']) / 100) * price
#         subtotal += price
#         gst_total += gst_amount
#         print("{:<20} {:<10} {:<10.2f} {:<10.2f}".format(product['name'], qty, price, gst_amount))
    
#     total = subtotal + gst_total
#     print("-" * 50)
#     print(f"Subtotal: Rs. {subtotal:.2f}")
#     print(f"GST Total: Rs. {gst_total:.2f}")
#     print(f"Grand Total: Rs. {total:.2f}\n")

# def add_more_products(products):
#     while True:
#         choice = input("Do you want to add more products? (yes/no): ")
#         if choice.lower() == 'no':
#             break
#         code = input("Enter new product code: ")
#         name = input("Enter product name: ")
#         price = input("Enter product price: ")
#         gst = input("Enter GST percentage: ")
#         if not price.replace('.', '', 1).isdigit() or not gst.replace('.', '', 1).isdigit():
#             print("Invalid input! Price and GST should be numbers.")
#             continue
#         products[code] = {'name': name, 'price': float(price), 'gst': float(gst)}
#         print("Product added successfully!")

# def main():
#     products = {
#         '101': {'name': 'Rice', 'price': 50, 'gst': 5},
#         '102': {'name': 'Milk', 'price': 30, 'gst': 5},
#         '103': {'name': 'Sugar', 'price': 40, 'gst': 5},
#         '104': {'name': 'Soap', 'price': 25, 'gst': 18},
#         '105': {'name': 'Toothpaste', 'price': 55, 'gst': 12},
#         '106': {'name': 'Shampoo', 'price': 120, 'gst': 18},
#         '107': {'name': 'Biscuits', 'price': 35, 'gst': 5},
#         '108': {'name': 'Tea Powder', 'price': 150, 'gst': 5},
#         '109': {'name': 'Cooking Oil', 'price': 200, 'gst': 12},
#         '110': {'name': 'Detergent', 'price': 90, 'gst': 18}
#     }
#     add_more_products(products)
#     cart = {}
#     while True:
#         display_products(products)
#         code = input("Enter product code to add to cart (or 'done' to finish): ")
#         if code.lower() == 'done':
#             break
#         if code in products:
#             qty = input(f"Enter quantity for {products[code]['name']}: ")
#             if not qty.isdigit():
#                 print("Invalid input! Quantity should be a number.")
#                 continue
#             qty = int(qty)
#             if code in cart:
#                 cart[code] += qty
#             else:
#                 cart[code] = qty
#         else:
#             print("Invalid product code. Try again!")
    
#     if cart:
#         calculate_bill(cart, products)
#     else:
#         print("Cart is empty. No items purchased.")

# if __name__ == "__main__":
#     main()













































# Supermarket Billing System with GST Calculation

def display_products(products):
    print("\nAvailable Products:")
    print("{:<10} {:<20} {:<10} {:<10}".format("Code", "Name", "Price", "GST%"))
    print("-" * 50)
    for code, details in products.items():
        print("{:<10} {:<20} {:<10.2f} {:<10}".format(code, details['name'], details['price'], details['gst']))

def calculate_bill(cart, products):
    subtotal = 0
    gst_total = 0
    print("\nBilling Details:")
    print("{:<20} {:<10} {:<10} {:<10}".format("Product", "Qty", "Price", "GST Amt"))
    print("-" * 50)
    for code, qty in cart.items():
        product = products[code]
        price = float(product['price']) * qty
        gst_amount = (float(product['gst']) / 100) * price
        subtotal += price
        gst_total += gst_amount
        print("{:<20} {:<10} {:<10.2f} {:<10.2f}".format(product['name'], qty, price, gst_amount))
    
    total = subtotal + gst_total
    print("-" * 50)
    print(f"Subtotal: Rs. {subtotal:.2f}")
    print(f"GST Total: Rs. {gst_total:.2f}")
    print(f"Grand Total: Rs. {total:.2f}\n")

def add_more_products(products):
    while True:
        choice = input("Do you want to add more products? (yes/no): ")
        if choice.lower() == 'no':
            break
        code = input("Enter new product code: ")
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        gst = input("Enter GST percentage: ")
        if not price.replace('.', '', 1).isdigit() or not gst.replace('.', '', 1).isdigit():
            print("Invalid input! Price and GST should be numbers.")
            continue
        products[code] = {'name': name, 'price': float(price), 'gst': float(gst)}
        print("Product added successfully!")

def main():
    products = {
        '101': {'name': 'Rice', 'price': 50, 'gst': 5},
        '102': {'name': 'Milk', 'price': 30, 'gst': 5},
        '103': {'name': 'Sugar', 'price': 40, 'gst': 5},
        '104': {'name': 'Soap', 'price': 25, 'gst': 18},
        '105': {'name': 'Toothpaste', 'price': 55, 'gst': 12},
        '106': {'name': 'Shampoo', 'price': 120, 'gst': 18},
        '107': {'name': 'Biscuits', 'price': 35, 'gst': 5},
        '108': {'name': 'Tea Powder', 'price': 150, 'gst': 5},
        '109': {'name': 'Cooking Oil', 'price': 200, 'gst': 12},
        '110': {'name': 'Detergent', 'price': 90, 'gst': 18}
    }
    add_more_products(products)
    cart = {}
    while True:
        display_products(products)
        code = input("Enter product code to add to cart (or 'done' to finish): ")
        if code.lower() == 'done':
            break
        if code in products:
            while True:
                qty = input(f"Enter quantity for {products[code]['name']}: ")
                if qty.isdigit() and int(qty) > 0:
                    qty = int(qty)
                    break
                else:
                    print("Invalid input! Quantity should be a positive number.")
            if code in cart:
                cart[code] += qty
            else:
                cart[code] = qty
        else:
            print("Invalid product code. Try again!")
    
    if cart:
        calculate_bill(cart, products)
    else:
        print("Cart is empty. No items purchased.")

if __name__ == "__main__":
    main()
