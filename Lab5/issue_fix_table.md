\# Lab 5 — Static Code Analysis: Issue and Fix Table



| Issue | Type | Original Line(s) | Description | Fix Approach |

|---|---|---:|---|---|

| Missing module docstring | Pylint — C0114 | 1 | The module has no top-level description. | Add a module docstring describing the parcel-tracking system. |

| Missing function docstrings | Pylint — C0116 | 11, 20, 27, 34, 43, 48, 53, 58 | Functions lack descriptions of their purpose. | Add concise docstrings to the retained functions. |

| Non-standard identifiers | Pylint — C0103 | 11–67 | Function names, arguments, and variables use camelCase instead of snake\_case. | Rename identifiers consistently throughout the program. |

| Mutable default argument | Pylint — W0102 | 11 | `history=\[]` reuses the same list across calls when the default is used. | Use `None` as the default and initialize a list safely. |

| Broad exception handling | Pylint — W0718 | 37 | `except Exception` catches errors unrelated to a missing tracking ID. | Catch `KeyError` for a missing parcel. |

| Repeated status comparisons | Pylint — R1714 | 45 | Two comparisons check the same variable against different values. | Use membership testing with `in`. |

| Missing operator whitespace | Flake8 — E225 | 28 | `cost=50` lacks spaces around the assignment operator. | Format as `cost = 50`. |

| Insufficient spacing before inline comment | Flake8 — E261 | 71 | The comment follows code without the required spacing. | Add at least two spaces before the comment. |

| Missing space after comma | Flake8 — E231 | 74 | The output statement lacks a space after a comma. | Add a space after the comma. |

| Insufficient blank lines | Flake8 — E305 | 75 | The final function definition is not followed by the required blank lines before the module-level call. | Add the required blank lines and use a main guard. |

| Risky subprocess import | Bandit — B404 | 2 | The subprocess module can execute external commands and requires careful use. | Remove the unused ping helper and subprocess import if they are not needed. |

| Insecure temporary filename | Bandit — B306 | 50 | `tempfile.mktemp()` does not safely reserve a temporary file. | Replace it with a safe temporary-file API. |

| Shell command execution | Bandit — B602 | 55 | `shell=True` combined with string concatenation can expose command injection risk. | Remove the unused helper or execute commands without a shell and with a list of arguments. |

| Non-cryptographic OTP generation | Bandit — B311 | 72 | `random.randint()` is unsuitable for security-sensitive OTPs. | Use `secrets` to generate the OTP. |



\## Verification targets



\- Resolve the reported security findings without merely suppressing warnings.

\- Address the reported Flake8 style issues.

\- Improve the Pylint score from 4.91/10 to above 9.5/10.

\- Rerun all three tools and retain before-and-after reports.

\- Verify that the program's demonstration still works after the changes.

