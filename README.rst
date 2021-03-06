===================
plain-json-logging
===================

`plain-json-logging` is a simple logging for a JSON data.


Installation:
-------------

    $ pip install plain-json-logging


Usage:
------

.. code-block:: python

    from plain_json_logging import PlainJsonLogging

    logging = new PlainJsonLogging()
    logging.error('this is error.)
    logging.warn('this is warn.')
    logging.info(
      'foo'
    ).info(
      'bar'
    ).info(
      'baz'
    )


The result is found in `stderr` like this:

.. code-block:: json

    { "timestamp": "2020-01-10T00:06:24.855159", "level": "ERROR", "message": "this is error."}
    { "timestamp": "2020-01-10T00:06:24.855159", "level": "WARN", "message": "this is warn."}
    { "timestamp": "2020-01-10T00:06:24.855159", "level": "INFO", "message": "foo"}
    { "timestamp": "2020-01-10T00:06:24.855159", "level": "INFO", "message": "bar"}
    { "timestamp": "2020-01-10T00:06:24.855159", "level": "INFO", "message": "baz"}


Options:
--------

.. code-block:: python

    from plain_json_logging import PlainJsonLogging

    logging = new PlainJsonLogging(
      file=sys.stdout,
      strftime='%Y-%m-%d %H:%M:%S.%f%z',
      timezone='America/Chicago',
      timedelta=+540, # 9 hours
      timestampname='@timestamp',
      messagename='@message',
      levelname='lev',
      levelinfo=0,
      levelwarn=1,
      levelerror=2,
      constextra={ name: 'Example' }
    )

The following parameters can modify how the logging behaves:

:file:          the writable `file object <https://docs.python.org/3/glossary.html#term-file-object>`_. Default: `sys.stderr`.
:strftime:      the `format <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior>`_. Defalut: `datetime.datetime <https://docs.python.org/3/library/datetime.html>`_ default.
:timezone:      the `TZ database name <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`_. Default: `UTC`.
:timedelta:     the `timedelta <https://docs.python.org/3/library/datetime.html#datetime.timedelta>`_. The `minute` is a unit. Default: `0`.
:timestampname: the name for `timestamp`. Default: `timestamp`.
:messagename:   the name for `message`. Default: `message`.
:levelname:     the name for `level`. Default: `level`.
:levelinfo:     the value for the level `info`. Default: `INFO`.
:levelwarn:     the value for the level `warn`. Default: `WARN`.
:levelerror:    the value for the level `error`. Default: `ERROR`.
:constextra:    the default additional items for each log
                (the value must be a dictionary object): Default: `None`.


API:
----

`PlainJsonLogging` has the following three methods:

* info
* warn
* error

All the methods returns the `PlainJsonLogging` instance itself.
Therefore, `method chaining` can be used for logging:

.. code-block:: python

    from plain_json_logging import PlainJsonLogging

    logging = new PlainJsonLogging()
    logging.info(
      'foo'
    ).info(
      'bar'
    ).info(
      'baz'
    )


Extra Payload:
--------------

All the methods can receives extra payload.

.. code-block:: python

    from plain_json_logging import PlainJsonLogging

    logging = new PlainJsonLogging(
      file=sys.stdout,
      strftime='%Y-%m-%d %H:%M:%S.%f%z',
      timezone='Asia/Tokyo',
      timedelta=0,
      timestampname='@timestamp',
      messagename='@message',
      levelname='lev',
      levelinfo=0,
      levelwarn=1,
      levelerror=2,
      constextra={ name: 'Example' },
    )

    logging.info('this is info.', { 'infoData': 'this is a extra payload for info.'})
    logging.warn('this is warn.', { 'warnData': 'this is a extra payload for warn.'})
    logging.error('this is error.', { 'errData': 'this is a extra payload for error.'})

The result is found in `stdout` like this:

.. code-block:: json

    {"@timestamp": "2020-01-13 07:17:06.370000+0900", "lev": 0, "@message": "this is info.", "name": "Example", "infoData": "this is a extra payload for info."}
    {"@timestamp": "2020-01-13 07:17:06.370000+0900", "lev": 1, "@message": "this is warn.", "name": "Example", "warnData": "this is a extra payload for warn."}
    {"@timestamp": "2020-01-13 07:17:06.370000+0900", "lev": 2, "@message": "this is error.", "name": "Example", "errData": "this is a extra payload for error."}
