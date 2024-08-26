import dask.array as da

def process_data_with_dask():
    # Simulate a large computation using Dask
    data = da.random.random((10000, 10000), chunks=(1000, 1000))
    result = da.dot(data, data).compute()
    return result

if __name__ == "__main__":
    process_data_with_dask()
