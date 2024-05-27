### Performance Analysis of Shortest Path First (SPF) Routing Using Floodlight and RYU Controllers in Software Defined Network (SDN) Based Networks

#### Overview

This repository contains the SPF module and topologies used for the performance analysis of Shortest Path First (SPF) routing on SDN-based networks. The following files are included:
- `shortestpath.py`: SPF module for the RYU Controller.
- `topology-fl.py`: Topology configuration for the Floodlight Controller.
- `topology-ryu.py`: Topology configuration for the RYU Controller.

The study aims to compare the performance of two controllers, Floodlight and RYU, in implementing the SPF routing algorithm. The experiments were conducted using mesh topologies with different numbers of nodes, specifically 6 nodes and 10 nodes.

#### Conclusions

1. **SPF Module on RYU and Floodlight**:
   - The SPF module on RYU was successfully run, but it exhibited instability leading to packet loss, whereas Floodlight remained stable with no packet loss.

2. **Throughput and Packet Loss**:
   - Higher throughput values indicate better data quality and lower delays, which minimize packet loss.
   - RYU testing resulted in an average packet loss of 0.0088%, while Floodlight experienced no packet loss (0%).

3. **Delay Comparison**:
   - RYU testing with 6 nodes resulted in an average delay of 0.013 ms, and with 10 nodes, it was 0.0344 ms.
   - Floodlight testing with 6 nodes resulted in an average delay of 0.036 ms, and with 10 nodes, it remained stable at 0.036 ms.

#### Summary Table of Results

| No. of Nodes | Controller | Throughput (Mbps) | Packet Loss (%) | Delay (ms) | Jitter (ms) |
|--------------|------------|-------------------|------------------|------------|-------------|
| 6 Nodes      | Floodlight | 7.53 - 7.10       | 0                | 0.032 - 0.041 | 0.016 - 0.020 |
| 6 Nodes      | RYU        | 8.91 - 11.36      | 0.01 - 0.02      | 0.030 - 0.039 | 0.015 - 0.017 |
| 10 Nodes     | Floodlight | 7.29 - 9.14       | 0                | 0.031 - 0.042 | 0.016 - 0.018 |
| 10 Nodes     | RYU        | 8.83 - 12.00      | 0.01 - 0.02      | 0.031 - 0.037 | 0.012 - 0.016 |

#### Acknowledgements
Thanks to everyone who provided guidance and support during this study.

This study shows that Floodlight has better stability compared to RYU in terms of packet loss, but RYU provides higher throughput despite a slight instability in packet loss.

---

This document provides an overview of the performance analysis results of two SDN controllers using the SPF routing algorithm and offers conclusions that can serve as a reference for further development and implementation in SDN-based networks. The repository includes the SPF module and topologies for both Floodlight and RYU controllers.
