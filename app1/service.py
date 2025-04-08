import grpc
from concurrent import futures
import time
import service_pb2
import service_pb2_grpc

class Greeter(service_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return service_pb2.HelloReply(message=f"Hello, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    service_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
