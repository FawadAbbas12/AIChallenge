import os
from yolox.exp import Exp as MyExp
class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 1.0
        self.width = 1.0
        # self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]
        # Define yourself dataset path
        self.data_dir = "datasets/coco"
        self.train_ann = "train.json"
        self.val_ann = "val.json"
        self.input_size = (1280, 1280)  # (h,w)
        #self.random_size = (23, 46)
        self.test_size = (1280, 1280)
        # self.random_size = (34, 46)
        self.num_classes = 4
        self.max_epoch = 100
        self.data_num_workers = 1
        self.eval_interval = 1
        # self.warmup_epochs = 1
        self.warmup_lr = 0
        self.basic_lr_per_img = 0.01
        #elf.scheduler = "yoloxwarmcos"
        # self.no_aug_epochs = 15
        self.min_lr_ratio = 0.05
        self.ema = True
        self.output_dir = 'model_zoo/schal/'
        self.weight_decay = 5e-4
        self.momentum = 0.9
        self.degrees = 10.0
        self.translate = 0.1
        self.scale = (0.5, 1.5)
        self.mosaic_scale = (0.8, 1.6)
        self.shear = 0.6
        self.perspective = 0.0
        self.enable_mixup = True