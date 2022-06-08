import requests
import random


def random_question():
    question_id = random.randint(1, 15)
    url = 'https://opentdb.com/api.php?amount=10&category=11&difficulty=medium&type=multiple{}'.format(question_id)
    res = requests.get(url)
    question = res.json()

    return {
        'question': question["question"],
    }

random_question()