Question = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower()

match Question:
    case "42":
        print("yes")
    case "forty-two":
        print("yes")
    case "forty two":
        print("yes")
    case _:
        print("No")    