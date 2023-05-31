
# This is the command you need to run your model. Please fill the ones that are written with [].

# Training commands
python3.8 [insert_code_address_here followed by pGAN.py] --dataroot [insert dataroot here that contains three subfolders named train test and val] --name [insert the name of the experiment here, you can select whatever you want] --dataset_mode aligned --norm batch  --output_nc [insert the number of output channels, I assume that it is 1] --input_nc [insert the number of input channels here, I assume that it is 6] --niter [number of epochs with constant learning rate, you can put 50] --niter_decay [number of epochs with decreasing learning rate, you can put 50] --save_epoch_freq 10 --lambda_A 100 --checkpoints_dir [insert a location where you want to save your network models and some training set images for controlling the progress of training] --training --gpu_ids 0

# Testing commands
python3.8 [insert_code_address_here followed by pGAN.py] --dataroot [insert dataroot here that contains three subfolders named train test and val] --name [insert the name of the experiment here, you can select whatever you want]  --which_direction AtoB --phase test --output_nc [insert the number of output channels, I assume that it is 1] --input_nc [insert the number of input channels here, I assume that it is 6] --how_many 5000 --norm batch --dataset_mode aligned --results_dir [insert a location where you want to save your results]  --checkpoints_dir [insert a location where you want to take your saved network moodels]

