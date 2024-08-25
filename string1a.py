# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:24:06 2024

@author: Kim Quyên
"""

s = ("Đại học quốc gia, Khu phố 6, P.Linh Trung, Q.Thủ Đức, TP.HCM")

s1 = s.replace('P.','').replace('Q.','').replace('TP.','').split(', ')
for i in s1:
    print(i)