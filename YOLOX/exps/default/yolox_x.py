#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 1.33
        self.width = 1.25
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]
        self.data_dir = "datasets/coco"
        self.train_ann = "train.json"
        self.val_ann = "val.json"

        self.num_classes = 4

        self.max_epoch = 300
        self.data_num_workers = 20
        self.eval_interval = 1
