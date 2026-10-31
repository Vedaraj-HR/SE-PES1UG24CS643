
import pytest

from customs_duty import duty_rate, total_duty, clearance_channel


# --------------------------------------------------
# Tests for duty_rate()
# --------------------------------------------------

def test_prohibited_category():
    with pytest.raises(ValueError, match="prohibited item"):
        duty_rate("weapons", "FTA")


def test_electronics_fta():
    assert duty_rate("electronics", "FTA") == 0.10


def test_electronics_non_fta():
    assert duty_rate("electronics", "US") == 0.20


def test_clothing_fta():
    assert duty_rate("clothing", "FTA") == 0.05


def test_clothing_non_fta():
    assert duty_rate("clothing", "US") == 0.12


def test_books_duty_free():
    assert duty_rate("books", "US") == 0


def test_other_category():
    assert duty_rate("furniture", "US") == 0.15


# --------------------------------------------------
# Tests for total_duty()
# --------------------------------------------------

def test_negative_value():
    with pytest.raises(ValueError, match="negative value"):
        total_duty("electronics", -100, "US", False)


def test_gift_value_within_exemption():
    assert total_duty("electronics", 5000, "US", True) == 0


def test_gift_value_above_exemption():
    assert total_duty("electronics", 6000, "FTA", True) == 100


def test_gift_minimum_duty():
    assert total_duty("clothing", 5100, "FTA", True) == 50


def test_non_gift_within_exemption():
    assert total_duty("electronics", 1000, "US", False) == 0


def test_non_gift_above_exemption():
    assert total_duty("electronics", 2000, "FTA", False) == 200


def test_zero_duty_does_not_apply_minimum():
    assert total_duty("books", 2000, "US", False) == 0


# --------------------------------------------------
# Tests for clearance_channel()
# --------------------------------------------------

def test_prohibited_item_refused():
    assert clearance_channel(5000, "narcotics", True) == "refuse"


def test_high_value_import_inspected():
    assert clearance_channel(100001, "electronics", True) == "inspect"


def test_import_without_documents_inspected():
    assert clearance_channel(25000, "electronics", False) == "inspect"


def test_import_with_documents_cleared():
    assert clearance_channel(25000, "electronics", True) == "green"


def test_value_at_inspection_threshold_cleared():
    assert clearance_channel(20000, "electronics", False) == "green"
