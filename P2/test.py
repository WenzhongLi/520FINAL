#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
IniUti = [100,90,80,70,60,50,40,30,20,-10]
beta = 0.9
UpdateUti =[0,0,0,0,0,0,0,0,0,0]
PolicyIndex =[0,0,0,0,0,0,0,0,0,1] # 0 is use, 1 is replace
for i in range(1,1000):
    U_new = 100 + beta*IniUti[1]
    U_used1 = [90 + beta * (0.9 * IniUti[1] + 0.1 * IniUti[2]), -250 + beta * IniUti[0]]
    U_used2 = [80 + beta * (0.8 * IniUti[2] + 0.2 * IniUti[3]), -250 + beta * IniUti[0]]
    U_used3 = [70 + beta * (0.7 * IniUti[3] + 0.3 * IniUti[4]), -250 + beta * IniUti[0]]
    U_used4 = [60 + beta * (0.6 * IniUti[4] + 0.4 * IniUti[5]), -250 + beta * IniUti[0]]
    U_used5 = [50 + beta * (0.5 * IniUti[5] + 0.5 * IniUti[6]), -250 + beta * IniUti[0]]
    U_used6 = [40 + beta * (0.4 * IniUti[6] + 0.6 * IniUti[7]), -250 + beta * IniUti[0]]
    U_used7 = [30 + beta * (0.3 * IniUti[7] + 0.7 * IniUti[8]), -250 + beta * IniUti[0]]
    U_used8 = [20 + beta * (0.2 * IniUti[8] + 0.8 * IniUti[9]), -250 + beta * IniUti[0]]
    U_dead = -250 + beta * IniUti[0]
    UpdateUti[0] = U_new
    UpdateUti[1] = max(U_used1)
    PolicyIndex[1] = U_used1.index(max(U_used1))
    UpdateUti[2] = max(U_used2)
    PolicyIndex[2] = U_used2.index(max(U_used2))
    UpdateUti[3] = max(U_used3)
    PolicyIndex[3] = U_used3.index(max(U_used3))
    UpdateUti[4] = max(U_used4)
    PolicyIndex[4] = U_used4.index(max(U_used4))
    UpdateUti[5] = max(U_used5)
    PolicyIndex[5] = U_used5.index(max(U_used5))
    UpdateUti[6] = max(U_used6)
    PolicyIndex[6] = U_used6.index(max(U_used6))
    UpdateUti[7] = max(U_used7)
    PolicyIndex[7] = U_used7.index(max(U_used7))
    UpdateUti[8] = max(U_used8)
    PolicyIndex[8] = U_used8.index(max(U_used8))
    UpdateUti[9] = U_dead
    # if abs(IniUti[1] - UpdateUti[1])<0.0000001 :
    #     break
    # else:
    IniUti = UpdateUti
    print(IniUti)
    print(PolicyIndex)