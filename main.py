import numpy as np
import dask.array as da
import argparse
import time


def process_data(use_dask=False):
    if use_dask:
        data = da.random.random((10000, 10000), chunks=(1000, 1000))
        result = da.dot(data, data).compute()
    else:
        data = np.random.rand(10000, 10000)
        result = np.dot(data, data)
    
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run data processing with or without Dask.")
    parser.add_argument('--dask', action='store_true', help="Use Dask for processing")
    args = parser.parse_args()

    start = time.time()
    process_data(use_dask=args.dask)
    end = time.time()
    print(f"Time taken: {end - start} seconds")
    
