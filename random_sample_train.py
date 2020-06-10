import os
import random
import numpy as np

ratio = 0.1

with open('data/VOCdevkit/VOC2007/ImageSets/Main/trainval.txt', 'r') as f:
    trainval_07 = f.readlines()
    len_07 = len(trainval_07)
    np.random.shuffle(trainval_07)
    new_trainval_07 = trainval_07[:int(len_07 * ratio)] * int((1/ratio))
    trainval_07_pool = trainval_07[int(len_07 * ratio):]
    if len(new_trainval_07) < len_07:
        new_trainval_07.extend(new_trainval_07[:len_07 - len(new_trainval_07)])
    print(len(new_trainval_07))

with open('data/VOCdevkit/VOC2007/ImageSets/Main/trainval_{}.txt'.format(int(ratio*100)), 'w') as f:
    for line in new_trainval_07:
        f.write(line)

with open('data/VOCdevkit/VOC2012/ImageSets/Main/trainval.txt', 'r') as f:
    trainval_12 = f.readlines()
    len_12 = len(trainval_12)
    np.random.shuffle(trainval_12)
    new_trainval_12 = trainval_12[:int(len_12 * ratio)] * int((1/ratio))
    trainval_12_pool = trainval_12[int(len_12 * ratio):]
    if len(new_trainval_12) < len_12:
        new_trainval_12.extend(new_trainval_12[:len_12 - len(new_trainval_12)])
    print(len(new_trainval_12))

with open('data/VOCdevkit/VOC2012/ImageSets/Main/trainval_{}.txt'.format(int(ratio*100)), 'w') as f:
    for line in new_trainval_12:
        f.write(line)

with open('data/VOCdevkit/VOC2012/ImageSets/Main/trainval_pool.txt', 'w') as f:
    for line in trainval_12_pool:
        f.write(line)

with open('data/VOCdevkit/VOC2007/ImageSets/Main/trainval_pool.txt', 'w') as f:
    for line in trainval_07_pool:
        f.write(line)