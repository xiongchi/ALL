# -*- coding: utf-8 -*-
from enum import Enum


class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Web = 3
    Thu = 4
    Fri = 5
    Sat = 6
    Str = "str"

print Weekday.Sun
print Weekday.Str
