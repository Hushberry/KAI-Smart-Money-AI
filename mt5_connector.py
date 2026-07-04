import MetaTrader5 as mt5

def connect_to_mt5():
    print("Connecting to MetaTrader 5...")

    if not mt5.initialize():
        print("Failed to initialize MetaTrader 5. Error code:", mt5.last_error())
        return False

    print("Successfully connected to MetaTrader 5.")
    return True

def get_account_info():
    account_info = mt5.account_info()
    if account_info is None:
        print("Failed to retrieve account information. Error code:", mt5.last_error())
        return
    
    print("========= Account Information ==========")
    print(f"Login: {account_info.login}")
    print(f"Name: {account_info.name}")
    print(f"Server: {account_info.server}")
    print(f"Balance: {account_info.balance}")
    print(f"Equity: {account_info.equity}")
    print(f"Margin: {account_info.margin}")
    print(f"Leverage: {account_info.leverage}")
    print(f"Currency: {account_info.currency}")
    print("=" * 50)