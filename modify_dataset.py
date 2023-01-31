#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 22:26:11 2023

@author: welcome870117
"""

import pandas as pd
import numpy as np

def modify_eng_recog_label(total_data, modify_index_in_dataset):

  for index in modify_index_in_dataset:
    # 與原本dataset配對, 1.遍歷 / 2.利用dataframe找value
    label = total_data['label'][index]
    print(index)
    print('---'*15)

    if label == 1:
        total_data['label'][index] = 0
    else:
        total_data['label'][index] = 1

  return  total_data

def modify_3class_label(df_modify, df_class3):
    #取modify label = 0 
    text = df_modify[df_modify['modify label']==0]['text']
    drop_index = []
    
    print(len(text))
    for text_ in text:
        index_ = df_class3.index[df_class3['text']==text_].to_list()[0]
        drop_index.append(index_)
        
    df_class3.drop(index=drop_index,inplace=True)

    return df_class3.reset_index(drop=True)
  
def modify_4class_label(df_modify, df_class4, label0_to_1):

    #如果是1改0 -> 原本label改為3
    text = df_modify[df_modify['modify label']==0]['text']
    
    for text_ in text:
        index_ = df_class4.index[df_class4['text']==text_].to_list()[0]
        print(index_)
        df_class4['label'][index_] = 3
    
    print('---'*15)
    #如果是0改再判斷
    text = df_modify[df_modify['modify label']==1]['text']
    for text_, label in zip(text,label0_to_1):
        index_ = df_class4.index[df_class4['text']==text_].to_list()[0]
        print(index_)
        df_class4['label'][index_] = label
    
    return df_class4
        
#修改前後對比
def compare_bna(origin_data, modify_data):
    if len(origin_data) != len(modify_data):
        pass
    
    else:
        origin_data_label = np.array(origin_data['label'])
        modify_label_data = np.array(modify_data['label'])
        diff_index = np.where(origin_data_label != modify_label_data)
        '''
        print('different index:', diff_index[0])
        #for index in diff_index:
        print('text:', origin_data['text'][diff_index[0]])
        print('original label :', origin_data['label'][diff_index[0]])
        print('modify label:', modify_data['label'][diff_index[0]])
        print('---'*15)
        '''
        df = pd.DataFrame({'text':origin_data['text'][diff_index[0]], 'original label':origin_data['label'][diff_index[0]], 'modify label':modify_data['label'][diff_index[0]]})
        return df

def drop_unname(data):
    data.drop(columns=['Unnamed: 0'],inplace=True)
    return data

 #%%
if __name__ == '__main__':
    # read csv
    enlish_recog_v9 = pd.read_csv('/Users/welcome870117/Desktop/git_project/XLNet/dataset/AXS_datset_v9/AXS_recognize_english_dataset_v9.csv')
    class3_v9 = pd.read_csv('/Users/welcome870117/Desktop/git_project/XLNet/dataset/AXS_datset_v9/AXS_data_3class_v9.csv')
    class4_v9 = pd.read_csv('/Users/welcome870117/Desktop/git_project/XLNet/dataset/AXS_datset_v9/AXS_data_4class_v9.csv')
    
    #
    enlish_recog_v10 = enlish_recog_v9.copy()
    class3_v10 = class3_v9.copy()
    class4_v10 = class4_v9.copy()
    
    #
    #enlish_recog_v4 = enlish_recog_v4.dropna(axis=0).reset_index(drop=True)
    
    #
    modify_index_in_dataset =  [2435, 4422]
     #%%
    ### double check
    for index in modify_index_in_dataset:
        print(enlish_recog_v10['text'][index])
        print('---'*15)
    

    #%%
    #
    enlish_recog_v10 = modify_eng_recog_label(enlish_recog_v10, modify_index_in_dataset)
    
   # enlish_recog_v4 = drop_unname(enlish_recog_v3)
    
    #%%
    modify_df = compare_bna(enlish_recog_v9, enlish_recog_v10)
    #%%
    class3_v10 = modify_3class_label(modify_df, class3_v10)
    #
    #%%
    ## third input 判斷0->1的data情感分數
    class4_v10 = modify_4class_label(modify_df, class4_v10,[0])
    #%%
    # check area
    print(class4_v10['label'][4420])
    #%%
    # save file
    enlish_recog_v10.to_csv('/Users/welcome870117/Desktop/git_project/XLNet/dataset/AXS_datset_v10/AXS_recognize_english_dataset_v10.csv',index=False)
    class3_v10.to_csv('/Users/welcome870117/Desktop/git_project/XLNet/dataset/AXS_datset_v10/AXS_data_3class_v10.csv',index=False)
    class4_v10.to_csv('/Users/welcome870117/Desktop/git_project/XLNet/dataset/AXS_datset_v10/AXS_data_4class_v10.csv',index=False)
    
    #%%
    