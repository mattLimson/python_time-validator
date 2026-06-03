# Time Validator CLI

A lightweight Python command-line utility designed to validate time strings against the strict international `HH:MM` format. This script was built as a practical backend exercise to master input sanitization, data validation, and error handling before processing data into databases or APIs.

## 🚀 Features

- **Strict Format Validation:** Enforces the two-digit rule for both hours and minutes (e.g., rejecting `12:9` or `9:05` in favor of `12:09` and `09:05`);
- **Logical Boundary Checks:** Ensures hours are strictly between `00-23` and minutes between `00-59`;
- **Input Sanitization:** Automatically handles accidental whitespace using string stripping techniques;
- **Robust Type Checking:** Leverages Python's `.isdigit()` to prevent application crashes when users input non-numeric characters;
- **Interactive CLI Loop:** Runs continuously in the terminal until the user explicitly types `exit`.

## 🛠️ Tech Stack & Concepts

- **Language:** Python 3.14+
- **String Manipulation:** `.split()`, `.strip()`, `len()`;
- **Type Casting & Checking:** `.isdigit()`, `int()`;
- **Control Flow:** `while` structural loops, nested `if/else` conditional statements.