# За допомогою тернарного оператора визначити, чи склав учень екзамен (отримав від 60 балів).

grade = int(input())

passed_exam = "Passed" if grade >= 60 else "Not passed"
print(passed_exam)
