#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        tuple = (len(sentence), sentence[0])
        return(tuple)
    else:
        return(tuple = (0, None))
