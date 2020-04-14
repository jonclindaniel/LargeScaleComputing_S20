#!/bin/bash

#SBATCH --job-name=mpi
#SBATCH --output=mpi.out
#SBATCH --ntasks=4
#SBATCH --partition=broadwl
#SBATCH --constraint=fdr

# Load the default mpi4py/Anaconda module.
module load mpi4py/3.0.1a0_py3

# Run the python program with mpirun. The -n flag is not required;
# mpirun will automatically figure out the best configuration from the
# Slurm environment variables.
mpirun python ./mpi_rand_walk.py
