from mpi4py import MPI
import matplotlib.pyplot as plt
import numpy as np
import time

def sim_rand_walks_parallel(n_runs):
    # Get rank of process and overall size of communicator:
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Start time:
    t0 = time.time()

    # Evenly distribute number of simulation runs across processes
    N = int(n_runs/size)

    # Simulate N random walks and specify as a NumPy Array
    r_walks = []
    for i in range(N):
        steps = np.random.normal(loc=0, scale=1, size=100)
        steps[0] = 0
        r_walks.append(100 + np.cumsum(steps))
    r_walks_array = np.array(r_walks)

    # Gather all simulation arrays to buffer of expected size/dtype on rank 0
    r_walks_all = None
    if rank == 0:
        r_walks_all = np.empty([N*size, 100], dtype='float')
    comm.Gather(sendbuf = r_walks_array, recvbuf = r_walks_all, root=0)

    # Print/plot simulation results on rank 0
    if rank == 0:
        # Calculate time elapsed after computing mean and std
        average_finish = np.mean(r_walks_all[:,-1])
        std_finish = np.std(r_walks_all[:,-1])
        time_elapsed = time.time() - t0

        # Print time elapsed + simulation results
        print("Simulated %d Random Walks in: %f seconds on %d MPI processes"
                % (n_runs, time_elapsed, size))
        print("Average final position: %f, Standard Deviation: %f"
                % (average_finish, std_finish))

        # Plot Simulations and save to file
        plt.plot(r_walks_all.transpose())
        plt.savefig("r_walk_nprocs%d_nruns%d.png" % (size, n_runs))

    return

def main():
    sim_rand_walks_parallel(n_runs = 10000)

if __name__ == '__main__':
    main()
