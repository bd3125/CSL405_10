if __name__ == '__main__':
    with open('./Bhavya(info).txt', 'r') as file:
        lines = file.readlines()

        numberOfLines = len(lines)
        numberOfWords = sum(len(line.split()) for line in lines)
        numberOfCharacters = sum(len(line) for line in lines)

    print(f"Lines: {numberOfLines}")
    print(f"Words: {numberOfWords}")
    print(f"Characters: {numberOfCharacters}")
