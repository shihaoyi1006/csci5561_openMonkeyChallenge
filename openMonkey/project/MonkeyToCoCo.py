import json
import os
import cv2
import numpy as np



def addImage (id, filename, height, width):
	newJson = {
            "id": id,
            "file_name": filename,
            "height": height,
            "width": width
	}
	return newJson

def addAnnotations(id,bbox,category,keypoints):
	newJson = {      
            "keypoints": keypoints,
            "image_id": id,
            "id": id,
            "num_keypoints": 17,
            "bbox": [
                bbox[0],
                bbox[1],
            	bbox[2],
                bbox[3]
            ],
            "category_id": 1,

        }
	return newJson 

exportJson = {
    "categories": [
        {
            "supercategory": "animal",
            "id": 1,
            "name": "monkey",
            "keypoints": [
                "right_eye",
                "left_eye",
                "nose",
                "head",
                "neck",
                "right_shoulder",
                "right_elbow",
                "right_wrist",
                "left_shoulder",
                "left_elbow",
                "left_wrist",
                "hip",
                "right_knee",
                "right_ankle",
                "left_knee",
                "left_ankle",
                "tail"
            ],
            "skeleton": [
                [
                    2,0
                ],
                [
                    2,1
                ],
                [
                   3,4
                ],
                [
                  4,5
                ],
                [
                    4,8
                ],
                [
                    5,6
                ],
                [ 8,9],
                [
                    6,
                    7
                ],
                [
                    9,10
                ],
                [
                   4,11
                ],
                [
                   11,16
                ],
                [
                   11,12
                ],
                [
                   11,14
                ],
                [
                   12,13
                ],
                [
                   14,15
                ]
            ]
        }
    ]
}
exportJson["images"] = []
exportJson["annotations"] = []



filepath = "./test_json_catecories/test_old_monkey.json"
exportPath = "./new_test_old_monkey.json"
imgPath = "../test/"
with open(filepath, 'r') as fp:
	information = json.load(fp)
	# print(len(information["data"]))
	for i in range(len(information["data"])):
		# get id
		file = information["data"][i]["file"]
		tempId = file.split("_")
		id = int(tempId[1][0:len(tempId[1])-4])
		# get bbx
		bbox = information["data"][i]["bbox"]

		# get landmarks
		# landmarks = information["data"][i]["landmarks"]
		# temp = []
		# count = 0
		# for i in range(len(landmarks)):
		# 	temp.append(landmarks[i])
		# 	count+=1
		# 	if(count == 2):
		# 		temp.append(2)
		# 		count = 0

		# get category
		category = information["data"][i]["species"]
		# get h and w
		path = imgPath+file
		im = cv2.imread(path,0)
		# print(path)
		h= im.shape[0]
		w = im.shape[1]
		curImg = addImage(id,file,h,w)
		# curAnnatation = addAnnotations(id,bbox,category,temp)
		curAnnatation = addAnnotations(id,bbox,category,[])
		exportJson["images"].append(curImg)
		exportJson["annotations"].append(curAnnatation)

with open(exportPath, 'w') as fp:
	json.dump(exportJson, fp, indent=4)

	
#python demo/top_down_img_demo.py configs/body/2d_kpt_sview_rgb_img/topdown_heatmap/coco/hrnet_w48_coco_256x192.py https://download.openmmlab.com/mmpose/top_down/hrnet/hrnet_w48_coco_256x192-b9e0b3ab_20200708.pth --img-root duke/aa --json-file duke/test_prediction.json --out-img-root vis_results