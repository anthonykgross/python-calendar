=============
Tutorial
=============

Getting started
===============

Before we start, we have to install **python-calendar**.

.. code-block::

    $ python -m pip install python-calendar


We have to create a ``main.py`` file and import **python-calendar**.

.. note:: You can see our examples on `Github <https://github.com/anthonykgross/python-calendar/tree/main/examples/>`_

Get interval
===============

.. code-block:: python

    # main.py
    #
    from python_calendar import Calendar

    date_from = parse('2023-08-23')
    date_to = parse('2024-08-23')
    calendar = Calendar.get(date_from, date_to)

Years
-----

.. code-block:: python

    # main.py
    #
    # ...
    #
    print("\nYears : ")
    for y in calendar.years:
        print(y)

    # Years :
    # 2023
    # 2024

Months
------

.. code-block:: python

    # main.py
    #
    # ...
    #
    print("\nMonths : ")
    for m in calendar.months:
        print(m)

    # Months :
    # 2023-08
    # 2023-09
    # 2023-10
    # 2023-11
    # 2023-12
    # 2024-01
    # 2024-02
    # 2024-03
    # 2024-04
    # 2024-05
    # 2024-06
    # 2024-07
    # 2024-08

Weeks
-----

.. code-block:: python

    # main.py
    #
    # ...
    #
    print("\nWeeks : ")
    for w in calendar.weeks:
        print(w)
    # Weeks :
    # 2023-W34
    # 2023-W35
    # 2023-W36
    # 2023-W37
    # 2023-W38
    # 2023-W39
    # 2023-W40
    # ...
    # 2024-W28
    # 2024-W29
    # 2024-W30
    # 2024-W31
    # 2024-W32
    # 2024-W33
    # 2024-W34


Days
----

.. code-block:: python

    # main.py
    #
    # ...
    #
    print("\nDays : ")
    for d in calendar.days:
        print(d)
    # Days :
    # 2023-08-23
    # 2023-08-24
    # 2023-08-25
    # 2023-08-26
    # 2023-08-27
    # 2023-08-28
    # 2023-08-29
    # 2023-08-30
    # 2023-08-31
    # 2023-09-01
    # ...
    # 2024-08-19
    # 2024-08-20
    # 2024-08-21
    # 2024-08-22
