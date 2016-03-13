#!/usr/bin/python3


def word_match(src, tgt):
    
    return "IMPOSSIBLE"

if __name__ == "__main__":
    assert(word_match('nice', 'niece') == "ADD E")
    assert(word_match('niece', 'nice') == "DELETE E")
    assert(word_match('form', 'from') == "SWAP O AND R")
    assert(word_match('from', 'form') == "SWAP R AND O")
    assert(word_match('hi', 'hello') == "IMPOSSIBLE")
    
