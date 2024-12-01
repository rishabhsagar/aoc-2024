#!/bin/bash

sim() {
    awk '{
        a[$1]++;
        b[$2]++;
    }
    END {
        s = 0;
        for (x in a) if (x in b) s += x * b[x];
        print s;
    }' "$1"
}

diff() {
    awk '{print $1 > "c1"; print $2 > "c2";}' "$1"
    sort -n c1 > s1
    sort -n c2 > s2
    paste s1 s2 | awk '{d += ($1 > $2 ? $1 - $2 : $2 - $1)} END {print d}'
    rm c1 c2 s1 s2
}

[ "$1" = "sim" ] && sim "$2"
[ "$1" = "diff" ] && diff "$2"
