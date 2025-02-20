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

financial_records = {
    #прибуток   
    "profit": [],
    #Витрати
    "costs": [],
    #інвестиції
    "investment": [],

}

def convert(amount, from_currency, to_currency):
    key = from_currency.upper() + "/" + to_currency.upper()
    if key in curse_currency:
        converted_amount = amount * curse_currency[key]
        if from_currency in wallet and wallet[from_currency] >= amount:
            wallet[from_currency] -= amount
            if to_currency in wallet:
                wallet[to_currency] += converted_amount
            else:
                wallet[to_currency] = converted_amount
            return converted_amount
        else:
            print("Недостатньо коштів або у вас немає цієї валюти")
            return None
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

def share_financial_record():
    for type in financial_records:
        print(type, ":", financial_records[type])
def add_financial_record(type, amount, currency, description):
    if type in financial_records:
        financial_records[type].append((amount, description))
        if type == "profit":
            replenish_wallet(currency, amount)
        if type == "costs" or type == "investment":
            withdrawal_funds(currency, amount)

while True:
    print("____Purr-Currency🐾💵____")
    print(f"{Fore.CYAN}1.{Style.RESET_ALL} Показати баланс")
    print(f"{Fore.GREEN}2.{Style.RESET_ALL} Поповнити гаманець")
    print(f"{Fore.RED}3.{Style.RESET_ALL} Зняти кошти")
    print(f"{Fore.BLUE}4.{Style.RESET_ALL} Конвертувати валюту")
    print(f"{Fore.YELLOW}5.{Style.RESET_ALL} Курс валюти на даний момент")
    print(f"{Fore.WHITE}6.{Style.RESET_ALL} фінансові записи")
    print(f"{Fore.RED}7.{Style.RESET_ALL} Огляд на записи ")
    print(f"{Fore.MAGENTA}8.{Style.RESET_ALL} Вийти")
    
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
        print("Додати прибуток")
        print("Додати витрати")
        print("Iнвестиції")
        type = input("Виберіть дію вписавши на англійській profit, costs або investment: ")
        currency = input("Введіть валюту(UAH) наприклад: ")
        amount = float(input("Введіть суму: "))
        description = input("Введіть опис: ")
        if type == "profit":
            add_financial_record("profit", amount, currency, description)
        if type == "costs":
            add_financial_record("costs", amount, currency, description)
        if type == "investments":
            add_financial_record("investments", amount, currency, description)
        else:
            print("Ви не вірно ввели, спробуйте ще раз")
    elif action == "7":
        share_financial_record()
    elif action == "8":
        break
    else:
        print("Невірний вибір, спробуйте ще раз.")
