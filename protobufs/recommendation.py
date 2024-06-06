from concurrent import futures
import random
import grpc

from songs_pb2 import SongCategory, SongRecommendation, RecommendationResponse
import songs_pb2_grpc

songs_categories = {
    SongCategory.POP: [
        SongRecommendation(id=1, name="Starboy - The Weeknd, Daft Punk"),
        SongRecommendation(id=2, name="Talking to the Moon - Bruno Mars"),
        SongRecommendation(id=3, name="bad guy - Billie Eilish"),
        SongRecommendation(id=4, name="Despacito - Luis Fonsi, Daddy Yankee"),
        SongRecommendation(id=5, name="Blinding Lights - The Weeknd")
    ],
    SongCategory.FOLK: [
        SongRecommendation(id=1, name="Не отвечай мне - Сироткин"),
        SongRecommendation(id=2, name="занавес - внимание брусника!"),
        SongRecommendation(id=3, name="505 - Artic Monkeys"),
        SongRecommendation(id=4, name="немерено - лампабикт, Элли на маковом поле"),
        SongRecommendation(id=5, name="Выше домов - Сироткин")
    ],
    SongCategory.ROCK: [
        SongRecommendation(id=1, name="Дом - ПИКЧИ!"),
        SongRecommendation(id=2, name="Романс - МОЛОДОСТЬ ВНУТРИ"),
        SongRecommendation(id=3, name="Полетаем - Дурной Вкус"),
        SongRecommendation(id=4, name="Вдыхай - Расстройство"),
        SongRecommendation(id=5, name="созависимость - aikko")
    ],
    SongCategory.HIP_HOP: [
        SongRecommendation(id=1, name="AMMO - FRIENDLY THUG 52 NGG"),
        SongRecommendation(id=2, name="Танцуйте - ATL"),
        SongRecommendation(id=3, name="Пацан - Ирина Кайратовна"),
        SongRecommendation(id=4, name="Разбуди меня - T-Fest"),
        SongRecommendation(id=5, name="Очи - Bakr")
    ],
    SongCategory.ELECTRONIC: [
        SongRecommendation(id=1, name="Воздух - КУОК"),
        SongRecommendation(id=2, name="Glue - Bicep"),
        SongRecommendation(id=3, name="Linked - Bonobo"),
        SongRecommendation(id=4, name="KINO - THE DAWLESS, KACCETA"),
        SongRecommendation(id=5, name="seven - skyfall beats")
    ]
}


class RecommendationsService(songs_pb2_grpc.RecommendationsServicer):
    def Recommend(self, request, context):
        if request.category not in songs_categories:
            context.abort(grpc.StatusCode.NOT_FOUND, "Нет такой категории")
        songs_in_category = songs_categories[request.category]
        count_of_results = min(max(request.max_results), len(songs_in_category))
        songs_to_recommend = random.sample(songs_in_category, count_of_results)
        return RecommendationResponse(recommendations=songs_to_recommend)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    songs_pb2_grpc.add_RecommendationsServicer_to_server(RecommendationsService(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
