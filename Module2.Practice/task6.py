# Створити конфіг для веб-сайту із мовою, часовим поясом і назвою сайту. Встановити значення за змовчуванням.

language = input()
timezone = input()
site_name = input()

config = {
    'language': language or 'uk',
    'timezone': timezone or 'UTC',
    'site_name': site_name or 'Coffee shop',
}
