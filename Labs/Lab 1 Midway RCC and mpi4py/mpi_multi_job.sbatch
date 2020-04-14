#!/bin/bash

#SBATCH --job-name=mpi_multi_job
#SBATCH --ntasks=11
#SBATCH --partition=broadwl
#SBATCH --constraint=fdr

# Load the default mpi4py/Anaconda module.
module load mpi4py/3.0.1a0_py3

# Run the python program with mpirun, using & to run jobs at the same time
mpirun -n 1 python ./mpi_rand_walk.py > ./mpi_nprocs1.out &
mpirun -n 10 python ./mpi_rand_walk.py > ./mpi_nprocs10.out &

# Wait until all simultaneous mpiruns are done
wait
