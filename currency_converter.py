def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount > 0:
                return amount
            else:
                raise ValueError()
        except ValueError:
            print("Invalid amount")


def get_currency(label):
    currencies = ('USD', 'EUR', 'CAD')
    while True:
        currency = input(f"Select {label} currency (USD/EUR/CAD): ").upper()
        if currency not in currencies:
            print("Invalid currency")
        else:
            return currency

def convert(amount,source_currency, target_currency):
    exchange_rates = {
        'USD': {'EUR':0.09, 'CAD':1.35},
        'EUR': {'USD':1.12, 'CAD':1.5},
        'CAD': {'USD':0.74, 'EUR':0.67},
    }
    if source_currency == target_currency:
        return amount

    return amount *exchange_rates[source_currency][target_currency]

def main():
    amount = get_amount()
    source_currency = get_currency('source')
    target_currency = get_currency('target')
    converted_amount = convert(amount,source_currency,target_currency)
    print(f'{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency} ')

if __name__ == "__main__":
    main()


