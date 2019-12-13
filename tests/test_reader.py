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


def test_reader(data):
    text = '\n'.join(json.dumps(item) for item in data) + '\n'

    fp = six.StringIO(text)
    reader = ndjson.reader(fp)

    read_items = [item for item in reader]

    assert read_items == data
