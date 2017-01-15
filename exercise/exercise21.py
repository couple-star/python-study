#Given a binary array, find the maximum number of consecutive 1s in this array.

binary=[1,1,0,0,0,0,1,1,1,1,1,0,0]
max_cnt = 0
cur_cnt = 0


for i in binary:
    if i == 1:
        cur_cnt += 1
        if cur_cnt > max_cnt:
            max_cnt = cur_cnt
    else:
        cur_cnt = 0

print max_cnt
