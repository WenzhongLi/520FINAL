#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''


b = 0.9
new_utility =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
policy =[0, 0, 0, 0, 0, 0, 0, 0, 0, 1] # 0 is use, 1 is replace
utility_used = [0,0,0,0,0,0,0,0,0,0]
init_utility = [100, 90, 80, 70, 60, 50, 40, 30, 20, -10]
for i in range(2000):
    new_utility_this_round = 100 + b * init_utility[1]
    j = 1
    for j in range(1,9):
        utility_used[j] = [100 - 10 * j + b * ((1 - j * 0.1) * init_utility[j] + j * 0.1 * init_utility[j + 1]),
                           -250 + b * init_utility[0]]

    utility_dead = -250 + b * init_utility[0]
    new_utility[0] = new_utility_this_round
    for j in range(1,9):
        new_utility[j] = max(utility_used[j][0], utility_used[j][1])
        policy[j] = utility_used[j].index(max(utility_used[j]))

    new_utility[9] = utility_dead

    init_utility = new_utility
    print(init_utility)
    print(policy)