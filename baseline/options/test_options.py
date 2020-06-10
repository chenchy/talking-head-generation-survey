# Copyright (c) 2019, NVIDIA Corporation. All rights reserved.
#
# This work is made available
# under the Nvidia Source Code License (1-way Commercial).
# To view a copy of this license, visit
# https://nvlabs.github.io/few-shot-vid2vid/License.txt
from .base_options import BaseOptions

class TestOptions(BaseOptions):
    def initialize(self, parser):
        BaseOptions.initialize(self, parser)        
        parser.add_argument('--results_dir', type=str, default='./results/', help='saves results here.')        
        parser.add_argument('--phase', type=str, default='test', help='train, val, test, etc')        
        parser.add_argument('--how_many', type=int, default=300, help='how many test images to run')
        parser.add_argument('--example', action='store_true', help='get one frame from each video')
        parser.add_argument('--evaluate', action='store_true', help='get one frame from each video')
        parser.add_argument('--finetune_shot', type=int, default=32, help='how many finetune image')
        parser.add_argument('--ref_dataroot', type=str, help='root path of reference dataset')
        parser.add_argument('--ref_dataset', type=str, help='name of dataset for reference')
        parser.set_defaults(batchSize=1)
        parser.set_defaults(nThreads=1)
        parser.set_defaults(no_flip=True)
        self.isTrain = False
        return parser
