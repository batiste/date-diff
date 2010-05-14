Human readable date diff filter for Django
==============================================

This snippet display a human readable date diff. You give it the your date in parameter (an UTC date is expected)
and the diff with datetime.datetime.utcnow() is returned. The diff must be positive to be
more accurate (future dates are not supported yet)

Usage::

    {{ status.created_at|date_diff }}

Will give something like::

    just now
    13 minutes ago
    1 hour ago
    etc.

To test the filter::

    python tests.py