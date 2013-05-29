import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix = record[0]
    row = record[1]
    column = record[2]
    value = record[3]
    if matrix == 'a':
        for k in range(5):
            mr.emit_intermediate((row,k),record)
    elif matrix == 'b':
        for k in range(5):
            mr.emit_intermediate((k,column),record)

def reducer(key, list_of_values):
    al={}
    bl={}
    for v in list_of_values:
        if v[0]=='a':
            al[v[2]]=v[3]
        elif v[0]=="b":
            bl[v[1]]=v[3]
    r = 0
    for k in range(5):
        if k in al and k in bl:
            r += al[k]*bl[k]
    n=[]
    n.append(key[0])
    n.append(key[1])
    n.append(r)
    mr.emit(tuple(n))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
