def main():
    # Hardcoded exchange rate for Commit 1 (e.g., 1 USD to 0.92 EUR)
    USD_TO_EUR_RATE = 0.92
    
    print("--- Simple Currency Converter (MVP) ---")
    
    try:
        amount = float(input("Enter amount in USD: "))
        
        # Core Math Logic
        converted_amount = amount * USD_TO_EUR_RATE
        
        print(f"\n[Fixed Rate] 1 USD = {USD_TO_EUR_RATE} EUR")
        print(f"{amount} USD is equivalent to {converted_amount:.2f} EUR")
        
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    main()
