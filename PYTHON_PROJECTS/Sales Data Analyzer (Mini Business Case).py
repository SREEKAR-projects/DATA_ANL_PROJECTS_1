print("=== Sales Data Analyzer ===")

sales_input = input("Enter daily sales separated by commas: ")
if not sales_input.strip():
    print("No sales data provided")
    exit()

sales = sales_input.split(",")
sales = [float(s) for s in sales]
