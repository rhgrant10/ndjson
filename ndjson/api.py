# -*- coding: utf-8 -*-
import json

from .codecs import Decoder, Encoder


def load(*args, **kwargs):
    kwargs.setdefault('cls', Decoder)
    return json.load(*args, **kwargs)


def loads(*args, **kwargs):
    kwargs.setdefault('cls', Decoder)
    return json.loads(*args, **kwargs)


def dump(obj, fp, cls=None, **kwargs):
    if cls is None:
        cls = Encoder
    text = cls(**kwargs).encode(obj)
    fp.write(text)


def dumps(*args, **kwargs):
    kwargs.setdefault('cls', Encoder)
    return json.dumps(*args, **kwargs)
