# Convert2YoloDist

Object Detection annotation Convert to [Yolo Darknet](https://pjreddie.com/darknet/yolo/) Format with the distance

Support DataSet : 

1. COCO                      : not suport
2. VOC                       : not suport
3. UDACITY Object Detection  : not suport
4. KITTI 2D Object Detection : not suport

​    

## Pre-Requiredment

```
pip3 install -r requirements.txt
```

​    

## Required Parameters

each dataset requried some parameters

see [example.py](https://github.com/ssaru/convert2Yolo/blob/master/example.py)

1. --datasets

   - like a COCO / VOC / UDACITY / KITTI

     ```bash
     --datasets COCO
     ```

2. --img_path

   - it directory path. not file path

     ```bash
     --img_path ./example/kitti/images/
     ```

3. --label

   - it directory path. not file path

     (some datasets give label `*.json` or `*.csv` . this case use file path)

     ```bash
     --label ./example/kitti/labels/
     ```

     OR

     ```bash
     --label ./example/kitti/labels/label.json
     
     or
     
     --label ./example/kitti/labels/label.csv
     ```

4. --convert_output_path

   - it directory path. not file path

     ```bash
     --convert_output_path ./
     ```

5. --img_type

   - like a `*.png`, `*.jpg`

     ```bash
     --img_type ".jpg"
     ```

6. --manifest_path

   - it need train yolo model in [darknet framework](https://pjreddie.com/darknet/)

     ```bash
     --manifest_path ./
     ```

7. --cla_list_file(`*.names`)

   - it is `*.names` file contain class name. refer [darknet `*.name` file](https://github.com/pjreddie/darknet/blob/master/data/voc.names)

     ```bash
     --cls_list_file voc.names
     ```

​    

### *.names file example

```
aeroplane
bicycle
bird
boat
bottle
bus
car
cat
chair
cow
diningtable
dog
horse
motorbike
person
pottedplant
sheep
sofa
train
tvmonitor
```

​    

## Example

​    

### 1. example command

```bash
python3 example.py --datasets [COCO/VOC/KITTI/UDACITY] --img_path <image_path> --label <label path or annotation file> --convert_output_path <output path> --img_type [".jpg" / ".png"] --manifest_path <output manipast file path> --cls_list_file <*.names file path>

>>
ex) python3 example.py --datasets KITTI --img_path ./example/kitti/images/ --label ./example/kitti/labels/ --convert_output_path ./ --img_type ".jpg" --manifest_path ./ --cls_list_file names.txt
```

​    
