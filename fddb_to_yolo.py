import numpy as np
import os
import glob
from shutil import move
import cv2
from tqdm import tqdm
from collections import OrderedDict

postfix = 'ellipseList.txt'
anno_dir = 'data/FDDB-folds/'
img_dir = 'data/originalPics/'
dest_img_dir = 'data/converted_data/'

if __name__ == "__main__":

    if not os.path.isdir(dest_img_dir):
        os.mkdir(dest_img_dir)

    fold_path = []
    fold_path.extend(glob.glob(os.path.join(anno_dir, '*{}'.format(postfix))))

    list_dict = {}
    for fold in fold_path:
        with open(fold, 'r') as f:
            filelist = f.readlines()
        flag = True
        count = 0
        for i in filelist:
            x = i.replace('\n', '')
            if flag:
                path = x
                list_dict[path] = []
                flag = False
            elif count == 0:
                count = int(x)
            else:
                list_dict[path].append(x)
                count -= 1
                if count == 0:
                    flag = True

    for i in tqdm(list_dict):
        name = '_'.join(i.split('/'))
        src = os.path.join(img_dir, '{}.jpg'.format(i))
        dest = os.path.join(dest_img_dir, '{}.jpg'.format(name))

        img = cv2.imread(src)
        img_h, img_w = img.shape[:2]

        move(src, dest)

        annos = list_dict[i]
        annotations = OrderedDict()
        annotations['face'] = []
        for j in annos:
            anno = list(map(float, j.split(' ')[:-2]))
            rad = abs(anno[2])
            h = anno[0] * np.sin(rad)
            w = anno[1] * np.sin(rad)
            x1, x2 = anno[3] - w, anno[3] + w
            y1, y2 = anno[4] - h, anno[4] + h

            yolo_x, yolo_y = anno[3]/img_w, anno[4]/img_h
            yolo_w, yolo_h = (w*2)/img_w, (h*2)/img_h

            annotations['face'].append([yolo_x, yolo_y, yolo_w, yolo_h])

        with open(os.path.join(dest_img_dir, '{}.txt'.format(name)), 'w', encoding="utf-8") as m:
            for annotation_line in annotations['face']:
                m.write('0 ' + ' '.join(["{:.10f}".format(i) for i in annotation_line]) + "\n")
