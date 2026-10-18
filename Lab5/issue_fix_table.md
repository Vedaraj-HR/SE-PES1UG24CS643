
# Lab 5 — Static Code Analysis: Issue and Fix Table

## 1. Pylint Issues

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Missing module docstring | Pylint — C0114 | 1 | The module has no top-level description. | Added a module docstring describing the parcel-tracking system. |
| Missing function docstrings | Pylint — C0116 | 11, 20, 27, 34, 43, 48, 53, 58 | Functions lack descriptions of their purpose. | Added concise docstrings to the retained functions. |
| Non-standard identifiers | Pylint — C0103 | 11–67 | Function names, arguments, and variables use camelCase instead of snake_case. | Renamed identifiers consistently, such as `bookParcel` to `book_parcel` and `trackingId` to `tracking_id`. |
| Mutable default argument | Pylint — W0102 | 11 | `history=[]` reuses the same list across calls when the default is used. | Changed the default to `None` and initialized a new list inside the function when needed. |
| Broad exception handling | Pylint — W0718 | 37 | `except Exception` catches errors unrelated to a missing tracking ID. | Replaced it with `except KeyError` to handle a missing parcel specifically. |
| Repeated status comparisons | Pylint — R1714 | 45 | Two comparisons check the same variable against different values. | Used membership testing: `status in ("Picked Up", "In Transit")`. |

## 2. Bandit Security Issues

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Subprocess import | Bandit — B404 | 2 | Importing `subprocess` can introduce security risks depending on how it is used. | Removed the unused `subprocess` import and the associated `ping_hub()` helper. |
| Insecure temporary filename | Bandit — B306 | 50 | `tempfile.mktemp()` can create a race condition because the file is not securely created. | Replaced it with `tempfile.NamedTemporaryFile()` and `delete=False` to create the temporary file securely. |
| Subprocess with shell enabled | Bandit — B602 | 55 | A subprocess command uses `shell=True` with a constructed command string, creating command-injection risk. | Removed the unused `ping_hub()` helper and its unsafe subprocess call. |
| Insecure random number generation | Bandit — B311 | 72 | The standard `random` module is unsuitable for security-sensitive values such as delivery OTPs. | Replaced `random.randint()` with `secrets.randbelow(9000) + 1000` to generate a four-digit OTP. |

## 3. Flake8 Style Issues

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Missing operator whitespace | Flake8 — E225 | 28 | The assignment `cost=50` lacks spaces around the assignment operator. | Changed it to `cost = 50`. |
| Insufficient whitespace before inline comment | Flake8 — E261 | 71 | The inline comment does not have the required two spaces before `#`. | Added two spaces before the inline comment. |
| Missing whitespace after comma | Flake8 — E231 | 74 | The `print()` statement lacks a space after the comma. | Changed `len(parcels)` formatting to include a space after the comma in the function arguments: `print("Parcels booked today:", len(parcels))`. |
| Missing blank lines before function definition | Flake8 — E305 | 75 | The original code does not have the required two blank lines before the top-level function definition. | Added the required blank lines between top-level definitions. |

## 4. Verification Results

| Tool | Final Result | Status |
|---|---|---|
| Pylint | Code quality score: 10.00/10 | Passed |
| Bandit | No issues identified | Passed |
| Flake8 | No reported violations | Passed |
| Python execution | Parcel tracking demonstration runs successfully | Passed |

## 5. Summary

Static code analysis was performed using Pylint, Bandit, and Flake8. The identified code-quality, security, and formatting issues were addressed. The final program achieved a Pylint score of 10.00/10, Bandit reported no issues, and Flake8 reported no violations. The program was executed successfully to verify that its parcel-tracking demonstration still works.
