# -*-coding:utf-8-*-

import os
from xml.etree.ElementTree import dump
import json
import pprint

import argparse


from Format import KITTI, YOLO

parser = argparse.ArgumentParser(description='label Converting example.')
parser.add_argument('--datasets', type=str, help='type of datasets')
parser.add_argument('--img_path', type=str, help='directory of image folder')
parser.add_argument('--label', type=str,
                    help='directory of label folder or label file path')
parser.add_argument('--convert_output_path', type=str,
                    help='directory of label folder')
parser.add_argument('--img_type', type=str, help='type of image')
parser.add_argument('--manifest_path', type=str,
                    help='directory of manipast file', default="./")
parser.add_argument('--cls_list_file', type=str,
                    help='directory of *.names file', default="./")


args = parser.parse_args()


def main(config):

    if config["datasets"] == "KITTI":
        kitti = KITTI()
        print("Start to change!");
        yolo = YOLO(os.path.abspath(config["cls_list"]))

        flag, data = kitti.parse(
            config["label"], config["img_path"], img_type=config["img_type"])
        
        print("pass step 1!")
        if flag == True:
            flag, data = yolo.generate(data)
            
            print("pass step 2!")
            if flag == True:
                flag, data = yolo.save(data, config["output_path"], config["img_path"],
                                       config["img_type"], config["manifest_path"])
                print("pass step 3!")
                if flag == False:
                    print("Saving Result : {}, msg : {}".format(flag, data))

            else:
                print("YOLO Generating Result : {}, msg : {}".format(flag, data))

        else:
            print("KITTI Parsing Result : {}, msg : {}".format(flag, data))

    else:
        print("Unkwon Datasets")


if __name__ == '__main__':

    config = {
        "datasets": args.datasets,
        "img_path": args.img_path,
        "label": args.label,
        "img_type": args.img_type,
        "manifest_path": args.manifest_path,
        "output_path": args.convert_output_path,
        "cls_list": args.cls_list_file,
    }

    main(config)
