"""Tests for splitter.py.

A test is an ordinary function whose name starts with ``test_``, living in a
file whose name starts with ``test_``. Its job is to assert something that
should be true. Run them all with::

    pytest

A dot is a pass. An ``F`` is a failure, and pytest then prints the value it
got next to the value it expected -- those two lines are the whole message.
"""

import pytest

import splitter

# One trip, used by most of the tests below. $248.80 in three expenses.
TRIP = [
    {"what": "Ferry tickets", "amount": 4250},
    {"what": "Groceries", "amount": 8630},
    {"what": "Campsite", "amount": 12000},
]


# --- totals ------------------------------------------------------------


def test_sum_amounts_adds_up_every_expense():
    assert splitter.sum_amounts(TRIP) == 24880


def test_sum_amounts_of_an_empty_trip_is_zero():
    assert splitter.sum_amounts([]) == 0


# --- what each person owes ---------------------------------------------


def test_share_divides_the_total_between_the_people():
    assert splitter.share(TRIP, 4) == 6220


def test_share_refuses_a_trip_with_nobody_on_it():
    with pytest.raises(ValueError):
        splitter.share(TRIP, 0)


# --- showing money to people -------------------------------------------


def test_format_money_shows_dollars_and_cents():
    assert splitter.format_money(4250) == "$42.50"


# --- TRIP-4  the largest single expense --------------------------------
#
# Your tests go below this line.
#


# --- TRIP-5  the smallest single expense -------------------------------
#
# A teammate's tests. Leave this section alone.
#


# --- TRIP-9  a summary line for the whole trip -------------------------
#
# Your tests, later in the lecture.
#
