# Зчитати рядок через кому, створити список із перелічених значень,
# вивести повідомлення відповідно до очікуваних значень
string = input()

match string.split(','):
    case ["apple"]:
        print("Only apple")
    case ["sun" | "Earth", "man"]:
        print("Sun or Earth")
