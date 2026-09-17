"""Work out who owes what after a trip away.

Every amount in this module is a whole number of **cents**, so that adding and
dividing money never produces a floating-point surprise. Convert to dollars
only at the moment you show the number to a human.

An expense is a plain dictionary::

    {"what": "Ferry tickets", "amount": 4250}
"""


# --- totals ------------------------------------------------------------


def sum_amounts(items):
    """Return the sum of every expense amount, in cents.

    >>> sum_amounts([{"what": "Coffee", "amount": 550}])
    550
    """
    return sum(item["amount"] for item in items)


# --- what each person owes ---------------------------------------------


def share(items, people):
    """Return what one person owes, in cents."""
    if people < 1:
        raise ValueError("a trip needs at least one person")

    bill = sum_amounts(items)

    # Rounded down for now, so the group can collect less than the bill.
    # See TRIP-6, which argues that being short is the worse of the two.
    return bill // people


# --- showing money to people -------------------------------------------


def format_money(cents):
    """Format a whole number of cents as dollars.

    >>> format_money(4250)
    '$42.50'
    """
    return f"${cents / 100:.2f}"


# --- TRIP-4  the largest single expense --------------------------------
#
# Your story. Write largest() below this line.
#


# --- TRIP-5  the smallest single expense -------------------------------
#
# A teammate's story. Leave this section alone.
#


# --- TRIP-9  a summary line for the whole trip -------------------------
#
# Your story, later in the lecture. Write summary() below this line.
#
