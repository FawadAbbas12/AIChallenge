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
        # self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]
        self.data_dir = "datasets"
        self.train_ann = "train.json"
        self.val_ann = "val.json"

        self.num_classes = 4
        self.input_size = (1280, 1280)
        self.test_size  = (1280, 1280)
        self.multiscale_range = 0
        self.max_epoch = 300
        self.data_num_workers = 1
        self.eval_interval = 1
        self.warmup_epochs = 1
        self.warmup_lr = 0
        self.basic_lr_per_img = 0.01 
        # self.scheduler = "yoloxwarmcos"
        self.no_aug_epochs = 0
        self.min_lr_ratio = 0.05
        self.ema = True

        self.weight_decay = 5e-4
        self.momentum = 0.9

        self.degrees = 10.0
        self.translate = 0.5
        self.scale = (0.1, 0.2)
        self.mosaic_scale = (0.8, 1.9)
        self.shear = 0.0
        self.perspective = 0.0
        self.enable_mixup = True
        self.output_dir = 'ph2/val'
        self.test_conf = 0.001
        # nms threshold
        self.nmsthre = 0.60