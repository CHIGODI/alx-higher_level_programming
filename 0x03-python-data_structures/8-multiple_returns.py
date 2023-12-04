#!/usr/bin/puython3


def multiple_returns(sentence):
    if sentence is None:
        return (0, None)
    else:
        length = int(len(sentence))
        first = sentence[0] if len(sentence) > 0 else None
        return (first, length)
