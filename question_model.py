class Question:
  def __init__(self, text, answer):
    self.text = text
    self.answer = answer


Q1 = Question("ready?", "Yes")

print("start")
print(Q1.answer)
print("end")