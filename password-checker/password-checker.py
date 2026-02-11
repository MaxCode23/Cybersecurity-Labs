def has_digit(text: str) -> bool:
    for ch in text:
        if ch.isdigit():
            return True
    return False


def has_upper(text: str) -> bool:
    for ch in text:
        if ch.isupper():
            return True
    return False


def password_strength(password: str) -> str:
    length_ok = len(password) >= 8
    digit_ok = has_digit(password)
    upper_ok = has_upper(password)

    # Simple scoring rules
    if not length_ok:
        return "Weak"
    if length_ok and digit_ok and upper_ok:
        return "Strong"
    if length_ok and digit_ok:
        return "Medium"
    return "Weak"


if __name__ == "__main__":
    user_pw = input("Enter a password: ")
    print(password_strength(user_pw))
