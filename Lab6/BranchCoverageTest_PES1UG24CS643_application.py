
import pytest

from customs_duty import duty_rate, total_duty, clearance_channel


# --------------------------------------------------
# Branch tests for duty_rate()
# --------------------------------------------------

def test_prohibited_category_branch():
    with pytest.raises(ValueError, match="prohibited item"):
        duty_rate("weapons", "US")


def test_allowed_category_branch():
    assert duty_rate("electronics", "US") == 0.20


def test_electronics_fta_branch():
    assert duty_rate("electronics", "FTA") == 0.10


def test_electronics_non_fta_branch():
    assert duty_rate("electronics", "US") == 0.20


def test_clothing_fta_branch():
    assert duty_rate("clothing", "FTA") == 0.05


def test_clothing_non_fta_branch():
    assert duty_rate("clothing", "US") == 0.12


def test_books_branch():
    assert duty_rate("books", "US") == 0


def test_other_category_branch():
    assert duty_rate("furniture", "US") == 0.15


# --------------------------------------------------
# Branch tests for total_duty()
# --------------------------------------------------

def test_negative_value_branch():
    with pytest.raises(ValueError, match="negative value"):
        total_duty("electronics", -1, "US", False)


def test_non_negative_value_branch():
    assert total_duty("electronics", 2000, "US", False) == 400


def test_gift_branch():
    assert total_duty("electronics", 5000, "US", True) == 0


def test_gift_exemption_boundary():
    assert total_duty("electronics", 5001, "US", True) == 50


def test_gift_above_exemption():
    assert total_duty("electronics", 6000, "FTA", True) == 100


def test_non_gift_branch():
    assert total_duty("electronics", 2000, "US", False) == 400


def test_non_gift_exemption_boundary():
    assert total_duty("electronics", 1000, "US", False) == 0


def test_non_gift_above_exemption():
    assert total_duty("electronics", 1001, "US", False) == pytest.approx(200.2)


def test_minimum_duty_condition_true():
    assert total_duty("clothing", 5100, "FTA", True) == 50


def test_minimum_duty_condition_false_zero():
    assert total_duty("books", 2000, "US", False) == 0


def test_minimum_duty_condition_false_high():
    assert total_duty("electronics", 2000, "US", False) == 400


# --------------------------------------------------
# Branch tests for clearance_channel()
# --------------------------------------------------

def test_prohibited_item_branch():
    assert clearance_channel(5000, "narcotics", True) == "refuse"


def test_allowed_item_branch():
    assert clearance_channel(5000, "electronics", True) == "green"


def test_value_above_100000_branch():
    assert clearance_channel(100001, "electronics", True) == "inspect"


def test_value_at_100000_boundary():
    assert clearance_channel(100000, "electronics", True) == "green"


def test_value_above_20000_without_documents():
    assert clearance_channel(25000, "electronics", False) == "inspect"


def test_value_above_20000_with_documents():
    assert clearance_channel(25000, "electronics", True) == "green"


def test_value_at_20000_without_documents():
    assert clearance_channel(20000, "electronics", False) == "green"


def test_value_below_20000_without_documents():
    assert clearance_channel(15000, "electronics", False) == "green"
