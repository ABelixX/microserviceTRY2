
from concurrent import futures
import random
import grpc
import time

import songs_pb2_grpc
import songs_pb2
from songs_pb2 import SongCategory, SongRecommendation, RecommendationResponse

songs_categories = {
    SongCategory.POP: [
        SongRecommendation(id=21, name="Starboy - The Weeknd, Daft Punk"),
        SongRecommendation(id=22, name="Talking to the Moon - Bruno Mars"),
        SongRecommendation(id=23, name="bad guy - Billie Eilish"),
        SongRecommendation(id=24, name="Despacito - Luis Fonsi, Daddy Yankee"),
        SongRecommendation(id=25, name="Blinding Lights - The Weeknd")
    ],
    SongCategory.FOLK: [
        SongRecommendation(id=1, name="Не отвечай мне - Сироткин"),
        SongRecommendation(id=2, name="занавес - внимание брусника!"),
        SongRecommendation(id=3, name="505 - Artic Monkeys"),
        SongRecommendation(id=4, name="немерено - лампабикт, Элли на маковом поле"),
        SongRecommendation(id=5, name="Выше домов - Сироткин")
    ],
    SongCategory.ROCK: [
        SongRecommendation(id=6, name="Дом - ПИКЧИ!"),
        SongRecommendation(id=7, name="Романс - МОЛОДОСТЬ ВНУТРИ"),
        SongRecommendation(id=8, name="Полетаем - Дурной Вкус"),
        SongRecommendation(id=9, name="Вдыхай - Расстройство"),
        SongRecommendation(id=10, name="созависимость - aikko")
    ],
    SongCategory.HIP_HOP: [
        SongRecommendation(id=11, name="AMMO - FRIENDLY THUG 52 NGG"),
        SongRecommendation(id=12, name="Танцуйте - ATL"),
        SongRecommendation(id=13, name="Пацан - Ирина Кайратовна"),
        SongRecommendation(id=14, name="Разбуди меня - T-Fest"),
        SongRecommendation(id=15, name="Очи - Bakr")
    ],
    SongCategory.ELECTRONIC: [
        SongRecommendation(id=16, name="Воздух - КУОК"),
        SongRecommendation(id=17, name="Glue - Bicep"),
        SongRecommendation(id=18, name="Linked - Bonobo"),
        SongRecommendation(id=19, name="KINO - THE DAWLESS, KACCETA"),
        SongRecommendation(id=20, name="seven - skyfall beats")
    ]
}


class RecommendationsService(songs_pb2_grpc.RecommendationsServicer):
    def Recommend(self, request, context):

        if request.category not in songs_categories:
            context.abort(grpc.StatusCode.NOT_FOUND, "Нет такой категории")
        songs_in_category = songs_categories[request.category]
        count_of_results = min(request.max_results, len(songs_in_category))
        songs_to_recommend = random.sample(songs_in_category, count_of_results)
        return RecommendationResponse(recommendations=songs_to_recommend)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    songs_pb2_grpc.add_RecommendationsServicer_to_server(RecommendationsService(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()
    print("Server started on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
