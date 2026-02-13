def sales_analyzer():
    print("=== Sales Data Analyzer ===")

    sales_input = input("Enter daily sales separated by commas: ")

    if not sales_input.strip():
        print("No sales data provided")
        return

    sales = sales_input.split(",")
    sales = [float(s) for s in sales]

    total_sales = sum(sales)
    count_days = len(sales)
    average_sales = total_sales / count_days
    highest_sale = max(sales)
    lowest_sale = min(sales)

    above_avg = len([s for s in sales if s > average_sales])
    below_avg = len([s for s in sales if s < average_sales])

    if average_sales >= 10000:
        performance = "Strong"
    elif average_sales >= 5000:
        performance = "Stable"
    else:
        performance = "Weak"

    print("\n--- Sales Summary Report ---")
    print("Total Days:", count_days)
    print("Total Sales:", total_sales)
    print("Average Daily Sales:", round(average_sales, 2))
    print("Highest Sale:", highest_sale)
    print("Lowest Sale:", lowest_sale)
    print("Days Above Average:", above_avg)
    print("Days Below Average:", below_avg)
    print("Business Performance:", performance)


sales_analyzer()
