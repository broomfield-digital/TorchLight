import torch
print('version:', torch.__version__)
print('have CUDA:', torch.cuda.is_available())
print('have  MPS:', torch.backends.mps.is_available())
