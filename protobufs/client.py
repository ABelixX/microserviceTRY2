import grpc
from songs_pb2 import SongCategory, SongRecommendation, RecommendationResponse
import songs_pb2_grpc
import songs_pb2


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = songs_pb2_grpc.RecommendationsStub(channel)
        rpc_call_type = input(
            "Какой жанр музыки вас интересует?\n 1. ПОП\n 2. РОК\n 3.ХИП-ХОП\n 4. ЭЛЕКТРОНИКА\n 5. ФОЛК\n")
        rpc_call_results = input("Сколько песен вам нужно?(максимум 5)\n")
        if rpc_call_type == "1":
            request = songs_pb2.RecommendationRequest(category=SongCategory.POP, max_results=int(rpc_call_results))
        elif rpc_call_type == "2":
            request = songs_pb2.RecommendationRequest(category=SongCategory.ROCK, max_results=int(rpc_call_results))
        elif rpc_call_type == "3":
            request = songs_pb2.RecommendationRequest(category=SongCategory.HIP_HOP, max_results=int(rpc_call_results))
        elif rpc_call_type == "4":
            request = songs_pb2.RecommendationRequest(category=SongCategory.ELECTRONIC,
                                                      max_results=int(rpc_call_results))
        elif rpc_call_type == "5":
            request = songs_pb2.RecommendationRequest(category=SongCategory.FOLK, max_results=int(rpc_call_results))
        response = stub.Recommend(request)
        print(response)


if __name__ == "__main__":
    run()
