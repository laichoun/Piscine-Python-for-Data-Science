#!/usr/bin/env python3.10

def NULL_not_found(object: any) -> int:
    match   object:
        case None:
            print("Nothing: None", type(object))
            return (0)
        case float():
            print("Cheese: nan", type(object))
            return (0)
        case False:
            print("Fake: False", type(object))
            return (0)
        case "":
            print("Empty:", type(object))
            return (0)
        case 0:
            print("Zero: 0", type(object))
            return (0)
        case _:
            print("Type not Found")
            return (1)
