from typing import List

from Classes.Session import Session
from Interfase.Proxy.Answers import Answers
from Classes.RequestsAPI import RequestsAPI
from Classes.Models.Answer import AnswerPost, AnswerGet


class AnswersAPI(Answers):
    def __init__(self):
        self.__api: RequestsAPI = RequestsAPI(Session().token.access_token)

    def get_package(self, id_contest: int, answers: dict) -> List[dict]:
        return self.__api.get_toke(f"answers/package/{id_contest}/0", answers)

    def get_answers(self, id_contest: int, id_task: int) -> dict:
        return self.__api.get_toke(f"answers/{id_contest}/{id_task}/0", {})

    def get_report(self, id_answer: int) -> dict:
        return self.__api.get(f"answers/report/{id_answer}", {})

    def post_answers(self, answer: dict) -> dict:
        return self.__api.post_token("answers/", answer)
