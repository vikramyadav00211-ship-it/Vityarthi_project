# Project Report: Password Strength Checker

**Project Title:** Password Strength Checker
**Language:** Python 3.10+
**File:** `password_checker.py`
**Submitted by:** _Your Name_
**Course / Institution:** _Your Course / College_
**Date:** _DD/MM/YYYY_

---

## Table of Contents

1. [Abstract](#1-abstract)
2. [Introduction](#2-introduction)
3. [Objectives](#3-objectives)
4. [Tools and Technologies](#4-tools-and-technologies)
5. [System Requirements](#5-system-requirements)
6. [System Design](#6-system-design)
7. [Implementation Details](#7-implementation-details)
8. [Scoring System](#8-scoring-system)
9. [Sample Input and Output](#9-sample-input-and-output)
10. [Testing](#10-testing)
11. [Limitations](#11-limitations)
12. [Future Scope](#12-future-scope)
13. [Conclusion](#13-conclusion)

---

## 1. Abstract

This project is a command-line application written in Python that allows a user to set a password, validates it against a set of security rules, and rates its strength on a scale of 0 to 10. Along with the score and a rating label (from *Very Weak* to *Very Strong*), the program gives clear recommendations to help the user improve the password. The project demonstrates core Python concepts such as functions, loops, conditional statements, string handling, and the `match` statement.

## 2. Introduction

Passwords are the first line of defence for most online accounts. Weak passwords, such as short ones, ones made only of letters, or ones using common words like "password" or "123456", are easy to guess or crack. Many users do not know what makes a password strong.

This project addresses that problem with a small, easy-to-use tool that checks a password against basic rules and tells the user how strong it is and how to make it better.

## 3. Objectives

- To build an interactive menu-driven program in Python.
- To validate a password against defined rules (length, starting character, restricted symbols).
- To calculate a strength score out of 10 based on length and character variety.
- To detect common weak patterns and repeated characters and reduce the score accordingly.
- To give the user useful feedback on how to improve the password.

## 4. Tools and Technologies

| Item | Details |
| --- | --- |
| Programming language | Python 3.10 or newer |
| Editor / IDE | Visual Studio Code |
| Version control | Git and GitHub |
| External libraries | None (only built-in features are used) |

## 5. System Requirements

**Software**

- Python 3.10 or above (required for the `match` statement)
- Any operating system (Windows, Linux, macOS)
- A terminal or command prompt

**Hardware**

- Any standard computer. The program uses negligible memory and CPU.

## 6. System Design

### 6.1 Program Flow

```
Start
  |
  v
Show Menu  <---------------------------+
  |                                     |
  +-- 1. Set password --> validate --> store password
  |                                     |
  +-- 2. Check strength --> (password set?) 
  |          |                          |
  |          +-- No --> show message ---+
  |          +-- Yes --> validate again, calculate score,
  |                      show rating + recommendations
  |                                     |
  +-- 3. Exit --> Goodbye message --> End
```

### 6.2 Modules / Functions

| Function | Purpose |
| --- | --- |
| `check_len(pw)` | Returns `True` if the password has at least `MIN_LEN` characters. |
| `check_not_start_with_number(pw)` | Returns `False` if the first character is a digit. |
| `check_no_bad_symbols(pw)` | Returns `False` if the password contains any restricted symbol. |
| `find_error(pw)` | Runs all validation checks and returns the first error message, or `None` if the password is valid. |
| `set_password()` | Repeatedly asks for a password until a valid one is entered. |
| `check_pw(pw)` | Calculates the strength score and builds a list of recommendations. |
| `label(sc)` | Converts a numeric score into a rating label. |
| `show_strength(pw)` | Displays the score, rating, and recommendations. |
| `main()` | Displays the menu and handles user choices. |

### 6.3 Constants

| Constant | Value | Meaning |
| --- | --- | --- |
| `MIN_LEN` | `10` | Minimum allowed password length |
| `BAD_SYMBOLS` | `^*()%` | Symbols that are not allowed |

## 7. Implementation Details

### 7.1 Menu

The program runs in an infinite `while` loop and shows three options. The user's choice is handled with a `match-case` statement:

- **Option 1** calls `set_password()` to store a new password.
- **Option 2** checks whether a password exists. If it does, `show_strength()` is called.
- **Option 3** exits the loop and ends the program.
- Any other input shows an error message and the menu is displayed again.

### 7.2 Validation Rules

A password is accepted only if all of the following are true:

1. It is at least **10 characters** long.
2. It does **not start with a number**.
3. It does **not contain** any of the symbols `^ * ( ) %`.

If any rule fails, an appropriate error message is shown and the user is asked to try again.

### 7.3 Strength Calculation

The function `check_pw()` starts with a score of 0 and adds points for each good property of the password. It also adds a matching recommendation to a feedback list whenever a property is missing. After the additions, penalties are applied for weak patterns and repeated characters. Finally, the score is kept within the range 0 to 10.

### 7.4 Weak Pattern Detection

The password is converted to lowercase and compared with a list of common weak patterns:

`123`, `password`, `qwerty`, `abc`, `letmein`, `admin`

If any of them is found inside the password, 2 points are deducted (only once, even if more than one pattern is present).

### 7.5 Repeated Character Detection

The program scans the password and checks every group of four consecutive characters. If all four are identical (for example `aaaa` or `@@@@`), 2 points are deducted.

## 8. Scoring System

### 8.1 Points

| Criteria | Points |
| --- | --- |
| Length of 14 or more characters | +2 |
| Length of 10 to 13 characters | +1 |
| Contains a lowercase letter | +2 |
| Contains an uppercase letter | +2 |
| Contains a digit | +2 |
| Contains a special character | +2 |
| Contains a common weak pattern | -2 |
| Same character repeated 4 or more times in a row | -2 |

Maximum score: **10**. Minimum score: **0**.

### 8.2 Rating Labels

| Score | Rating |
| --- | --- |
| 0 - 3 | Very Weak |
| 4 - 5 | Weak |
| 6 - 7 | Moderate |
| 8 - 9 | Strong |
| 10 | Very Strong |

## 9. Sample Input and Output

**Example 1: Password that fails validation**

```
Enter a new password: hello123
Error: password must be at least 10 characters long.
Please try again.
```

**Example 2: Moderate password**

```
Enter a new password: HelloWorld12
Password updated successfully.

Password Strength: Moderate  (7/10)

Recommendations:
- Use 14 or more characters to earn full length points.
- Include a special character, other than ^ * ( ) %
```

**Example 3: Very strong password**

```
Password Strength: Very Strong  (10/10)
Excellent, this is a strong password.
```

## 10. Testing

The following test cases were used to verify the program. Expected results are based on the rules in the code.

| # | Input Password | Expected Result |
| --- | --- | --- |
| 1 | `Hello123` | Rejected: fewer than 10 characters |
| 2 | `1234567890abc` | Rejected: starts with a number |
| 3 | `Hello^World1` | Rejected: contains restricted symbol `^` |
| 4 | `helloworld` | Accepted. Score 3/10, Very Weak |
| 5 | `HelloWorld12` | Accepted. Score 7/10, Moderate |
| 6 | `Password@1234` | Accepted. Score 7/10, Moderate (weak pattern penalty applied) |
| 7 | `Hello@@@@World1` | Accepted. Score 8/10, Strong (repeated-character penalty applied) |
| 8 | `Hello@World#2024` | Accepted. Score 10/10, Very Strong |
| 9 | Menu choice `2` before setting a password | Message asking the user to set a password first |
| 10 | Menu choice `9` | "Not a valid option" message |

## 11. Limitations

- The password is typed in plain text and is visible on the screen.
- The password is stored only in memory and is lost when the program closes.
- The list of weak patterns is small and fixed. For example, `Password@1234` still receives a Moderate rating.
- The tool does not check the password against real lists of leaked passwords.
- Only one deduction is applied for weak patterns, even if several are present.
- The program uses a command-line interface only and has no graphical interface.

## 12. Future Scope

- Hide the typed password using Python's `getpass` module.
- Add a larger list of common passwords, or check against a leaked-password database.
- Detect keyboard sequences (such as `asdf`) and simple increasing or decreasing sequences.
- Add a random strong password generator.
- Save only a hashed version of the password for secure storage.
- Build a graphical interface (for example with Tkinter) or a web version.
- Add automated unit tests for every function.

## 13. Conclusion

The Password Strength Checker meets its goal of validating passwords, scoring them out of 10, and giving clear suggestions for improvement. The project uses simple, readable Python code and covers important programming concepts such as functions, loops, conditions, and string processing. It also helps raise awareness of what makes a password secure. With the improvements listed under Future Scope, it can be extended into a more complete and practical tool.

---

*End of Report*
