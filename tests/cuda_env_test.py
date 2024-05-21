import torch
import os

# 检查CUDA工具包和驱动程序的安装
nvcc_version = torch.version.cuda
print("CUDA工具包版本:", nvcc_version)

# 检查GPU驱动程序的安装
cuda_version = torch.version.cuda.split(".")[0]
print("驱动程序版本:", cuda_version)

# 安装匹配版本的PyTorch
torch_version = torch.__version__.split("+")[0]
print("PyTorch版本:", torch_version)

# 确认CUDA环境变量的设置
cuda_home = os.environ.get("CUDA_PATH")
print("CUDA安装路径:", cuda_home)

# 检查PyTorch库的重新安装
available = torch.cuda.is_available()
print("result:", available)