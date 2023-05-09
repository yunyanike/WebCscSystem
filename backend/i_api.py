#!/usr/bin/env python
# -*- coding: utf-8 -*
import requests
import json
import cv2
import base64
def cv2_to_base64(image):
    data = cv2.imencode('.jpg', image)[1]
    return base64.b64encode(data.tobytes()).decode('utf8')

imgPath = "C:/Users/Administrator/Desktop/timg/1.jpg"
# 发送HTTP请求
data = {'images':[cv2_to_base64(cv2.imread(imgPath))]}
headers = {"Content-type": "application/json"}
url = "http://47.107.240.92:19003/predict/pyramidbox_lite_mobile"
#print(url)
r = requests.post(url=url, headers=headers, data=json.dumps(data))

# 打印预测结果
l = r.json()["results"][0]['data']
print(type(l))

img = cv2.imread(imgPath)

for d in l:
    print(d['left'],d['top'],d['right'],d['bottom'])
    cv2.rectangle(
        img,
        (d['left'], d['top']),
        (d['right'], d['bottom']),
        (255, 0, 0),  # 蓝色
        thickness=2
    )

# l0 = l[0]
#
# print(l0['left'],l0['top'])
# print(l0['right'],l0['bottom'])
# img = cv2.imread(imgPath)
#
# cv2.rectangle(
#     img,
#     (l0['left'], l0['top']),
#     (l0['right'], l0['bottom']),
#     (255, 0, 0),  # 蓝色
#     thickness=2)

cv2.imshow('src',img)
cv2.waitKey()