
import math
from hypothesis import given, strategies as st

from customs_duty import parse_declaration, duty_amount, hs_chapter


# Test 1: Fuzz parse_declaration
@given(st.text() | st.none())
def test_parse_declaration_no_crash(s):
    try:
        result = parse_declaration(s)
    except ValueError:
        return

    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert result[0] != ""
    assert math.isfinite(result[1])
    assert result[1] >= 0


# Test 2: Fuzz duty_amount
@given(st.text() | st.none())
def test_duty_amount_no_crash(s):
    try:
        result = duty_amount(s)
    except ValueError:
        return

    assert isinstance(result, float)
    assert math.isfinite(result)
    assert result >= 0


# Test 3: Fuzz hs_chapter
@given(st.text() | st.none())
def test_hs_chapter_no_crash(s):
    try:
        result = hs_chapter(s)
    except ValueError:
        return

    assert isinstance(result, int)
    assert 0 <= result <= 99


# Additional tests for valid input and expected results
def test_valid_parse_declaration():
    assert parse_declaration("electronics:25000") == ("electronics", 25000.0)


def test_valid_duty_amount():
    assert duty_amount("25000@20") == 5000.0


def test_valid_hs_chapter():
    assert hs_chapter("8517.12") == 85
