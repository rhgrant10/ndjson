#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ndjson` package."""
import json

import six
import pytest

import ndjson


@pytest.fixture
def text():
    return '\n'.join([
        '{"bar": "spam", "baz": ["eggs", "spam"], "foo": "spam"}',
        '{"bar": "ham", "baz": ["eggs", "ham"], "foo": "ham"}',
    ])


def _create_list(text):
    return [json.loads(each) for each in text.splitlines()]


def test_dumps(text):
    objects = _create_list(text)
    assert ndjson.dumps(objects, sort_keys=True) == text


def test_dump(text):
    objects = _create_list(text)
    fp = six.StringIO()
    ndjson.dump(objects, fp, sort_keys=True)
    assert fp.getvalue() == text


def test_without_encoder(text):
    objects = _create_list(text)
    json.dumps(objects)
