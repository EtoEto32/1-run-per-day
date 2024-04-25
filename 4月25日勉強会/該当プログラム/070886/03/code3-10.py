from collections import OrderedDict

dict_a = {"a": 10, "b": 200, "c": 300}
dict_b = {"a": 10, "c": 300, "b": 200}

od_a = OrderedDict(dict_a)
od_b = OrderedDict(dict_b)
od_a.move_to_end("a")
print(od_a)
od_a.move_to_end("a", last=False)
print(od_a)