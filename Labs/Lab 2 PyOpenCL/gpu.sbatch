#!/bin/bash
#SBATCH --job-name=gpu   # job name
#SBATCH --output=gpu.out # output log file
#SBATCH --error=gpu.err  # error file
#SBATCH --time=00:05:00  # 5 minutes of wall time
#SBATCH --nodes=1        # 1 GPU node
#SBATCH --partition=gpu2 # GPU2 partition
#SBATCH --ntasks=1       # 1 CPU core to drive GPU
#SBATCH --gres=gpu:1     # Request 1 GPU

module load cuda
module load mpi4py/3.0.1a0_py3

python ./print_gpu_info.py
# python ./gpu_rand_walk.py
