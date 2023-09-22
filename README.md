# ElasticFlow-artifact

We provide the artifact for the ASPLOS 2023 paper "ElasticFlow: An Elastic Serverless Training Platform for Distributed Deep Learning", including:

- The main implementation of ElasticFlow.
- Cluster simulation scripts (Sec 6.3 \& 6.4 \& 6.5), which get the main results of the paper.
- Testbed experiment scripts (Sec 6.2 \& 6.6).
- Figure plotting scripts.

## Simulation Experiments

### General Simulation Experiments

Please see `ElasticFlow/README.md` for more details. 

### Pollux simulation

Please see `pollux/pollux_simulator/README.md` for more details. 

## Testbed Experiments
Note: Due to the execution scripts of testbed experiments are highly related to internal testbed platform, we only demonstrate the functionality and provide the reproduction steps on the hardware devices we use. Please adjust to your platform if you would like to execute the testbed experiment.

The testbed experiments require 16 nodes, each with 8 A100 GPUs, 96 CPU cores, 900 GB RAM, and eight NVIDIA Mellanox HDR InfiniBand HCAs. 
You may use the Azure Standard_ND96asr_A100 VMs for reproduction.

### General Testbed Experiments
Please see `ElasticFlow/README.md` for more details.

### Pollux Testbed Experiments
As the Pollux baseline is implemented on k8s, we do not interage Pollux in the ElasticFlow system for comparison. We use the open-sourced artifact from the [Pollux repo](https://github.com/petuum/adaptdl/tree/osdi21-artifact) for testbed experiments. 

Please see `pollux/pollux_testbed/README.md` for more details.

## Plotting Figures
Please refer to `<repo>/plot_figure/README.md`

## Citation
If you use this code or survey in your research, please cite this project.
```
@inproceedings{GuZZXHCYHJL23,
  author       = {Diandian Gu and
                  Yihao Zhao and
                  Yinmin Zhong and
                  Yifan Xiong and
                  Zhenhua Han and
                  Peng Cheng and
                  Fan Yang and
                  Gang Huang and
                  Xin Jin and
                  Xuanzhe Liu},
  title        = {ElasticFlow: An Elastic Serverless Training Platform for Distributed
                  Deep Learning},
  booktitle    = {Proceedings of the 28th {ACM} International Conference on Architectural
                  Support for Programming Languages and Operating Systems, Volume 2,
                  {ASPLOS} 2023},
  pages        = {266--280},
  year         = {2023},
  doi          = {10.1145/3575693.3575721}
}
```
