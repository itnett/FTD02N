python
   import grpc
   from my_grpc_module import MyServiceStub, RequestMessage

   with grpc.insecure_channel('localhost:50051') as channel:
       stub = MyServiceStub(channel)
       response = stub.MyFunction(RequestMessage(param="value"))
       print(response.result)