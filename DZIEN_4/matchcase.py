def provideAccess(user):
    return {
        "username":user,
        "password":"abc123"

    }

def runMatch():
    user = str(input("podaj nazwę użytkownika: ")).strip()
    match user:
        case "Leon" | "Olga":
            print("Nie masz dostępu do bazy XYZ!")
        case "Benedykt":
            print("Uzyskujesz dostęp do bazy XYZ!")
            data = provideAccess("Benedykt")
            print(data)
        case _:
            print("nie jest członkiem orgaznizacji, nie posiadasz praw dostępu...")

if __name__ == '__main__':
    for _ in range(2):
        runMatch()
