#!/usr/bin/env python3.10

import datetime
import time

"""
f-string : print(f"{value:format_spec}")

format_spec can be : , or .2f or .2e etc

Use a f-string with syntaxe {<value>:.<p>e} where <value> 
is the value to display and <p> the number you want after the ","

ou on peut utiliser la fonction format(y, ".2e")
"""

y = time.time()

print(f"Seconds since January 1, 1970: {y:,.4f}", f"or {y:.2e} in scientific notation")

#print("Seconds since January 1, 1970:", y, "or" , format(y, ".2e"), "in scientific notation")


x = datetime.datetime.now()

print(x.strftime("%b"), x.strftime("%d"), x.strftime("%Y"))