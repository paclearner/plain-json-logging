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
    logging.info('this is info.')
    logging.warn('this is warn.')
    logging.error('this is error.)

The result is found in `stderr` like this:

.. code-block:: python

    { "timestamp": , "level": "INFO", "message": "this is info."}
    { "timestamp": , "level": "WARNNING", "message": "this is warn."}
    { "timestamp": , "level": "ERROR", "message": "this is error."}


Options:
--------------

The following parameters can modify how the logging behaves:

:file: the `f` for `print('output to file', file=f)`. Default: `stderr`.
:strftime: the `format <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior>`_. Defalut: `datetime.datetime <https://docs.python.org/3/library/datetime.html>`_ default.
:timedelta: the `timedelta <https://docs.python.org/3/library/datetime.html#datetime.timedelta>`_. The minute is a unit.
:timestampname: the name for `timestamp`. Default: `timestamp`.
:levelname: the name for `level`. Default: `level`.
:messagename: the name for `message`. Default: `message`.
:infoname: the name for `info`. Default: `INFO`.
:warnname: the name for `warn`. Default: `WARNNING`.
:errorname: the name for `error`. Default: `ERROR`.

For example, AWS CloudWatch supports the `discovered fields <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData-discoverable-fields.html>`_.
Therefor, if `timestampname` and `messagename` are `@timestamp` and `@message`, CloudWatch can discovere those fields.
And more, `.info()`, `.warn()` and `.error()` methods can receives extra payload.


.. code-block:: python

    from plain_json_logging import PlainJsonLogging

    logging = new PlainJsonLogging(
        file=sys.stdout,
        strftime='%Y-%m-%d %H:%M:%S.%f%z',
        timedelta=+540, # 9 hours
        timestampname='@timestamp',
        levelname='level',
        messagename='@message',
    )

    logging.info('this is info.', { 'infoData': 'this is a extra payload for info.'})
    logging.warning('this is warn.', { 'warnData': 'this is a extra payload for warning.'})
    logging.error('this is error.', { 'errData': 'this is a extra payload for warning.'})

The result is found in `stdout` like this:

.. code-block:: python

    {"infoData": "this is a extra payload for info.", "@timestamp": "2020-01-10 05:31:20.151462", "level": "INFO", "@message": "this is info"}
    {"warnData": "this is a extra payload for warning.", "@timestamp": "2020-01-10 05:31:20.151462", "level": "WARNNING", "@message": "this is warn"}
    {"errData": "this is a extra payload for warning.", "@timestamp": "2020-01-10 05:31:20.151462", "level": "ERROR", "@message": "this is error"}
