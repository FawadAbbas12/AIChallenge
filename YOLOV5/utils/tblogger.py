import torch
from torch.utils.tensorboard import SummaryWriter
# from minio import Minio
from threading import Thread
import time
class TBLogger:
    class Logger(Thread):
        def __init__(self, writer, data, step, isTest, keeplist):
            super().__init__()
            self.writer = writer
            self.data_list = data
            self.step = step
            self.isTest = isTest
            self.keeplist = keeplist

        def update(self):
            for data in self.data_list:
                self.write(data, self.step, self.isTest)

        def write(self, data, step, isTest):
            for key, val in data.items():
                if not key in self.keeplist: continue
                if isTest: key = f'test_{key}'
                self.writer.add_scalar(key, float(str(val).split(' ')[0]), step)

        def run(self):
            self.update()

    def __init__(self, outputPath:str, keepList:list = ['lr', 'class_error', 'loss', 'loss_bbox', 'loss_bbox_0', 'loss_bbox_1', 'loss_bbox_2', 'loss_bbox_3', 'loss_bbox_4', 'loss_ce', 'loss_ce_0', 'loss_ce_1', 'loss_ce_2', 'loss_ce_3', 'loss_ce_4', 'loss_giou', 'loss_giou_0', 'loss_giou_1', 'loss_giou_2', 'loss_giou_3', 'loss_giou_4', 'cardinality_error_unscaled', 'cardinality_error_0_unscaled', 'cardinality_error_1_unscaled', 'cardinality_error_2_unscaled', 'cardinality_error_3_unscaled', 'cardinality_error_4_unscaled', 'class_error_unscaled', 'loss_bbox_unscaled', 'loss_bbox_0_unscaled', 'loss_bbox_1_unscaled', 'loss_bbox_2_unscaled', 'loss_bbox_3_unscaled', 'loss_bbox_4_unscaled', 'loss_ce_unscaled', 'loss_ce_0_unscaled', 'loss_ce_1_unscaled', 'loss_ce_2_unscaled', 'loss_ce_3_unscaled', 'loss_ce_4_unscaled', 'loss_giou_unscaled', 'loss_giou_0_unscaled', 'loss_giou_1_unscaled', 'loss_giou_2_unscaled', 'loss_giou_3_unscaled', 'loss_giou_4_unscaled', 'loss_hw_unscaled', 'loss_hw_0_unscaled', 'loss_hw_1_unscaled', 'loss_hw_2_unscaled', 'loss_hw_3_unscaled', 'loss_hw_4_unscaled', 'loss_xy_unscaled', 'loss_xy_0_unscaled', 'loss_xy_1_unscaled', 'loss_xy_2_unscaled', 'loss_xy_3_unscaled', 'loss_xy_4_unscaled', 'time', 'data']):
        self.writer = SummaryWriter(outputPath)
        self.keeplist = keepList

    def update(self, data_list, step, isTest=False):
        logger = self.Logger(self.writer, data_list, step, isTest, self.keeplist)
        logger.start()
        logger.join()
    
    def addImage(self, images, ann):
        pass

# class ModelRegistery:
#     class Uploader(Thread):
#         def __init__(self, minio_client:Minio, bucket_name:str, object_name:str, file_path:str, metadata:dict={}):
#             super().__init__()
#             self.minio_client = minio_client
#             self.bucket_name = bucket_name
#             self.object_name = object_name
#             self.file_path = file_path
#             self.metadata =metadata
#             self.metadata['upload_time'] = time.time()
#         def run(self):
#             self.minio_client.fput_object(
#                 self.bucket_name,
#                 self.object_name,
#                 self.file_path,
#                 metadata=self.metadata
#             )
#     def __init__(self,host, secret_access, secret_key, secure, bucket_name) -> None:
#         self.minio_client = Minio(
#             host, 
#             access_key= secret_access,
#             secret_key= secret_key,
#             secure=secure
#         )
#         self.bucket_name = bucket_name
#         if not self.bucket_name in self.minio_client.list_buckets():
#             self.minio_client.make_bucket(self.bucket_name)
#     def upload(self, checkpoint_path:str, metadata:dict={}):
#         uploader = self.Uploader(self.minio_client, self.bucket_name, checkpoint_path.split('/')[-1], checkpoint_path, metadata)
#         uploader.daemon = True
#         uploader.start()