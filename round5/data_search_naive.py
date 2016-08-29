#!/usr/bin/env python3

"""
Hi!

I decided to implement this task in Python because it's my main tool.
Certanly this task is more suited for C/C++ because of fine-grained
resource control in these languages.

The present approach requires indexing of all substrings
of length=threshold in ``needle''. This takes O(len(needle)*threshold) additional
space. For practictal reasons it's worth not to make index (dictionary) too big.
So we can, e.g., index less than threshold bytes in the string and then filter out
matches shorter than threshold. Or use one of the techniques described below.

Potential optimizations
-----------------------

1) Bloom-filter
We can use bloom-filter to speed-up hash lookups.
In this case we can avoid cache thrashing when looking up among many keys that do not fit CPU caches.

2) Strings with limited set of chars
If ``needle'' consists of a limited set of chars then
we can ``haystack'' faster by skipping areas with chars not present in ``needle''.

3) Rolling check-sums
If calculating hashes/checksums takes too much time, an rsync-approach (rolling checksum) can be used.
I've done this: https://github.com/kopchik/itasks/blob/master/rsync.py
Reference: https://rsync.samba.org/tech_report/

4) The present algorithm works at a byte granularity, but 64bit block would better fit
modern CPUs.

5) The code does not try to minimize the number of matches (or maximize match length).
This is intended to keep the code simple and easy to read.

PS to launch tests:

~~~
py.test -vs ./data_search_naive.py
~~~
"""
from collections import namedtuple
Match = namedtuple("Match", ["hay_pos", "needle_pos", "match_len", "match"])


def search(haystack, needle, threshold):
    """ Searches common subsequencies in 'haystack' and 'needle' with length greater than 'threshold'.
        It's generator.
        
        Local variables:

              [=========== haystack ===============]
                ^                   ^
                |                   |
              hay_pos             hay_end
                <---- match_len ---->

    """
    # some basic input validation
    assert len(needle) >= threshold,  \
      "Needle is too short or threshold is too big"

    # we first need to build search index
    index = get_index(needle, threshold)

    hay_pos = 0
    hay_end = threshold
    hay_len = len(haystack)
    needle_len = len(needle)
    while hay_end <= hay_len:
        myslice = haystack[hay_pos:hay_end]
        needle_pos = index.get(myslice, None)
        if needle_pos is not None:
            # we found a minimal match, now expand it
            match_len = threshold
            hay_idx = hay_pos + match_len
            needle_idx = needle_pos + match_len
            while hay_idx < hay_len  \
                    and needle_idx < needle_len \
                    and needle[needle_idx] == haystack[hay_idx]:
                match_len += 1
                needle_idx += 1
                hay_idx += 1
            seq = haystack[hay_pos:hay_pos + match_len]
            yield Match(hay_pos=hay_pos,
                        needle_pos=needle_pos,
                        match_len=match_len,
                        match=seq)
            hay_pos += match_len
            hay_end = hay_pos + threshold
        else:
            # no match, move scanning window
            hay_pos += 1
            hay_end += 1


def get_index(needle, threshold):
    """ Dict matching the last occurence. """
    d = {}
    start = 0
    stop = threshold
    needle_len = len(needle)
    while stop <= needle_len:
        myslice = needle[start:stop]
        d[myslice] = start
        start += 1
        stop += 1
    return d


def test_get_index():
    assert get_index("a", 1) == {'a': 0}
    assert get_index("a", 3) == {}


def test_search_sanity_check():
    # the most trivial check
    matches = list(search('a', 'a', threshold=1))
    assert matches == [Match(match='a', match_len=1,
                       hay_pos=0, needle_pos=0)]

    # repeated pattern
    matches = list(search("aaa", "a", threshold=1))
    assert len(matches) == 3
    assert all(m.match == 'a' for m in matches)

    # check boundary conditions
    ## no match
    assert [] == list(search("a","b", threshold=1))
    ## full match
    matches = list(search("abc","abc", threshold=1))
    assert len(matches) == 1
    assert matches[0].match == "abc"
    ## bigger threshold
    matches2 = list(search("abc","abc", threshold=3))
    assert matches2 == matches
    ## match at start
    assert next(search("ABCxxxx", "A", threshold=1)).match == "A"
    ## match at the end
    assert next(search("xxxxABC", "A", threshold=1)).match == "A"


def test_search_basic():
    haystack = "abcdefg"
    needle = "abcefg"
    threshold = 1
    it = search(haystack, needle, threshold)
    assert next(it).match == "abc"
    assert next(it).match == "efg"


if __name__ == '__main__':
    haystack = "vnk2435kvabco8awkh125kjneytbcd12qjhb4acd123xmnbqwnw4t"
    needle = "abcd1234"
    threshold = 3

    for match in search(haystack, needle, threshold):
        print(
            "sequence of length = {match.match_len} found "
            "at haystack offset {match.hay_pos}, "
            "needle offset {match.needle_pos} ({match.match})".format(
                match=match))
