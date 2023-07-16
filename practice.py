import random
symbols={
    "a":4,
    "b":4,
    "c":4,
    "d":4
}

values={
    "a":2,
    "b":3,
    "c":6,
    "d":1
}

valarray=[]
arrays=[]
ROWS=3
COLS=3

for key,i in symbols.items():
    for _ in range(i):
        valarray.append(key)

for _ in range(COLS):
    column=[]
    temparr=valarray[:]
    for _ in range(ROWS):
        val=random.choice(temparr)
        column.append(val)
        temparr.remove(val)
    arrays.append(column)

print(arrays)
#now we have to print 
for i in range(len(arrays[0])):
    for num,col in enumerate(arrays):
        if num != len(col)-1: 
            print(col[i],end="|")
        else:
            print(col[i],end="")
    print("")

line=2
for line in range(line):
    sym=arrays[0][line]
    print(sym)
    for col in arrays:
        symbol_chk=col[line]
        print(symbol_chk)
        
