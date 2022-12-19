from Interfase.Proxy.Answers import Answers
from Classes.ProxyController.AnswersAPI import AnswersAPI
from Classes.Models.Answer import AnswerGet, AnswerPost
from functools import partial


class AnswersProxy(Answers):
    def __init__(self):
        self.__api: AnswersAPI = AnswersAPI()
        self.operations = []

    def get_package(self, id_contest: int, answers: dict):
        func = partial(self.__api.get_package, id_contest, answers)
        self.operations.append(func)
        return func()

    def get_answers(self, id_contest: int, id_task: int):
        func = partial(self.__api.get_answers, id_contest, id_task)
        self.operations.append(func)
        return func()

    def get_report(self, id_answer: int):
        func = partial(self.__api.get_report, id_answer)
        self.operations.append(func)
        return func()

    def post_answers(self, answer: dict):
        func = partial(self.__api.post_answers, answer)
        self.operations.append(func)
        return func()


