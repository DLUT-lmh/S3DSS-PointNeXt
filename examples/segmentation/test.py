import torch
import sys
import os

print("Python version is {}".format(sys.version))
print("\nHello World, Hello PyTorch {}".format(torch.__version__))
print("\nCUDA is available:{}, version is {}".format(torch.cuda.is_available(), torch.version.cuda))
print("\ncudnn version is {}".format(torch.backends.cudnn.version()))
print("\ndevice_name: {}".format(torch.cuda.get_device_name(0)))
print("\nCHECK INSTALLATION: {}".format(os.environ.get('CUDA_PATH')))