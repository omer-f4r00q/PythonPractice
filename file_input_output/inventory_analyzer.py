import csv

def inventory_analyzer(file_name):
    try:
        total_value = 0.0
        low_stock_products = []
        
        with open(file_name, "r", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            
            for row in reader:
                price = float(row["price"])
                quantity = int(row["quantity"])
                value = price*quantity
                total_value += value
                if quantity < 10:
                    low_stock_products.append(row["product_name"])

        print("---Inventory Analysis---")
        print(f"Total Inventory Value: ${total_value:.2f}")
        print(f"Products with Low Stock (less than 10 units):")
        for product in low_stock_products:
            print(f"-{product}")
        print("------------------------")
        
    except FileNotFoundError:
        print("csv file not found!")

if __name__ == "__main__":
    inventory_analyzer("inventory.csv")