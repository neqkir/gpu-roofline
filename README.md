### amd_gpu_roofline

#### Roofline model for AMD MI100 GPUs

A roofline analysis enables a quantification of performance which is an agnostic and an abstraction over specific benchmarks, architecture, ISA, numerical algorithm, problem size etc. 

Good GPU performance is when

-- GPU operates in the throughput-limited regime

-- We attain a high usage of the GPU capabilities: maximal bandwidth, maximal throughput

#### Methodology

We use ROCm rocprof profiler

**(1) Write an input file for rocprof** 

An example is given by rocprof-input-file.txt

Documentation for rocprof data collection https://github.com/ROCm-Developer-Tools/rocprofiler/blob/amd-master/doc/rocprof.md

**(2) Run application adding rocprof call**

`rocprof -i rocprof-input-file.txt --timestamp on python3 shakespeare-text-gen.py`

**(3) Compute relevant values**

Rearrange the rocprof .csv output file extracting the relevant values

Compute 

Memory size (KB) = FETCH_SIZE + WRITE_SIZE
Float Size = (SQ_INSTS_VALU + SQ_INSTS_SALU)* 64

FLOPs = Float size/executed time
FLOP/byte = Float size/(Memory size*1024)

**(4) Write a python script for building roofline model** inspired from `roofline.py`

