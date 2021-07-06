# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 15:32:44 2021

@author: 86158
"""
#%%question1


import json
with open('./boxes.json','r',encoding='utf8')as fp:  #用字典读取
    json_data = json.load(fp)

for key in  json_data['boxes'][1].keys(): #打印 'rectangle'
    if key == 'rectangle':
        print(key)

    
#%% question2

from PIL import Image

def Picture_Synthesis(M_Img
                      ,S_Img
                      ,factor = (1,1)
                      ,left_top = (100,100)
                      ,right_bottom = (200,300)
                      ):
    """
    :param M_Img: 母图
    :param S_Img: 子图
    :param foctor: 缩放因子
    :param left_top，right_bottom: 子图在母图的填充区域
    :return:
    """
    
    # 获取图片的尺寸
    M_Img_w, M_Img_h = M_Img.size  # 获取被放图片的大小（母图）
    print("母图尺寸：",M_Img.size)
    S_Img_w, S_Img_h = S_Img.size  # 获取小图的大小（子图）
    print("子图尺寸：",S_Img.size)
    
    if M_Img_w>right_bottom[0] and M_Img_h>right_bottom[1]:
        
        # 对子图尺寸进行缩放
        S_Img_w = int(S_Img_w/factor[0])
        S_Img_h = int(S_Img_h/factor[1])

        size_w = int(right_bottom[0] - left_top[0])
        size_h = int(right_bottom[1] - left_top[1])

        # 防止子图尺寸大于母图所给区域
        if S_Img_w > size_w:
            S_Img_w = size_w
        if S_Img_h > size_h:
            S_Img_h = size_h
 
        # # 重新设置子图的尺寸
        S_Img_reshape = S_Img.resize((S_Img_w, S_Img_h))
        
        coordinate = left_top

        M_Img.paste(S_Img_reshape, coordinate, mask=None)
    
        return M_Img
    
    else:
        print('给定区域超出母图范围')
        
       
    
