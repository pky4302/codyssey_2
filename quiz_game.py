import json
from pathlib import Path
from quiz import Quiz, quiz_list

class QuizGame:

    def __init__(self):
        self.score = None
        self.best_score = 0
        self.current_question = 0

        self.load_state()

    #목록
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


    #목록에서 실행
    def start(self):
         try:
          
             while True:
                  self.show_menu()   

                  choice = self.get_menu_choice()

                  if choice == "1":
                       self.play_quiz()

                  elif choice == "2":
                       self.add_quiz()

                  elif choice == "3":
                       self.list_quizzes()

                  elif choice == "4":
                       self.show_score()

                  else:
                       print("게임을 종료합니다.")
                       break
                  
         except KeyboardInterrupt:
              print("\n사용자가 프로그램을 중단했습니다.")

              self.save_state()
              print("프로그램을 종료합니다.")

         except EOFError:
              print("\n입력이 종료되었습니다.")

              self.save_state()
              print("프로그램을 종료합니다.")

    
    #퀴즈풀기
    def play_quiz(self):
         if not quiz_list:
              print("등록된 퀴즈가 없습니다.")
              print("먼저 퀴즈를 추가해 주세요.")
              return
         
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

         if self.score > self.best_score:
              self.best_score = self.score
              self.save_state()
              print("최고 점수가 갱신되었습니다.") 

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

         choices = []

         for index in range(1,5):
              choice = input(f"{index}번 선택지를 입력하세요: ").strip()

              while not choice:
                   print("선택지는 비워둘 수 없습니다.")
                   choice = input(f"{index}번 선택지를 입력하세요: ").strip()

              choices.append(choice)

         answer = self.get_answer() #추가하더라도 검사

         new_quiz = Quiz(question, choices, answer)

         quiz_list.append(new_quiz)

         self.save_state()

         print("새로운 퀴즈가 등록되었습니다!")


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

    #점수확인
    def show_score(self):
         print()
         print("========== 점수 확인 ==========")

         if self.score is None:
              print("아직 퀴즈를 풀지 않았습니다.")
         else:
              print(f"최근 점수: {self.score}")
         print(f"최고 점수: {self.best_score}점")
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


    #json파일생성저장
    def save_state(self):
         state = {
              "quizzes": [],
              "best_score": self.best_score
         }

         for quiz in quiz_list:
              quiz_data = {
                   "question": quiz.question,
                   "choices": quiz.choices,
                   "answer": quiz.answer
              }

              state["quizzes"].append(quiz_data)

         file_path = Path(__file__).parent / "state.json" #현재 파이썬 파일이 있는 폴더

         try:
              
             with file_path.open("w", encoding="utf-8") as file:
                  json.dump(state, file, ensure_ascii=False, indent=4)

             print("데이터가 저장되었습니다.")

         except OSError as e:
              print("파일 저장에 실패했습니다.")
              print("오류: ", e)


    #프로그램실행시 자동 읽어오기
    def load_state(self):
         file_path = Path(__file__).parent / "state.json"

         # 저장 파일이 없는 경우
         if not file_path.exists():
              print("저장된 데이터가 없습니다. 기본 퀴즈를 사용합니다.")
              return

         try:
              with file_path.open("r", encoding="utf-8") as file:
                   state = json.load(file)

              #전체 데이터 구조 검증
              if not isinstance(state, dict):
                   raise ValueError("잘못된 데이터 구조")

              if not isinstance(state.get("quizzes"), list):
                   raise ValueError("퀴즈 목록이 잘못되었습니다.")

              best_score = state.get("best_score")

              if type(best_score) is not int or best_score < 0:
                   raise ValueError("최고 점수가 잘못되었습니다.")

              loaded_quizzes = []

              for quiz_data in state["quizzes"]:
                   
                   if not isinstance(quiz_data, dict):
                        raise ValueError("퀴즈 데이터가 잘못되었습니다.")
                   
                   question = quiz_data["question"]
                   choices = quiz_data["choices"]
                   answer = quiz_data["answer"]

                   if not isinstance(question, str) or not question.strip():
                        raise ValueError("문제가 잘못되었습니다.")

                   if not isinstance(choices, list) or len(choices) != 4:
                        raise ValueError("선택지가 잘못되었습니다.")

                   if not all(isinstance(choice, str) and choice.strip() for choice in choices):
                        raise ValueError("선택지 내용이 잘못되었습니다.")

                   if type(answer) is not int or not 1 <= answer <= 4:
                        raise ValueError("정답 번호가 잘못되었습니다.")

                   quiz = Quiz(question, choices, answer)

                   loaded_quizzes.append(quiz)

              #기존 기본 퀴즈 목록을 불러온 목록으로 교체
              quiz_list.clear()
              quiz_list.extend(loaded_quizzes)

              self.best_score = state["best_score"]

              print("저장된 데이터를 불러왔습니다.")

         except (json.JSONDecodeError, KeyError, TypeError, ValueError, OSError) as e:
              print("저장 파일이 손상되었습니다. 기본 데이터를 사용합니다.")
              print("오류: ", e)
