import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
  for lefttable in list_of_values:
    for righttable in list_of_values:
      if lefttable[0] == "order" and righttable[0] == "line_item":
        mr.emit(lefttable + righttable)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
