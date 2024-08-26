# Dockerfile
FROM daskdev/dask:latest

WORKDIR /app
COPY . /app

# Install any additional dependencies
RUN pip install -r requirements.txt

CMD ["dask-scheduler"]
