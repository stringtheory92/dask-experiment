import numpy as np

def process_data():
    # Simulate a large computation
    data = np.random.rand(10000, 10000)
    result = np.dot(data, data)
    return result

if __name__ == "__main__":
    process_data()
