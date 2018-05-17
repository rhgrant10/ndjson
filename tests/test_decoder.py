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


def _create_ndjson(data):
    lines = [json.dumps(each) for each in data]
    return '\n'.join(lines)


def test_loads(data):
    text = _create_ndjson(data)
    assert ndjson.loads(text) == data


def test_load(data):
    text = _create_ndjson(data)
    fp = six.StringIO(text)
    result = ndjson.load(fp)
    assert result == data


def test_without_decoder(data):
    text = _create_ndjson(data)
    with pytest.raises(ValueError):
        json.loads(text)
