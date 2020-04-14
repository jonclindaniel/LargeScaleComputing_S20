# Logging in and Copying Files to Midway
See [RCC user guide](https://rcc.uchicago.edu/docs/) for login details specific to your system and additional options. The instructions for copying files via `scp` and logging in via `ssh` below assume a Unix-style command line interface.

### SSH into Cluster with cNetID and Password
```
ssh your_cnet_id@midway2.rcc.uchicago.edu
```
Note that you'll now be able to move around your home directory using standard unix commands (`cd`, `pwd`, `ls`, etc.). If you are on a Windows machine, I (Jon) recommend enabling [Windows Subsystem for Linux and installing Ubuntu 18.04](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to complete all of these tasks. This is what I do and I find this makes my life a lot easier than having to mentally transition between DOS and Unix commands (or needing to use an additional third-party tool).

### SCP files to/from local directory
If you need to transfer files to and from Midway's storage, I find it easiest to just copy files via the `scp` command. Here, I copy a local file `local_file` in my current directory to my home directory on Midway. Then, I copy a file `remote_file` from my Midway home directory back to my current directory on my local machine. If you prefer not to use this command line approach, there are tutorials in the Midway documentation with [alternative approaches](https://rcc.uchicago.edu/docs/data-transfer/index.html).

```
scp local_file your_cnet_id@midway2.rcc.uchicago.edu:
```
```
scp your_cnet_id@midway2.rcc.uchicago.edu:remote_file .
```

To copy an entire directory, use the `-r` flag:
```
scp -r your_cnet_id@midway2.rcc.uchicago.edu:remote_directory .
```

### Clone GitHub Repository
Another good option is to clone a GitHub repository (for instance this public course repository) to your home directory on Midway and access files/code this way.

```
git clone https://github.com/jonclindaniel/LargeScaleComputing_S20.git
```

### Adjustments to text on the Command Line
If need to make any adjustments to text files before/after running them (or create new ones) on Midway, can do so on the command line with text editing tools such as nano, vim, etc.
```
nano mpi.sbatch
```

# Loading Modules and installing programs

### Load appropriate modules for MPI CPU* and OpenCL GPU dev
```
module load cuda
module load mpi4py/3.0.1a0_py3
```

### Install additional Python packages to local user directory from login node
To install packages that are not already included in a module (such as upgrading matplotlib, and installing PyOpenCL, which we will be using in this class), you can use `pip` to install these packages in your local user directory from the login node on Midway. Make sure you have loaded the cuda and mpi4py modules above before you try to run the below commands.

```
pip install -U --user matplotlib
pip install --user pyopencl
```

# Running jobs

Resource sharing and job scheduling is handled by Slurm software on the Midway RCC. You can see detailed information in the Midway documentation, but Slurm allows you to see which partitions are available at any given time via the `sinfo` command, submit batch jobs via the `sbatch` command (which will allow you to request specific node/interconnect resources for a period of time and run your code on those resources), and schedule interactive sessions via the `sinteractive` command. Listed below are some of the fundamental commands you will need to know how to perform for this class.

### Run Batch jobs with Slurm scripts
You will use Slurm scripts to request computational resources for a period of time and run your code. These scripts can be run with the `sbatch` commands, as demonstrated below. You can check out sample Slurm scripts in our GitHub course repository, for more detail on how these scripts are structured.

```
sbatch mpi.sbatch
sbatch gpu.sbatch
```

Note, if you wrote your sbatch file on a Windows machine, you might need to convert the text into a Unix format for it to run properly on the Midway RCC. To do so, you can install `dos2unix` on WSL via `apt-get install dos2unix` and then run the converter on your sbatch file.

```
dos2unix gpu.sbatch
```

You can monitor the progress of your job with (the sbatch command will print out your job ID):
```
squeue -j your_job_id
```

You can also cancel jobs with:
```
scancel your_job_id
```

### Check results of your batch job (assuming write to `.out` file)
In your Slurm script, you will specify a `.out` file, where the output of your program will be written. You can download the file to your local machine to look at the results (via `scp`), or you can check the results on the Midway command line with the standard Unix `cat` command.

```
cat gpu.out
```

### Run interactive jobs
You should not perform intensive computational tasks on the login nodes. Use the `sinteractive` command to set up an interactive session on other Midway nodes if you want to have an interactive command line experience (you can specify exactly which nodes you would like to access; see the documentation for syntax). Here we request 4 cores for 15 minutes. Additionally, you can use the interactive mode to run Jupyter notebooks, which you can view in your browser (see documentation for more details).

```
sinteractive --time=00:15:00 --ntasks=4
```

\* Note: this setup allows for use of mpi4py, PyOpenCL, as well as PySpark (which is included in the mpi4py module)
