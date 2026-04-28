# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]
# Combined list of items using the zip function
combined_list = zip(products, prices, quantities_sold);
# Sorting the combined list using the sorted function
sorted_products = sorted(combined_list);

for full_product_list in sorted_products:
        print(f"Product: {full_product_list[0]}, Price: {full_product_list[1]}, Quantity Sold: {full_product_list[2]}")
    
    
