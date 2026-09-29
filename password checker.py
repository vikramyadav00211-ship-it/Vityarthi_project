# password_checker.py
# a small tool that lets you set a password, validates it, and rates its strength

MIN_LEN = 10  
BAD_SYMBOLS = "^*()%"

def check_len(pw):
    return len(pw) >= MIN_LEN

def check_not_start_with_number(pw):
    if pw[0].isdigit():
        return False
    return True

def check_no_bad_symbols(pw):
    for c in pw:
        if c in BAD_SYMBOLS:
            return False
    return True

def find_error(pw):
    if not check_len(pw):
        return f"Error: password must be at least {MIN_LEN} characters long."
    if not check_not_start_with_number(pw):
        return "Error: password must not start with a number."
    if not check_no_bad_symbols(pw):
        return f"Error: password contains a restricted symbol. Avoid: {BAD_SYMBOLS}"
    return None


def set_password():
    while True:
        pw = input("Enter a new password: ")
        err = find_error(pw)
        if err:
            print(err)
            print("Please try again.\n")
        else:
            print("Password updated successfully.")
            return pw


def check_pw(pw):
    sc = 0
    fb = []
    if len(pw) >= 14:
        sc += 2
    elif len(pw) >= MIN_LEN:
        sc += 1
        fb.append("Use 14 or more characters to earn full length points.")

    low = False
    for c in pw:
        if c.islower():
            low = True
            break
    if low:
        sc += 2
    else:
        fb.append("Include at least one lowercase letter.")
    up = False
    for c in pw:
        if c.isupper():
            up = True
            break
    if up:
        sc += 2
    else:
        fb.append("Include at least one uppercase letter.")

    num = False
    for c in pw:
        if c.isdigit():
            num = True
            break
    if num:
        sc += 2
    else:
        fb.append("Include at least one number.")

    sym = False
    for c in pw:
        if not c.isalnum():
            sym = True
            break
    if sym:
        sc += 2
    else:
        fb.append("Include a special character, other than ^ * ( ) %")

    weak_words = ["123", "password", "qwerty", "abc", "letmein", "admin"]
    pw_lower = pw.lower()
    for w in weak_words:
        if w in pw_lower:
            fb.append(f"Avoid common patterns such as '{w}'.")
            sc -= 2
            break

    for i in range(len(pw) - 3):
        if pw[i] == pw[i+1] == pw[i+2] == pw[i+3]:
            fb.append("Avoid repeating the same character four or more times in a row.")
            sc -= 2
            break
    if sc < 0:
        sc = 0
    if sc > 10:
        sc = 10

    return sc, fb

def label(sc):
    if sc <= 3:
        return "Very Weak"
    elif sc <= 5:
        return "Weak"
    elif sc <= 7:
        return "Moderate"
    elif sc <= 9:
        return "Strong"
    else:
        return "Very Strong"

def show_strength(pw):
    err = find_error(pw)
    if err:
        print(f"\n{err}")
        return

    sc, fb = check_pw(pw)
    lvl = label(sc)

    print(f"\nPassword Strength: {lvl}  ({sc}/10)")

    if fb:
        print("\nRecommendations:")
        for tip in fb:
            print(f"- {tip}")
    else:
        print("Excellent, this is a strong password.")

def main():
    pw = "" 

    while True:
        print("\n===== Password Strength Checker =====")
        print("1. Set or replace password")
        print("2. Check password strength (out of 10)")
        print("3. Exit")
        choice = input("Please choose an option (1-3): ")

        match choice:
            case "1":
                pw = set_password()

            case "2":
                if pw == "":
                    print("\nNo password has been set yet. Please choose option 1 first.")
                else:
                    show_strength(pw)

            case "3":
                print("Thank you for using the Password Strength Checker. Goodbye!")
                break

            case _:
                print("That's not a valid option, please choose 1, 2, or 3.")

main()