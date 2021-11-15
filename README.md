### amd_gpu_roofline

#### Roofline model for AMD MI100 GPUs

A roofline analysis enables a quantification of performance which is an agnostic and an abstraction over specific benchmarks, architecture, ISA, numerical algorithm, problem size etc. 

Good GPU performance is when

-- GPU operates in the throughput-limited regime

-- We attain a high usage of the GPU capabilities: maximal bandwidth, maximal throughput

#### Methodology

We use ROCm rocprof profiler

(1) Write an input file for rocprof


