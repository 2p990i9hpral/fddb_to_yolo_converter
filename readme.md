# Dependency
* numpy
* tqdm
* cv2
  
  
# How to use
please download images and annotations from this page
* **FDDB**
-http://vis-www.cs.umass.edu/fddb/index.html#download

or direct link

* **images (552MB)**
-http://tamaraberg.com/faceDataset/originalPics.tar.gz
* **annotations (156KB)**
-http://vis-www.cs.umass.edu/fddb/FDDB-folds.tgz 

unzip the downloaded .zip files and move it to data folder

run fddb_to_yolo.py


below is folder structure

```
- fddb_to_yolo_converter
  - data
    - FDDB-folds
    - originalPics
  - fddb_to_yolo.py
``` 