# Перевірити, чи отримано очікувани значення (юніттести)

actual_submissions = [120, "Hello world!", ["Python", "JavaScript", "Dart"]]
expected_submissions = [120, "Hello world", ["Python", "C++"]]

for actual_submission, expected_submission in zip(actual_submissions, expected_submissions):
    if actual_submission != expected_submission:
        print(f"Wrong answer. Expected: {expected_submission}, actual: {actual_submission}")