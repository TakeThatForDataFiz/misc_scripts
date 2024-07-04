import pytest
from main import get_date
from datetime import date

@pytest.mark.parametrize(
"input_dt,day_int,expected",
[
    ("04/22/2024", "20", date(2024, 4, 20)),
    ("05/18/2024", "8", date(2024, 5, 8)),
    ("06/01/2024", None, date(2024, 6, 1))
])
def test_date_func(input_dt, day_int, expected):
    assert get_date(input_dt=input_dt, day_int=day_int) == expected
