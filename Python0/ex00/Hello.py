#!/usr/bin/env python3.10

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here

#first version

ft_list = ["Hello", "World!"]
ft_tuple = ("Hello", "Luxembourg!")
ft_set = {"Hello", "Belval!"}
# ft_dict = {"Hello" : "42Luxembourg!"}

#second version
ft_list[1] = "World!"

#tuple immuable donc on doit le reassigner
ft_tuple = ("Hello", "Luxembourg!")

ft_dict["Hello"] = "42Luxembourg!"





print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# private test : 
plateformes_sociales = {"Facebook" : "fb", "Instagram" : "insta", "Snapchat" : "snap", "Twitter" : "tweet", 12 : 120}
print(plateformes_sociales)
print (plateformes_sociales.keys())
print (plateformes_sociales.values())
print (plateformes_sociales.items())
print (plateformes_sociales.get("Instagram"))
# print (plateformes_sociales.pop("11"))
print (plateformes_sociales.pop(12))
print(plateformes_sociales)
print (plateformes_sociales.clear())
print(plateformes_sociales)

