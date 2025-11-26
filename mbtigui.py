import tkinter as tk
from tkinter import messagebox

class MBTiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("개발자 성향 테스트 (MBTI)")
        self.root.geometry("500x400")
        
        # 질문 DB (실제로는 더 많아야 정확함)
        self.questions = [
            {"q": "개발 공부를 할 때 나는?", "opt": [("스터디 그룹에서 같이한다 (E)", "E"), ("혼자 조용히 파고든다 (I)", "I")]},
            {"q": "코딩할 때 더 중요한 것은?", "opt": [("지금 당장 돌아가는 기능 구현 (S)", "S"), ("미래를 고려한 우아한 구조 (N)", "N")]},
            {"q": "동료의 코드를 리뷰할 때?", "opt": [("팩트 위주로 효율성을 지적한다 (T)", "T"), ("상처받지 않게 돌려서 말한다 (F)", "F")]},
            {"q": "마감일이 다가올 때?", "opt": [("이미 다 끝내고 리팩토링 중이다 (J)", "J"), ("커피 수혈하며 밤새 달린다 (P)", "P")]},
             # 문항을 더 추가하려면 (E/I, S/N, T/F, J/P) 순서 고려해서 넣으면 됨
        ]
        
        self.scores = {"E":0, "I":0, "S":0, "N":0, "T":0, "F":0, "J":0, "P":0}
        self.current_idx = 0
        
        self.setup_ui()
        self.update_question()

    def setup_ui(self):
        # 상단 진행률
        self.lbl_progress = tk.Label(self.root, text="", font=("Arial", 10), fg="gray")
        self.lbl_progress.pack(pady=10)
        
        # 질문
        self.lbl_question = tk.Label(self.root, text="", font=("Arial", 14, "bold"), wraplength=450)
        self.lbl_question.pack(pady=30)
        
        # 버튼 프레임
        self.frame_btn = tk.Frame(self.root)
        self.frame_btn.pack(pady=10)
        
        # 선택지 버튼 A
        self.btn_a = tk.Button(self.frame_btn, text="", width=40, height=3, command=lambda: self.answer(0), bg="#e1f5fe")
        self.btn_a.pack(pady=5)
        
        # 선택지 버튼 B
        self.btn_b = tk.Button(self.frame_btn, text="", width=40, height=3, command=lambda: self.answer(1), bg="#ffebee")
        self.btn_b.pack(pady=5)

    def update_question(self):
        q = self.questions[self.current_idx]
        self.lbl_progress.config(text=f"진행 상황: {self.current_idx + 1} / {len(self.questions)}")
        self.lbl_question.config(text=q["q"])
        self.btn_a.config(text=q["opt"][0][0]) # 텍스트 표시
        self.btn_b.config(text=q["opt"][1][0])

    def answer(self, choice_idx):
        # 점수 계산
        target_type = self.questions[self.current_idx]["opt"][choice_idx][1]
        self.scores[target_type] += 1
        
        self.current_idx += 1
        
        if self.current_idx < len(self.questions):
            self.update_question()
        else:
            self.show_result()

    def show_result(self):
        # 결과 조합
        res = ""
        res += "E" if self.scores["E"] >= self.scores["I"] else "I"
        res += "S" if self.scores["S"] >= self.scores["N"] else "N"
        res += "T" if self.scores["T"] >= self.scores["F"] else "F"
        res += "J" if self.scores["J"] >= self.scores["P"] else "P"
        
        messagebox.showinfo("결과 발표", f"당신의 MBTI는 [ {res} ] 입니다!\n\n졸업하고 훌륭한 개발자가 되실 겁니다.")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MBTiApp(root)
    root.mainloop()