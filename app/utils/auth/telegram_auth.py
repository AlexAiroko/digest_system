import hashlib
import hmac
import time


# Проверяем хэш, который нам прислали и который мы получили от Telegram
def verify_telegram_auth(data: dict, bot_token: str):
    data = data.copy()
    telegram_hash = data.pop("hash")
    # Преобразуем None в пустую строку, чтобы включить поле в строку проверки
    for key, value in data.items():
        if value is None:
            data[key] = ""
    data_check_string = "\n".join(
        f"{key}={value}"
        for key, value in sorted(data.items())
        if value is not None  # теперь None уже заменены на "", но оставим проверку
    )
    print("Data after conversion:", data)
    print("=== VERIFY AUTH (with None->'') ===")
    print("Data check string:", repr(data_check_string))
    secret_key = hashlib.sha256(bot_token.encode()).digest()
    calculated_hash = hmac.new(
        secret_key,
        data_check_string.encode(),
        hashlib.sha256
    ).hexdigest()
    print("Calculated hash:", calculated_hash)
    print("Telegram hash:", telegram_hash)
    return calculated_hash == telegram_hash


# Проверяем, чтобы авторизация не устарела
def validate_auth_date(auth_date: int, max_age: int = 86400):
    now = int(time.time())
    
    if int(now) - int(auth_date) > max_age:
        return False
    return True
