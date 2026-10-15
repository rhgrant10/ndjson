# -*- coding: utf-8 -*-
import json
import re


class Decoder(json.JSONDecoder):
    def decode(self, s, *args, **kwargs):
        # splitlines() also splits characters allowed inside JSON strings.
        lines = re.split(r'\r\n|\r|\n', s)
        if lines[-1] == '':
            lines.pop()
        text = '[{}]'.format(','.join(lines))
        return super(Decoder, self).decode(text, *args, **kwargs)


class Encoder(json.JSONEncoder):
    def encode(self, obj, *args, **kwargs):
        lines = []
        for each in obj:
            line = super(Encoder, self).encode(each, *args, **kwargs)
            lines.append(line)
        return '\n'.join(lines)
