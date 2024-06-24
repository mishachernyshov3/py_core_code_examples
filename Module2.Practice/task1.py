# В залежності від оцінки визначити кометар викладача до роботи:
# 90-100: Excellent!
# 75-89: Well done!
# 60-74: You can do better.
# Інша: You don't pass the exam.


grade = int(input())

if grade >= 90:
    teacher_comment = "Excellent!"
elif grade >= 75:
    teacher_comment = "Well done!"
elif grade >= 60:
    teacher_comment = "You can do better."
else:
    teacher_comment = "You don't pass the exam."
