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


class writer(object):
    def __init__(self, f, **kwargs):
        self.f = f
        self.kwargs = kwargs

    def writerow(self, row):
        stringified = json.dumps(row, **self.kwargs)
        self.f.write(stringified + '\n')


class reader(object):
    def __init__(self, f, **kwargs):
        self.f = f
        self.kwargs = kwargs

    def __iter__(self):
        return self

    def __next__(self):
        line = ''

        while line == '':
            line = next(self.f).strip()

        return json.loads(line, **self.kwargs)

    # NOTE: this is necessary to comply with py27
    def next(self):
        return self.__next__()
