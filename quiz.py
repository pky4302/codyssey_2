class Quiz:
    #생성자로 값을 전달받기 위한 필요 과정
    def __init__(self, question,choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 문제와 선택지 출력
    def show_question(self):
        print(self.question)

        for index, choice in enumerate(self.choices, start=1): #start는 index 시작지점
            print(f"{index}. {choice}")

    # 사용자입력정답과 실제정답 비교 확인 (boolean)
    def check_answer(self, user_answer):
        return self.answer == user_answer # true/false



# 기본 퀴즈 데이터
quiz_list = [
    Quiz(
        "Python에서 화면에 문자를 출력하는 함수는?",
        ["input()", "print()", "len()", "type()"],
        2
    ),
    Quiz(
        "Python에서 리스트를 만드는 기호는?",
        ["()", "{}", "[]", "<>"],
        3
    ),
    Quiz(
        "Python에서 함수를 정의할 때 사용하는 키워드는?",
        ["function", "def", "class", "import"],
        2
    ),
    Quiz(
        "Python에서 참과 거짓을 나타내는 자료형은?",
        ["int", "str", "bool", "list"],
        3
    ),
    Quiz(
        "Python에서 반복문을 작성할 때 사용하는 키워드는?",
        ["if", "for", "return", "import"],
        2
    )
]