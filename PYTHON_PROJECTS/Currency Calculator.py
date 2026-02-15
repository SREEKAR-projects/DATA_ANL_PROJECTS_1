import requests

def get_live_rate(base_currency, target_currency):
    """Fetches the real-time exchange rate from a public API."""
    # Updated URL to the standard open-access endpoint format
    url = f"https://api.exchangerate-api.com{base_currency}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        
        # Get the rate for our target currency from the rates dictionary
        return data["rates"].get(target_currency)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    print("--- Real-Time Currency Converter ---")
    
    try:
        from_curr = input("Enter base currency (e.g., USD): ").upper()
        to_curr = input("Enter target currency (e.g., EUR): ").upper()
        amount = float(input(f"Enter amount in {from_curr}: "))

        # Fetch dynamic rate
        rate = get_live_rate(from_curr, to_curr)

        if rate:
            converted_amount = amount * rate
            print(f"\n[LIVE RATE] 1 {from_curr} = {rate} {to_curr}")
            print(f"{amount} {from_curr} is equivalent to {converted_amount:.2f} {to_curr}")
        else:
            print(f"Could not find exchange rate for {to_curr}.")
            
    except ValueError:
        print("Invalid input. Please enter a numerical value for the amount.")

if __name__ == "__main__":
    main()
