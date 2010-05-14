Human readable date diff filter for python (and Django)
=======================================================

This snippet display a human readable date differential for feed update like twitter or facebook.
You give it the your date in parameter (an UTC date is expected) and the diff with datetime.datetime.utcnow() is returned.
Dates in the future dates are not supported yet.

Usage::

    {{ status.created_at|date_diff }}

Will give something like::

    just now
    13 minutes ago
    1 hour ago
    etc.

To test the filter::

    python tests.py


I proposed the code for inclusion in Django.

.. Django ticket 13541: http://code.djangoproject.com/ticket/13541

The use of javascript instead of python is an open discussion.