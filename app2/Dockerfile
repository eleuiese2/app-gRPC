FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install grpcio grpcio-tools

RUN python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/service.proto

CMD ["python", "server.py"]
