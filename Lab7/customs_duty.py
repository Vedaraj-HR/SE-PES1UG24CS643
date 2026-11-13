
import math


def parse_declaration(text):
    """Parse a customs declaration in category:value format."""
    if not isinstance(text, str):
        raise ValueError("Declaration must be a string")

    if text.count(":") != 1:
        raise ValueError("Declaration must contain exactly one colon")

    category, value = text.split(":")
    category = category.strip()
    value = value.strip()

    if not category or not value:
        raise ValueError("Category and value cannot be empty")

    try:
        numeric_value = float(value)
    except ValueError:
        raise ValueError("Declaration value must be numeric")

    if not math.isfinite(numeric_value) or numeric_value < 0:
        raise ValueError("Declaration value must be finite and non-negative")

    return category.lower(), numeric_value


def duty_amount(text):
    """Calculate duty from an input in value@rate format."""
    if not isinstance(text, str):
        raise ValueError("Duty input must be a string")

    if text.count("@") != 1:
        raise ValueError("Duty input must contain exactly one @ symbol")

    value, rate = text.split("@")
    value = value.strip()
    rate = rate.strip()

    if not value or not rate:
        raise ValueError("Value and rate cannot be empty")

    try:
        numeric_value = float(value)
        numeric_rate = float(rate)
    except ValueError:
        raise ValueError("Value and rate must be numeric")

    if (
        not math.isfinite(numeric_value)
        or not math.isfinite(numeric_rate)
        or numeric_value < 0
        or numeric_rate < 0
    ):
        raise ValueError("Value and rate must be finite and non-negative")

    result = numeric_value * numeric_rate / 100

    if not math.isfinite(result):
        raise ValueError("Calculated duty is outside the supported range")

    return result


def hs_chapter(code):
    """Extract the two-digit chapter from an HS code."""
    if not isinstance(code, str):
        raise ValueError("HS code must be a string")

    code = code.strip()

    if not code or code.count(".") > 1:
        raise ValueError("Invalid HS code format")

    parts = code.split(".")

    chapter_part = parts[0]
    if len(chapter_part) < 2 or not chapter_part.isdigit():
        raise ValueError("HS code must start with at least two digits")

    if len(parts) == 2:
        suffix = parts[1]
        if not suffix or not suffix.isdigit():
            raise ValueError("HS code suffix must contain digits only")

    return int(chapter_part[:2])


def main():
    print("==== Running parse_declaration ====")
    user_input = input("Enter category:value (e.g. electronics:25000): ")
    try:
        result = parse_declaration(user_input)
        print("Category and Value:", result)
    except ValueError as error:
        print("Invalid declaration:", error)

    print("\n==== Running duty_amount ====")
    user_input = input("Enter value@rate (e.g. 25000@20): ")
    try:
        result = duty_amount(user_input)
        print("Duty Amount:", result)
    except ValueError as error:
        print("Invalid duty input:", error)

    print("\n==== Running hs_chapter ====")
    user_input = input("Enter an HS code (e.g. 8517.12): ")
    try:
        result = hs_chapter(user_input)
        print("Chapter:", result)
    except ValueError as error:
        print("Invalid HS code:", error)


if __name__ == "__main__":
    main()
