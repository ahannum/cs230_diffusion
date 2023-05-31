import torch.utils.data
from data.base_data_loader import BaseDataLoader
import numpy as np, h5py
import random
def CreateDataLoader(opt):
    data_loader = CustomDatasetDataLoader()
    print(data_loader.name())
    data_loader.initialize(opt)
    return data_loader


def CreateDataset(opt):
    
    
    #Make sure that data_in_file and data_out_file correspond to the correct folders given that you provide dataroot and phase as correct arguments
    data_in_file = opt.dataroot + opt.phase + '/data_in.npy'
    data_out_file = opt.dataroot + opt.phase + '/data_out.npy'
         
    data_in = np.load(data_in_file)
    data_out = np.load(data_out_file)  
  
    data_in[0,:,:,:] = data_in[0,:,:,:]/np.max(data_in[0,:,:,:])
    data_in[1,:,:,:] = data_in[1,:,:,:]/np.max(data_in[1,:,:,:])
    data_in[2,:,:,:] = data_in[2,:,:,:]/np.max(data_in[2,:,:,:])
    data_in[3,:,:,:] = data_in[3,:,:,:]/np.max(data_in[3,:,:,:])
    data_in[4,:,:,:] = data_in[4,:,:,:]/np.max(data_in[4,:,:,:])
    data_in[5,:,:,:] = data_in[5,:,:,:]/np.max(data_in[5,:,:,:])
    data_in[6,:,:,:] = data_in[6,:,:,:]/np.max(data_in[6,:,:,:])

    #Make your processing of data_in and data_out here
    dataset=[]
    #Make sure that data_in and data_out are of shapes [6,(train_slices*combinations),128,128] and [1,(train_slices*combinations),128,128] 
    for sample_ind in range(data_in.shape[1]):
        dataset.append({'A': torch.from_numpy(data_in[:,sample_ind,:,:]),'B': torch.from_numpy(data_out[:,sample_ind,:,:])})
    return dataset 



class CustomDatasetDataLoader(BaseDataLoader):
    def name(self):
        return 'CustomDatasetDataLoader'

    def initialize(self, opt):
        BaseDataLoader.initialize(self, opt)
        self.dataset = CreateDataset(opt)
        self.dataloader = torch.utils.data.DataLoader(
            self.dataset,
            batch_size=opt.batchSize,
            shuffle=not opt.serial_batches,
            num_workers=int(opt.nThreads))

    def load_data(self):
        return self


    def __len__(self):
        return min(len(self.dataset), self.opt.max_dataset_size)

    def __iter__(self):
        for i, data in enumerate(self.dataloader):
            if i >= self.opt.max_dataset_size:
                break
            yield data
