import os

import grpc
from langchain.agents import Tool, tool
from cloud.blintora.apis.code2cloud.kubernetes.rediskubernetes.v1 import query_pb2_grpc
from cloud.blintora.apis.code2cloud.kubernetes.rediskubernetes.v1 import io_pb2
from google.protobuf.text_format import MessageToString

@tool
def get_redis_kubernetes_client(redis_id: str):
    """Use this tool to get the redis kubernetes details from planton cloud. Input should be redis kubernetes id"""

    credentials = grpc.ssl_channel_credentials()

    channel = grpc.secure_channel('msk8s-planton-cloud-app-prod-code2cloud-main.planton.live:443', credentials)
    stub = query_pb2_grpc.RedisKubernetesQueryControllerStub(channel)

    token = os.getenv("PLANTON_CLOUD_AUTH_TOKEN")

    # Create a valid request message.
    request = io_pb2.RedisKubernetesId(value=redis_id)
    metadata = [('authorization', 'Bearer ' + token)]

    try:
        # Make the call to the server
        response = stub.get(request, metadata=metadata)

        # Convert the protobuf response to a string
        response_str = MessageToString(response)
        print("Response result:")
        print(response_str)

        # Return the string representation of the response
        return response_str

    except grpc.RpcError as e:
        print(f"gRPC error: {e.code()} - {e.details()}")
        raise
