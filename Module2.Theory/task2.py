# За числовим значенням відповіді на веб-запит вивести його текстове значення

status = int(input())

if status == 200:
    print("OK")
elif status == 201:
    print("Created")
elif status == 404:
    print("Not Found")
elif status == 500:
    print("Internal erver error")
else:
    print("ERROR")


match status:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 404:
        print("Not Found")
    case 500:
        print("Internal erver error")
    case _:
        print("ERROR")
