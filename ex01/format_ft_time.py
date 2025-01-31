#!/usr/bin/env python3

import time
from datetime import date, timedelta

today = date.today()
now = time.time()

print(f"Seconds since January 1, 1970: {now} or {format(now,'.2e')} in scientific notation")
print(today.strftime("%d %B %Y"))

# $>python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$