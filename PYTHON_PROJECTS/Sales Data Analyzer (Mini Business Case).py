print("=== Sales Data Analyzer ===")

sales_input = input("Enter daily sales separated by commas: ")
if not sales_input.strip():
    print("No sales data provided")
    exit()

sales = sales_input.split(",")
sales = [float(s) for s in sales]
total_sales = sum(sales)
count_days = len(sales)
average_sales = total_sales / count_days
highest_sale = max(sales)
lowest_sale = min(sales)
