# Hacky Thing for Peterbe

To open a web page and keep it open, use the following command:

``py.test --driver Firefox --base-url {url_to_visit} --minutes {minutes_to_keep_page_open}``

To open multiple browsers include a ``--count`` for the number of times you want run the "test"
as well as a ``-n`` for the number of concurrent browsers, for example:

``py.test --driver Firefox --base-url https://www.mozilla.org --minutes 10 --count 10 -n 5``

will open 5 browser sessions to run 10 instances of the test.

Note that ``pytest-xdist`` (which uses the ``-n`` parameter) doesn't always open the number of sessions one would expect,
which is why I recommend making ``--count`` greater than ``-n``.
