from quiz import quiz_list

class QuizGame:

    def __init__(self):
        self.score = 0
        self.current_question = 0

    def show_menu(self):
           print()
           print("========================================")
           print("          나만의 퀴즈 게임")
           print("========================================")
           print("1. 퀴즈 풀기")
           print("2. 퀴즈 추가")
           print("3. 퀴즈 목록")
           print("4. 점수 확인")
           print("5. 종료")
           print("========================================")

    def start(self):
         while True:
              self.show_menu()

              choice = self.get_menu_choice()

              if choice == "1":
                   self.play_quiz()

              elif choice == "2":
                   print("퀴즈 추가를 선택했습니다.")

              elif choice == "3":
                   self.list_quizzes()

              elif choice == "4":
                   print("퀴즈 확인을 선택했습니다.")

              else:
                   print("게임을 종료합니다.")
                   break

    #퀴즈풀기
    def play_quiz(self):
         self.score = 0
         total = len(quiz_list)

         for index, quiz in enumerate(quiz_list, start=1):
              print()
              print(f"{index}번 문제]")
              quiz.show_question() #Quiz 클래스의 인스턴스 메소드

              user_answer = self.get_answer() #정답입력 검사 메소드 호출

              if quiz.check_answer(user_answer): #Quiz 클래스의 인스턴스 메소드
                   print("정답입니다!")
                   self.score += 1
              else:
                   print("틀렸습니다!")

         wrong_count = total - self.score
         accuracy = self.score / total * 100

         print()
         print("========================")
         print("         게임 결과")
         print("========================")
         print(f"전체 문제: {total}개")
         print(f"정답: {self.score}개")
         print(f"오답: {wrong_count}개")
         print(f"정답률: {accuracy:.1f}%")
         print("========================")


    #퀴즈추가
    def add_quiz(self):
         print()
         print("========== 퀴즈 추가 ==========")

         question = input("문제를 입력하세요: ").strip()

         while not question:
              print("문제는 비워둘 수 없습니다.")
              question = input("문제를 입력하세요: ").strip()
         
             


         
         

    #퀴즈목록조회
    def list_quizzes(self):
         print()
         print("========== 퀴즈 목록 ==========")

         if not quiz_list:
              print("등록된 퀴즈가 없습니다.")
              return

         for index, quiz in enumerate(quiz_list, start=1):
              print()
              print(f"{index}번 문제]")
              print(quiz.question)

              for choice_index, choice in enumerate(quiz.choices, start=1):
                   print(f"{choice_index}. {choice}")

         print()
         print(f"총 {len(quiz_list)}개의 퀴즈가 등록되어 있습니다.")
         print("==============================")
         

    #메뉴 입력값 검사
    def get_menu_choice(self):
         while True:
              choice = input("메뉴 선택: ").strip() #공백제거

              if not choice:
                   print("메뉴를 입력해 주세요.")
                   continue

              if choice not in ["1", "2", "3", "4", "5"]:
                   print("1부터 5까지의 메뉴를 선택해 주세요.")
                   continue

              return choice


    #play_quiz에서 정답 입력 1 ~ 4 까지 받기와 타입 검사
    def get_answer(self):
         while True:
              user_input = input("정답 입력: ").strip() #공백제거

              if not user_input:
                   print("아무것도 입력하지 않았습니다.")
                   continue

              try:
                   user_answer = int(user_input)
              except ValueError:
                   print("숫자만 입력해 주세요.")
                   continue

              if user_answer < 1 or user_answer > 4:
                   print("1부터 4까지의 숫자를 입력해 주세요.")
                   continue

              return user_answer
         