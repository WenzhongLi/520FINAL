#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
# import math


class means(object):
    def __init__(self):
        self.a = [[[1,1,0,0,0],
                [0,1,1,0,0],
                [0,1,0,0,0],
                [1,0,0,0,0],
                [0,0,0,0,0]
                ],[
                [1,1,0,0,0],
                [0,0,1,0,0],
                [1,0,0,0,0],
                [0,0,1,0,0],
                [0,0,0,0,0]
                ],[
                [0,1,0,0,0],
                [1,1,0,0,0],
                [1,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]
                ],[
                [1,1,0,0,0],
                [1,0,1,0,0],
                [0,1,0,1,0],
                [0,0,0,0,0],
                [0,0,1,0,0]
                ],[
                [0,1,1,0,0],
                [1,1,0,0,1],
                [0,1,0,0,0],
                [0,0,1,0,0],
                [0,0,0,0,0]]]
        self.b = [[[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,1,0],
                [0,0,0,0,1],
                [0,0,1,1,1]
                ],[
                [0,0,0,0,0],
                [1,0,0,0,0],
                [0,0,0,0,0],
                [1,0,1,0,1],
                [0,1,0,1,1]
                ],[
                [0,1,0,0,0],
                [0,0,0,1,0],
                [1,0,0,1,0],
                [0,0,0,1,1],
                [0,0,0,1,0]
                ],[
                [1,0,0,0,0],
                [0,0,0,0,0],
                [0,0,1,0,0],
                [0,0,0,1,1],
                [0,1,0,1,0]
                ],[
                [0,0,0,0,0],
                [0,1,0,0,1],
                [0,0,0,0,1],
                [0,0,0,0,0],
                [0,0,1,1,1]]]
        self.m = [[[1,0,0,0,0],
                [1,0,1,0,1],
                [0,0,0,0,0],
                [0,0,1,1,1],
                [0,0,0,1,0]],
                [
                [1,1,1,0,0],
                [1,1,1,0,0],
                [0,0,1,1,0],
                [0,0,0,0,0],
                [1,0,1,0,0]],
                [
                [0,0,0,0,1],
                [0,0,0,0,1],
                [0,0,0,1,1],
                [0,0,0,0,1],
                [0,1,0,1,1]],
                [
                [0,1,1,0,0],
                [1,1,0,0,0],
                [0,1,1,0,0],
                [0,1,0,0,1],
                [0,0,0,0,0]],
                [
                [1,0,0,0,1],
                [0,0,0,0,0],
                [0,0,1,0,0],
                [0,0,0,0,0],
                [1,0,0,0,1]]]

    def knn(self, t, k):
        a_distance = []
        b_distance = []
        for ma in self.a:
            a_distance.append(self.distance(ma,t))
        for mb in self.b:
            b_distance.append(self.distance(mb,t))

        a_distance.sort()
        b_distance.sort()
        print a_distance, b_distance
        count_a = 0
        count_b = 0
        index_a = 0
        index_b = 0
        for x in range(k):

            if a_distance[index_a] < b_distance[index_b]:
                count_a+=1
                index_a+=1
            else:
                count_b += 1
                index_b += 1

        if count_a > count_b:
            print "a"
        else:
            print "b"
    def distance(self,v1,v2):
        count = 0
        for x in range(len(v1)):
            for y in range(5):
                count += abs(v1[x][y] - v2[x][y])
        return count



    def co_mean(self):
        A_means = 0
        B_means = 0
        # for

if __name__ == "__main__":
    nn = means()
    nn.knn(nn.m[0],5)
    nn.knn(nn.m[1], 5)
    nn.knn(nn.m[2], 5)
    nn.knn(nn.m[3], 5)
    nn.knn(nn.m[4], 5)