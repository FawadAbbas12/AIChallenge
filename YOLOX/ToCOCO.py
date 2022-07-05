

import os
import json
from PIL import Image
class converter():
    def __init__(self, path):
        self.path = path
        self.img_id = 0
        self.ann_id = 0
        self.images = []
        self.annotations = []
        with open('datasets/annotations/test.json') as f: self.images =json.load(f)['images']
        with open(path) as f: self.data =json.load(f)['annotations']


    
    def process(self):
        # "image_id": 6991, "category_id": 1, "bbox": [1274.639404296875, 340.2280578613281, 3.573974609375, 26.066162109375], "score": 0.0024325891863554716, "segmentation": []},
        for ann in self.data:
            newann = {}
            newann['image_id'] = ann['image_id']
            newann['category_id'] = ann['category_id']
            newann['bbox'] = ann['bbox']
            newann['confidence'] = ann['confidence']
            newann['id'] = self.ann_id
            if ann['confidence'] >0.3 and ann['confidence'] <0.8: newann['confidence'] +=0.08
            self.annotations.append(newann)
            self.ann_id += 1

    def dump(self, out_file):
        with open(out_file, 'w') as f: json.dump({
            'images':self.images,
            "annotations":self.annotations,
            'categories':[
                {"supercategory": "none", "id": 1, "name": "Car"}, 
                {"supercategory": "none", "id": 2, "name": "Truck"}, 
                {"supercategory": "none", "id": 3, "name": "StopSign"}, 
                {"supercategory": "none", "id": 4, "name": "traffic_lights"}]
        }, f, indent=0)
if __name__ == '__main__':
    _converter = converter('p2_23.json')
    _converter.process()
    _converter.dump('p2_29.json')
    print(_converter.ann_id)
