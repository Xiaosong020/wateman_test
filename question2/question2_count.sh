#!/bin/bash

# Author ：Ni Xiaosong
# Created time ：2021/7/6

num=0

function readfile () {

 for file in `ls $1`
  do
   #这里的-d表示是一个directory，即目录/子文件夹
   if [ -d $1"/"$file ]
    then
    #如果子文件夹则递归
    readfile $1"/"$file
   else
    #读取该文件的文件名，文件名是否匹配关键字
    if [[ $file == *"_gt.json"* ]]; then
        num=$((num + 1))
    fi
  fi
 done
}

#函数定义结束，这里用来运行函数
readfile $1
echo $num 
