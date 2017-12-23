#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
import copy
import sys
import bfs as Search


class maze(object):
    # highest probability of containing the target.
    def __init__(self):
        self.d = None
        self.m = [
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
    [-1, 0,-1,-1,-1,-1, 0,-1,-1,-1,-1, 0,-1, 0,-1,-1,-1,-1, 0,-1,-1,-1,-1, 0,-1, 0,-1,-1,-1,-1, 0,-1,-1,-1,-1, 0,-1],
    [-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1],
    [-1, 0,-1, 0,-1,-1,-1,-1,-1, 0,-1, 0,-1, 0,-1, 0,-1,-1,-1,-1,-1, 0,-1, 0,-1, 0,-1, 0,-1,-1,-1,-1,-1, 0,-1, 0,-1],
    [-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1],
    [-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1],
    [-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1],
    [-1, 0,-1, 0,-1,-1, 0,-1,-1, 0,-1, 0,-1, 0,-1, 0,-1,-1, 0,-1,-1, 0,-1, 0,-1, 0,-1, 0,-1,-1, 0,-1,-1, 0,-1, 0,-1],
    [-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1],
    [-1, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0,-1, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0,-1, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0,-1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
    [-1, 0,-1,-1,-1,-1, 0,-1,-1,-1,-1, 0,-1, 0,-1,-1,-1,-1, 0,-1,-1,-1,-1, 0,-1, 0,-1,-1,-1,-1, 0,-1,-1,-1,-1, 0,-1],
    [-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1],
    [-1, 0,-1, 0,-1,-1,-1,-1,-1, 0,-1, 0,-1, 0,-1, 0,-1,-1,-1,-1,-1, 0,-1, 0,-1, 0,-1, 0,-1,-1,-1,-1,-1, 0,-1, 0,-1],
    [-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1],
    [-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1],
    [-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1],
    [-1, 0,-1, 0,-1,-1, 0,-1,-1, 0,-1, 0,-1, 0,-1, 0,-1,-1, 0,-1,-1, 0,-1, 0,-1, 0,-1, 0,-1,-1, 0,-1,-1, 0,-1, 0,-1],
    [-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1],
    [-1, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0,-1, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0,-1, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0,-1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
    [-1, 0,-1,-1,-1,-1, 0,-1,-1,-1,-1, 0,-1, 0,-1,-1,-1,-1, 0,-1,-1,-1,-1, 0,-1, 0,-1,-1,-1,-1, 0,-1,-1,-1,-1, 0,-1],
    [-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1],
    [-1, 0,-1, 0,-1,-1,-1,-1,-1, 0,-1, 0,-1, 0,-1, 0,-1,-1,-1,-1,-1, 0,-1, 0,-1, 0,-1, 0,-1,-1,-1,-1,-1, 0,-1, 0,-1],
    [-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1],
    [-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1],
    [-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1, 0,-1, 0,-1, 0, 0, 0,-1, 0,-1, 0,-1],
    [-1, 0,-1, 0,-1,-1, 0,-1,-1, 0,-1, 0,-1, 0,-1, 0,-1,-1, 0,-1,-1, 0,-1, 0,-1, 0,-1, 0,-1,-1, 0,-1,-1, 0,-1, 0,-1],
    [-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1],
    [-1, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0,-1, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0,-1, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0,-1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
        self.current = None

    def print_m(self):
        for row in self.current:
            for point in row:
                if point == -1:
                    print '\033[1;35m\033[0m'+"BBB",
                elif 0 <= point < 10:
                    print '\033[0m'+"  "+str(point),
                elif 10 <= point < 100:
                    print '\033[0m'+" "+str(point),
                else:
                    print str(point),
            print '\n',

    def init1(self):
        self.current = copy.deepcopy(self.m)
        for y in range(len(self.m)):
            for x in range(len(self.m)):
                if self.current[y][x] != -1:
                    self.current[y][x] = 1

    def one_step(self,d):
        # up 0, right 1, down 2, left 3
        dir = [(-1,0),(0,1),(1,0),(0,-1)]
        new_m = copy.deepcopy(self.m)
        for y in range(len(new_m)):
            for x in range(len(new_m)):
                if new_m[y][x] == -1:
                    continue
                elif new_m[y+dir[d][0]][x+dir[d][1]] == -1:
                    # print y,x,y+dir[d][0],x+dir[d][1]
                    new_m[y][x] += self.current[y][x]
                else:
                    new_m[y + dir[d][0]][x + dir[d][1]] += self.current[y][x]
        self.current = new_m

    def check_around(self, yi):
        dir = [(1, 0), (1, 1), (0, 1), (-1, 1),(-1,0),(-1,-1),(0,-1),(1,-1)]
        for y in range(len(self.m)):
            for x in range(len(self.m)):
                if self.current[y][x] != -1:
                    count = 0
                    for d in dir:
                        if self.current[y+d[0]][x+d[1]] == -1:
                            count += 1
                    if count != yi:
                        self.current[y][x] = 0

    def bfs_init(self):
        current = copy.deepcopy(self.m)
        for y in range(37):
            for x in range(37):
                if self.m[x][y] == 0:
                    bfs = Search.BFS()
                    r = bfs.bfs_init(copy.deepcopy(self.m), 37, (x, y), (30, 30))
                    # print r[1]
                    # print r[1][-2:-1]
                    st = r[1][-1]
                    if st == (30,30):
                        current[x][y] = -1
                        continue
                    nt = r[1][-2]
                    d = -1
                    if st[0] == nt[0]:  # row
                        if st[1] < nt[1]:  # col
                            # right
                            d = 1
                        else:
                            d = 3
                    else:
                        if st[0] < nt[0]:  # col
                            # down
                            d = 2
                        else:
                            d = 0
                    current[x][y] = d

        for x in range(37):
            for y in range(37):
                if current[x][y] == -1:
                    print '\033[1;35m\033[0m'+"B",
                else:
                    print '\033[0m'+str(current[x][y]),

            print '\n',

        self.d = current

    def find_best(self):
        self.init1()
        self.bfs_init()
        sq = []
        maze.print_m()
        dir = [1, 1, 2, 2, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0]

        for thisd in dir:
            self.one_step(thisd)
            self.print_m()

        last_step = -1
        while self.current[30][30] < 348:
            count = [0, 0, 0, 0]
            for x in range(37):
                for y in range(37):
                    if self.m[x][y] != -1:
                        if 26<x<34 and 26<y<34:
                            continue
                        ni = self.current[x][y]
                        di = self.d[x][y]
                        count[di] += ni
            max1 = -1
            max1_index = -1
            max2 = -1
            max2_index = -1
            for j in range(len(count)):
                if max1 == -1:
                    max1 = count[j]
                    max1_index = j
                    continue
                elif max2 == -1:
                    if count[j] > max1:
                        max2 = max1
                        max2_index = max1_index
                        max1 = count[j]
                        max1_index = j
                        continue
                    else:
                        max2 = count[j]
                        max2_index = j
                        continue
                if count[j] > max2:
                    if count[j] > max1:
                        max2 = max1
                        max2_index = max1_index
                        max1 = count[j]
                        max1_index = j

                    else:
                        max2 = count[j]
                        max2_index = j
            print last_step, max1_index, max1, max2_index, max2, count
            if max1_index == ((last_step+2)%4):
                max1_index = max2_index

            last_step = max1_index
            count_outside = 0
            for c in count:
                count_outside += c
            if count_outside < 10:
                break
            print "run",
            print max1_index
            sq.append(max1_index)
            self.one_step(max1_index)
            self.print_m()
        print sq


if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argment", i, sys.argv[i]
    print ('start initialize')
    # -------------test------------------
    # maze = maze()
    # maze.find_best()
    # -------------game------------------
    maze = maze()
    maze.init1()
    maze.print_m()
    data_in = []
    while(1):
        data = raw_input()
        if len(data)>1:
            for d in data:
                dint = int(d)
                data_in.append(dint)
                # print data
                maze.one_step(dint)
                maze.print_m()
            continue
        data = int(data)
        if data == 9:
            print data_in
            break
        data_in.append(data)
        # print data
        maze.one_step(data)
        maze.print_m()
    # -------------around-------------------
    # ys = [5,5,5]
    # actions = [1,1]
    # maze = maze()
    # maze.init1()
    # maze.check_around(ys[0])
    # maze.print_m()
    # for j in range(len(actions)):
    #     maze.one_step(actions[j])
    #     maze.check_around(ys[j+1])
    #     maze.print_m()
    # count = 0
    # for x in range(37):
    #     for y in range(37):
    #         if maze.current[x][y] == 1:
    #             count+=1
    # print count
    # --------------------------------------
    # maze = maze()
    # maze.bfs_init()
    # maze = maze()
    # bfs = Search.BFS()
    # r = bfs.bfs_init(copy.copy(maze.m), 37, (2,6), (30,30))
    # print r[1]
    # print r[1][-2:-1]
    # st = r[1][-1]
    # nt = r[1][-2]
    # d = -1
    # if st[0] == nt[0]:#row
    #     if st[1] < nt[1]:#col
    #         #right
    #         d = 1
    #     else:
    #         d = 3
    # else:
    #     if st[0] < nt[0]:#col
    #         #down
    #         d = 2
    #     else:
    #         d = 0
    #
    # m = copy.copy(maze.m)
    # for y in range(37):
    #     for x in range(37):
    #         if m[y][x] == -1:
    #             print '\033[1;35m\033[0m'+"BBB",
    #         elif (y,x) in r[1]:
    #             print '\033[0m'+"RRR",
    #         elif (y,x) not in r[1]:
    #             print '\033[0m'+"   ",
    #         else:
    #             print "error",
    #     print '\n',




