#!/usr/bin/env python
# -*- coding: utf-8 -*

# l = [{'data': [{'bottom': 222, 'confidence': 0.998528003692627, 'left': 408, 'right': 438, 'top': 183}, {'bottom': 300, 'confidence': 0.9981206059455872, 'left': 590, 'right': 619, 'top': 264}, {'bottom': 142, 'confidence': 0.9970307350158691, 'left': 201, 'right': 239, 'top': 101}, {'bottom': 184, 'confidence': 0.9941745400428772, 'left': 303, 'right': 333, 'top': 146}, {'bottom': 72, 'confidence': 0.9938634634017944, 'left': 123, 'right': 155, 'top': 35}, {'bottom': 282, 'confidence': 0.9924627542495728, 'left': 491, 'right': 519, 'top': 245}, {'bottom': 143, 'confidence': 0.9895480871200562, 'left': 316, 'right': 341, 'top': 110}, {'bottom': 194, 'confidence': 0.9665833711624146, 'left': 436, 'right': 462, 'top': 166}], 'path': 'ndarray_time=1683535876296669.0'}]
l = [{'data': [{'bottom': 147, 'confidence': 0.8640711903572083, 'left': 118, 'right': 161, 'top': 104}], 'path': 'ndarray_time=1683371449682014.0'}]


l = l[0]['data']

print(type(l))

# d["confidence"] = round(d["confidence"], 2)
# d["识别的置信度"] = d.pop("confidence")
#print(d['left'],d['top'],d['right'],d['bottom'])

for d in l:
    print(d['left'],d['top'],d['right'],d['bottom'])
    # for k, v in d.items():
    #      print(k , v)