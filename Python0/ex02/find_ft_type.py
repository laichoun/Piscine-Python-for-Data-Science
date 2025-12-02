
#!/usr/bin/env python3.10

def all_thing_is_obj(object: any) -> int:
        match   object:
            case list():
                print("List :", type(object))
            case tuple():
                print("Tuple :", type(object))
            case set():
                print("Set :", type(object))
            case dict():
                print("Dict :", type(object))
            case "Brian":
                print("Brian is in the kitchen :", type(object))
            case "Toto":
                print("Toto is in the kitchen :", type(object))
            case _:
                print("Type not found$")
        return (42)

