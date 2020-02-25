======
ndjson
======

Support for ndjson. Plain and simple.

.. image:: https://img.shields.io/pypi/v/ndjson.svg
        :target: https://pypi.python.org/pypi/ndjson

.. image:: https://img.shields.io/travis/rhgrant10/ndjson.svg
        :target: https://travis-ci.org/rhgrant10/ndjson

.. image:: https://img.shields.io/pypi/pyversions/ndjson
    :target: https://pypi.python.org/pypi/ndjson

.. image:: https://img.shields.io/pypi/l/ndjson
    :target: https://pypi.python.org/pypi/ndjson


Features
--------

* familiar interface
* very small
* no dependencies
* works as advertised
* has tests


Usage
-----

``ndjson`` exposes the same api as the builtin ``json`` and ``pickle`` packages.

.. code-block:: python

    import ndjson

    # load from file-like objects
    with open('data.ndjson') as f:
        data = ndjson.load(f)

    # convert to and from objects
    text = ndjson.dumps(data)
    data = ndjson.loads(text)

    # dump to file-like objects
    with open('backup.ndjson', 'w') as f:
        ndjson.dump(items, f)


It contains ``JSONEncoder`` and ``JSONDecoder`` classes for easy
use with other libraries, such as ``requests``:

.. code-block:: python

    import ndjson
    import requests

    response = requests.get('https://example.com/api/data')
    items = response.json(cls=ndjson.Decoder)

The library also packs ``reader`` and ``writer`` classes very similar to standard csv ones:

.. code-block:: python

    import ndjson

    # Streaming lines from ndjson file:
    with open('./posts.ndjson') as f:
        reader = ndjson.reader(f)

        for post in reader:
            print(post)

    # Writing items to a ndjson file
    with open('./posts.ndjson', 'w') as f:
        writer = ndjson.writer(f, ensure_ascii=False)

        for post in posts:
            writer.writerow(post)


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
