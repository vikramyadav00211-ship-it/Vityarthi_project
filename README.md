# Vityarthi_project
# Password Strength Checker

A small command-line tool written in Python that lets you set a password, validates it against a few rules, and rates its strength on a scale of 0–10 with tips for improving it.

## Features

- **Interactive menu** – set or replace a password, check its strength, or exit
- **Validation rules** – rejects passwords that are too short, start with a number, or contain restricted symbols
- **Strength score (0–10)** – based on length and character variety
- **Penalties** – deducts points for common weak patterns and repeated characters
- **Actionable feedback** – tells you exactly what to change to improve your score

## Requirements

- Python **3.10 or newer** (the script uses `match` statements)

No external dependencies are needed.

## Getting Started

```bash
# Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# Run the program
python password_checker.py
```

## Usage

When you run the script, you'll see this menu:

```
===== Password Strength Checker =====
1. Set or replace password
2. Check password strength (out of 10)
3. Exit
Please choose an option (1-3):
```

1. **Set or replace password** – enter a new password. It must pass the validation rules or you'll be asked to try again.
2. **Check password strength** – shows a score out of 10, a rating, and recommendations. You must set a password first.
3. **Exit** – quits the program.

### Example output

```
Password Strength: Moderate  (7/10)

Recommendations:
- Use 14 or more characters to earn full length points.
- Include a special character, other than ^ * ( ) %
```

## Validation Rules

A password is accepted only if it:

- Is at least **10 characters** long
- Does **not** start with a number
- Does **not** contain any of these symbols: `^ * ( ) %`

## Scoring System

| Criteria | Points |
| --- | --- |
| Length of 14+ characters | +2 |
| Length of 10–13 characters | +1 |
| Contains a lowercase letter | +2 |
| Contains an uppercase letter | +2 |
| Contains a number | +2 |
| Contains a special character | +2 |
| Contains a common pattern (`123`, `password`, `qwerty`, `abc`, `letmein`, `admin`) | −2 |
| Same character repeated 4+ times in a row | −2 |

The final score is limited to the range **0–10**.

### Strength ratings

| Score | Rating |
| --- | --- |
| 0–3 | Very Weak |
| 4–5 | Weak |
| 6–7 | Moderate |
| 8–9 | Strong |
| 10 | Very Strong |

## Customization

You can adjust the behavior by editing the constants and lists at the top of `password_checker.py`:

- `MIN_LEN` – minimum allowed password length
- `BAD_SYMBOLS` – characters that are not allowed
- `weak_words` (inside `check_pw`) – common patterns that reduce the score

## Project Structure

```
.
├── password_checker.py   # Main script
└── README.md
```

## Security Note

This is a learning project. The password is held in memory only while the program runs and is never saved or transmitted. Scoring is rule-based and is not a substitute for a professional password audit. For real-world use, prefer a password manager and unique, randomly generated passwords.

## License

Add a license of your choice (for example, [MIT](https://choosealicense.com/licenses/mit/)) and describe it here.
