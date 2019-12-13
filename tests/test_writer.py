#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ndjson` package."""
import json

import pytest
import six

import ndjson


@pytest.fixture
def data():
    return [
        {'bar': 'spam', 'baz': ['eggs', 'spam'], 'foo': 'spam'},
        {'bar': 'ham', 'baz': ['eggs', 'ham'], 'foo': 'ham'},
    ]


def test_writer(data):
    fp = six.StringIO()
    writer = ndjson.writer(fp)

    for item in data:
        writer.writerow(item)

    assert fp.getvalue() == '\n'.join(json.dumps(item) for item in data) + '\n'
