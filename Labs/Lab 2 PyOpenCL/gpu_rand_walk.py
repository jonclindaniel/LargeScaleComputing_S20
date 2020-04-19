import numpy as np
import pyopencl as cl
import pyopencl.array as cl_array
import pyopencl.clrandom as clrand
import pyopencl.tools as cltools
from pyopencl.scan import GenericScanKernel
import matplotlib.pyplot as plt
import time

def sim_rand_walks(n_runs):
    # Set up context and command queue
    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx)

    # mem_pool = cltools.MemoryPool(cltools.ImmediateAllocator(queue))

    t0 = time.time()

    # Generate an array of Normal Random Numbers on GPU of length n_sims*n_steps
    n_steps = 100
    rand_gen = clrand.PhiloxGenerator(ctx)
    ran = rand_gen.normal(queue, (n_runs*n_steps), np.float32, mu=0, sigma=1)

    # Establish boundaries for each simulated walk (i.e. start and end)
    # Necessary so that we perform scan only within rand walks and not between
    seg_boundaries = [1] + [0]*(n_steps-1)
    seg_boundaries = np.array(seg_boundaries, dtype=np.uint8)
    seg_boundary_flags = np.tile(seg_boundaries, int(n_runs))
    seg_boundary_flags = cl_array.to_device(queue, seg_boundary_flags)

    # GPU: Define Segmented Scan Kernel, scanning simulations: f(n-1) + f(n)
    prefix_sum = GenericScanKernel(ctx, np.float32,
                arguments="__global float *ary, __global char *segflags, "
                    "__global float *out",
                input_expr="ary[i]",
                scan_expr="across_seg_boundary ? b : (a+b)", neutral="0",
                is_segment_start_expr="segflags[i]",
                output_statement="out[i] = item + 100",
                options=[])

    # Allocate space for result of kernel on device
    '''
    Note: use a Memory Pool (commented out above and below) if you're invoking
    multiple times to avoid wasting time creating brand new memory areas each
    time you invoke the kernel: https://documen.tician.de/pyopencl/tools.html
    '''
    # dev_result = cl_array.arange(queue, len(ran), dtype=np.float32,
    #                                allocator=mem_pool)
    dev_result = cl_array.empty_like(ran)

    # Enqueue and Run Scan Kernel
    prefix_sum(ran, seg_boundary_flags, dev_result)

    # Get results back on CPU to plot and do final calcs, just as in Lab 1
    r_walks_all = (dev_result.get()
                         .reshape(n_runs, n_steps)
                         .transpose()
                         )

    average_finish = np.mean(r_walks_all[-1])
    std_finish = np.std(r_walks_all[-1])
    final_time = time.time()
    time_elapsed = final_time - t0

    print("Simulated %d Random Walks in: %f seconds"
                % (n_runs, time_elapsed))
    print("Average final position: %f, Standard Deviation: %f"
                % (average_finish, std_finish))

    # Plot Random Walk Paths
    '''
    Note: Scan already only starts scanning at the second entry, but for the
    sake of the plot, let's set all of our random walk starting positions to 100
    and then plot the random walk paths.
    '''
    r_walks_all[0] = [100]*n_runs
    plt.plot(r_walks_all)
    plt.savefig("r_walk_nruns%d_gpu.png" % n_runs)

    return

def main():
    sim_rand_walks(n_runs = 10000)

if __name__ == '__main__':
    main()
