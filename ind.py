#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# X = (A и С) или (D и B)
# Y = (A и B) или (C / D)

if __name__ == "__main__":
    a = {"a", "h", "m", "o", "r"}
    b = {"j", "k", "o", "u", "y"}
    c = {"g", "h", "i"}
    d = {"g", "i", "q"}

    ac = a.intersection(c)
    db = d.intersection(b)
    print("X =", ac.union(db))

    ab = a.intersection(b)
    cd = c.difference(d)
    print("Y =", ab.union(cd))
