Slurm (formerly Simple Linux Utility for Resource Management) is an open-source job scheduler and workload manager used for Linux clusters and supercomputers.

10. What is RDMA?

Answer

Remote Direct Memory Access allows one server to access another server's memory directly without involving the CPU.

Benefits:

Lower latency
Higher performance
Less CPU utilization


GPFS (General Parallel File System), now rebranded by IBM as IBM Storage Scale (and formerly IBM Spectrum Scale), is a high-performance, distributed, and parallel cluster file system. It allows thousands of compute nodes to read and write to a single, unified data pool simultaneously


https://www.cyberciti.biz/faq/network-statistics-tools-rhel-centos-debian-linux/

"My experience is primarily from an infrastructure and operations perspective. I understand HPC cluster architecture consisting of login, controller, and compute nodes; Slurm scheduling and resource management; shared parallel storage such as Lustre or BeeGFS; and high-speed networking using InfiniBand. I'm comfortable troubleshooting job scheduling issues, node failures, storage bottlenecks, Linux performance problems, and automating cluster administration using Ansible and Terraform."


MPI most commonly refers to the Message Passing Interface, a standardized protocol for high-performance parallel computing. 
It allows multiple processors to communicate in distributed memory systems

Btrfs (often pronounced "butter FS" or "better FS") is a modern copy-on-write (CoW) file system for Linux. It is designed to replace older file systems like ext4 by implementing advanced storage features natively, including built-in volume management, rapid read-only snapshots, and data integrity verification

Copy-on-Write (CoW): Instead of overwriting data in place, Btrfs writes modifications to empty space and updates the metadata to point to the new location. This ensures data consistency and allows for instant backupsv

Hugepages is a memory management feature that allows an operating system to use larger memory blocks (typically 2MB or 1GB) instead of the standard 4KB page size. By reducing the number of memory chunks a system must track, it drastically improves performance for memory-intensive applications like databases and virtualization

============================================================
Core Framework Comparison
Understanding where each framework operates is critical for structuring a job script correctly:

Framework	Architecture Type		Memory	 Model						Typical Use Case

MPI (Message Passing Interface)	Multi-Node (Distributed)	Isolated per process	Inter-node communication across network

OpenMP (Open Multi-Processing)		Single Node (Multi-Core)Shared across threads		Intra-node loop parallelization on CPUs

CUDA (Compute Unified Device Architecture)	Hardware Accelerator (GPU)	Independent device memory	Massively parallel matrix/vector math]
| Component        | Purpose                                       |
| ---------------- | --------------------------------------------- |
| Login Node       | User access, code compilation, job submission |
| Compute Node     | Executes jobs                                 |
| Slurm Controller | Scheduler and resource manager                |
| Storage          | Shared data access                            |
| InfiniBand       | Low-latency communication                     |

