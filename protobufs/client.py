import grpc

import songs_pb2_grpc, songs_pb2
from songs_pb2 import SongCategory


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = songs_pb2_grpc.RecommendationsStub(channel)
        try:
            rpc_call_type = input(
                "Какой жанр музыки вас интересует?\n 1. ПОП\n 2. РОК\n 3. ХИП-ХОП\n 4. ЭЛЕКТРОНИКА\n 5. ФОЛК\n")
            rpc_call_results = input("Сколько песен вам нужно?(максимум 5)\n")
            rpc_call_type = int(rpc_call_type)
            rpc_call_results = int(rpc_call_results)
            if rpc_call_type not in [1, 2, 3, 4, 5]:
                raise ValueError("Неправильный жанр")
            if rpc_call_results < 1 or rpc_call_results > 5:
                raise ValueError("Неправильное количество песен")

            if rpc_call_type == 1:
                request = songs_pb2.RecommendationRequest(category=SongCategory.POP, max_results=rpc_call_results)
                response = stub.Recommend(request)
                print(response)
            elif rpc_call_type == 2:
                request = songs_pb2.RecommendationRequest(category=SongCategory.ROCK, max_results=rpc_call_results)
                response = stub.Recommend(request)
                print(response)
            elif rpc_call_type == 3:
                request = songs_pb2.RecommendationRequest(category=SongCategory.HIP_HOP, max_results=rpc_call_results)
                response = stub.Recommend(request)
                print(response)
            elif rpc_call_type == 4:
                request = songs_pb2.RecommendationRequest(category=SongCategory.ELECTRONIC,
                                                          max_results=rpc_call_results)
                response = stub.Recommend(request)
                print(response)
            elif rpc_call_type == 5:
                request = songs_pb2.RecommendationRequest(category=SongCategory.FOLK, max_results=rpc_call_results)
                response = stub.Recommend(request)
                print(response)

        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except grpc.RpcError as e:
            print(f"RPC ошибка: {e}")


if __name__ == "__main__":
    run()
