select A.row_num, B.col_num, sum(A.value * B.value)

from A join B on A.col_num = B.row_num

--and A.row_num = 2 and B.col_num = 3

group by A.row_num, B.col_num
;
