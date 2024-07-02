# Порівняння двох рядків незалежно від регістру
# Додати новий тег, якщо такого ще не існує.

existed_tags = {
    "Python",
    "Data Science",
    "Machine Learning",
    "JavaScript",
    "React",
    "WordPress",
    "CSS",
}

new_tag = input("Enter a tag name: ").strip()
new_tag_lowercase = new_tag.lower()
is_tag_existed = False

for tag in existed_tags:
    if new_tag_lowercase == tag.lower():
        is_tag_existed = True
        break

if not is_tag_existed:
    existed_tags.add(new_tag)
