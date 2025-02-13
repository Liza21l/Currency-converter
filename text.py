from colorama import init, Fore, Style 

init()

wallet = {"USD": 1000, "EUR": 50, "UAH": 5000}
curse_currency = {
    "USD/EUR": 0.85,
    "EUR/USD": 1.18,
    "USD/UAH": 41.79,
    "UAH/USD": 0.023,
    "EUR/UAH": 32.3,
    "UAH/EUR": 0.031,
    "PLN/UAH": 10.05,
    "UAH/PLN": 0.093,
    "PLN/USD": 0.23,
    "USD/PLN": 3.88 
}

def convert(amount, from_currency, to_currency):
    key = from_currency.upper() + "/" + to_currency.upper()
    if key in curse_currency:
        return amount * curse_currency[key]
    else:
        return None

def Balance(currency):
    if currency in wallet:
        print(wallet[currency])
    else: 
        print(f"Такої валюти не знайдено, ось весь гаманець: {wallet}")

# поповнюємо гаманець
def replenish_wallet(currency, amount):
    if currency in wallet:
        wallet[currency] += float(amount)
        print(wallet)
    else:
        wallet[currency] = float(amount)
        print(wallet)

# зняти кошти 
def withdrawal_funds(currency, amount):
    if currency in wallet and wallet[currency] >= float(amount):
        wallet[currency] -= float(amount)
        return True
    else:
        print("Недостатньо коштів або у вас немає цієї валюти")
        return False

# курс валюти на даний момент
def curse():
    for currency in curse_currency:
        print(currency, ":", curse_currency[currency])

while True:
    print("____Purr-Currency🐾💵____")
    print(f"{Fore.CYAN}1.{Style.RESET_ALL} Показати баланс")
    print(f"{Fore.GREEN}2.{Style.RESET_ALL} Поповнити гаманець")
    print(f"{Fore.RED}3.{Style.RESET_ALL} Зняти кошти")
    print(f"{Fore.BLUE}4.{Style.RESET_ALL} Конвертувати валюту")
    print(f"{Fore.YELLOW}5.{Style.RESET_ALL} Курс валюти на даний момент")
    print(f"{Fore.MAGENTA}6.{Style.RESET_ALL} Вийти")
    
    action = input("Виберіть дію, яку ви хочете зробити, вписавши просто цифру: ")

    if action == "1":
        currency = input("Введіть валюту, наприклад (UAH): ")
        Balance(currency)
    elif action == "2":
        currency = input("Введіть валюту, наприклад (UAH): ")
        amount = input("Введіть суму: ")
        replenish_wallet(currency, amount)
    elif action == "3":
        currency = input("Введіть валюту, наприклад (UAH): ")
        amount = input("Введіть суму, яку хочете зняти: ")
        withdrawal_funds(currency, amount)
    elif action == "4":
        from_currency = input("Введіть валюту джерела: ")
        to_currency = input("Введіть валюту призначення: ")
        amount = float(input("Введіть суму: "))
        result = convert(amount, from_currency, to_currency)
        if result is not None:
            print(f"Конвертована сума: {result}")
        else:
            print("Конвертація неможлива. Перевірте введені валюти.")
    elif action == "5":
        curse()
    elif action == "6":
        break
    else:
        print("Невірний вибір, спробуйте ще раз.")
