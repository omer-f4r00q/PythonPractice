import csv

def inventory_analyzer(file_name):
    try:
        total_value = 0.0
        low_stock_products = []
        
        with open(file_name, "r", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            
            for row in reader:
                try:
                    price = float(row["price"])
                    quantity = int(row["quantity"])
                    value = price*quantity
                    total_value += value
                    if quantity < 10:
                        low_stock_products.append(row["product_name"])
                except ValueError:
                    print(f"WARNING: Skipping bad row due to data error: {row}")
        
    except FileNotFoundError:
        print("csv file not found!")

    else:
        print("---Inventory Analysis---")
        print(f"Total Inventory Value: ${total_value:.2f}")
        print(f"Products with Low Stock (less than 10 units):")
        for product in low_stock_products:
            print(f"-{product}")
        print("------------------------")

    finally:
        print("---Analysis Script Finished.---")
    
if __name__ == "__main__":
    inventory_analyzer("inventory_with_errors.csv")