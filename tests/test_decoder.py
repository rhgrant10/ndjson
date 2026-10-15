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


@pytest.mark.parametrize('separator', [u'\x85', u'\u2028', u'\u2029'])
def test_unicode_line_separators_are_preserved(separator):
    data = [{u'key' + separator: u'before' + separator + u'after'}, separator]
    text = ndjson.dumps(data, ensure_ascii=False)

    assert ndjson.loads(text) == data
    assert ndjson.load(six.StringIO(text)) == data


@pytest.mark.parametrize('separator', [
    u'\v', u'\f', u'\x1c', u'\x1d', u'\x1e',
])
def test_unescaped_control_characters_are_rejected(separator):
    text = u'"before' + separator + u'after"'
    with pytest.raises(ValueError):
        ndjson.loads(text)


@pytest.mark.parametrize('separator', [
    u'\v', u'\f', u'\x1c', u'\x1d', u'\x1e',
])
def test_non_strict_control_characters_are_preserved(separator):
    text = u'"before' + separator + u'after"'
    expected = [u'before' + separator + u'after']
    assert ndjson.loads(text, strict=False) == expected


@pytest.mark.parametrize('separator', ['\n', '\r\n', '\r'])
@pytest.mark.parametrize('trailing_separator', [False, True])
def test_record_delimiters(separator, trailing_separator):
    text = '{"value": 1}' + separator + '"second record"'
    if trailing_separator:
        text += separator

    assert ndjson.loads(text) == [{'value': 1}, 'second record']


@pytest.mark.parametrize('text', ['', '\n', '\r\n', '\r', ' \t'])
def test_empty_input(text):
    assert ndjson.loads(text) == []


@pytest.mark.parametrize('text', [
    '{}\n\n{}', '{}\r\n\r\n{}', '\n{}', '{}\n\n',
])
def test_empty_records_are_rejected(text):
    with pytest.raises(ValueError):
        ndjson.loads(text)
