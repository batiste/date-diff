Human readable date diff filter for python (and Django)
=======================================================

This snippet display a human readable date differential for feed update like twitter or facebook.
You give it the your date in parameter a fuzzy diff with datetime.datetime.now() is returned.

Usage::

    {{ status.created_at|fuzzy_date }}

Will give something like::

    just now
    13 minutes ago
    1 hour ago
    in 1 week

To test the filter::

    python tests.py

I proposed the code to be included in Django: `Django ticket 13541 <http://code.djangoproject.com/ticket/13541>`_.

The use of javascript instead of python is an open discussion.