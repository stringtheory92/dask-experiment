# Dask Experiment Repository

Welcome to the Dask Experiment repository! This project aims to explore and demonstrate the benefits (and potential drawbacks) of using Dask for parallel computing in Python, particularly in the context of processing large datasets.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Experiment](#running-the-experiment)
  - [Switching Between Dask and Non-Dask Execution](#switching-between-dask-and-non-dask-execution)
- [Performance Observations](#performance-observations)
- [Optimization and Future Work](#optimization-and-future-work)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains a set of scripts and Docker configurations designed to test and compare the performance of computational tasks when executed using Dask versus standard Python execution. The primary objective is to measure the performance impact of using Dask for parallel processing, especially for tasks involving large datasets.

## Project Structure

````plaintext
dask-experiment/
│
├── Dockerfile                    # Docker configuration for running Dask containers
├── docker-compose.yml            # Docker Compose file for managing multiple Dask services
├── main.py                       # Main script for running the experiment
├── no_dask.py                    # Script demonstrating the task without Dask
├── with_dask.py                  # Script demonstrating the task with Dask
└── README.md                     # This README file

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Docker**: [Docker Installation Guide](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

### Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/dask-experiment.git
cd dask-experiment
```
## Usage

### Running the Experiment

The experiment can be run using Docker. Follow the steps below:

1. **Build and Start the Docker Containers**:

   ```bash
   docker-compose up --build```

This will start the Dask scheduler, worker, and client services.

2. **Access the Dask Client Container**:

   Once the containers are running, open a bash shell in the client container:

   ```bash
   docker exec -it dask-experiment-client-1 /bin/bash```


```
3. **Navigate to the Project Directory**:

   Inside the container, navigate to the `/app` directory:

   ```bash
   cd /app

```

4. **Run the Experiment**:

   You can run the main experiment script with or without Dask:

   - **With Dask**:

     ```bash
     python main.py --dask
     ```

   - **Without Dask**:

     ```bash
     python main.py
     ```

### Switching Between Dask and Non-Dask Execution

The `main.py` script includes a command-line argument `--dask` to switch between using Dask for parallel processing and running the task without Dask. This allows for easy comparison of performance between the two approaches.

## Performance Observations

Based on the initial experiments:

- **Without Dask**: The task completed in approximately 14 seconds.
- **With Dask**: The task completed in approximately 38 seconds, with a warning about chunk size adjustments.

**Key Insights**:
- The overhead introduced by Dask may not be beneficial for smaller tasks or simpler operations.
- Dask's true benefits are more likely to be realized with larger datasets or more complex workflows.

## Optimization and Future Work

Future improvements and potential areas for exploration include:

- **Chunk Size Optimization**: Experiment with different chunk sizes to improve Dask performance.
- **Task Granularity**: Evaluate how breaking down tasks into smaller units affects performance.
- **Resource Allocation**: Fine-tune CPU and memory limits for containers to better manage resources.
- **Profiling**: Use Dask's built-in profiling tools to gain insights into task execution and identify bottlenecks.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request. Please ensure your changes are well-documented and tested.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

````
