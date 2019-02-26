def randDir(n):
    from random import randint
    a = []
    for i in range(1, n):
        u = randint(0, 3)
        if (u == 0):
            a.append("NORTH")
        elif (u == 1):
            a.append("SOUTH")
        elif (u == 2):
            a.append("WEST")
        else:
            a.append("EAST")
    return a

def dirReducTest(arr):
    import re
    s = ",".join(arr)
    nd = True
    while nd:
        ss = re.sub(r"NORTH,SOUTH|SOUTH,NORTH|EAST,WEST|WEST,EAST", "", s)
        ss = re.sub(r"^,|,$", "",ss)
        ss = re.sub(",,", ",",ss)
        if ss == s:
            nd = False
        else:
            s = ss
    if s != "":
        return s.split(",")
    else:
        return []

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"] # ['WEST']
test.assert_equals(dirReduc(a), ['WEST'])
a = ["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH","WEST", "EAST"] # ['NORTH', 'NORTH']
test.assert_equals(dirReduc(a), ['NORTH', 'NORTH'])
a = [] # []
test.assert_equals(dirReduc(a), [])
a=["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"] # []
test.assert_equals(dirReduc(a), [])
a = ["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","NORTH"] # ["NORTH"]
test.assert_equals(dirReduc(a), ["NORTH"])
a = ["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"] # ["EAST", "NORTH"]
test.assert_equals(dirReduc(a), ["EAST", "NORTH"])
a = ["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"] # ["NORTH", "EAST"])
test.assert_equals(dirReduc(a), ["NORTH", "EAST"])
a = ["NORTH", "WEST", "SOUTH", "EAST"] # ["NORTH", "WEST", "SOUTH", "EAST"])
test.assert_equals(dirReduc(a), ["NORTH", "WEST", "SOUTH", "EAST"])
a = ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH']
test.assert_equals(dirReduc(a), ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH'])
# ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH']
u = randDir(11)
test.assert_equals(dirReduc(u), dirReducTest(u))
u = randDir(11)
test.assert_equals(dirReduc(u), dirReducTest(u))
u = randDir(11)
test.assert_equals(dirReduc(u), dirReducTest(u))
u = randDir(11)
test.assert_equals(dirReduc(u), dirReducTest(u))
u = randDir(15)
test.assert_equals(dirReduc(u), dirReducTest(u))
