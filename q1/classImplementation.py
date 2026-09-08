class Song:
    def __init__(self, artist, difficulty, level, name, availability):
        self.artist = artist
        self.difficulty = difficulty
        self.level = level
        self.name = name
        self.__availability = availability

    def info(self):
        print("Name:", self.name)
        print("Artist:", self.artist)
        print("Difficulty:", self.difficulty)
        print("Level:", self.level)
        print("Availability:", self.__availability)

    def play(self):
        if self.__availability:
            print("Now playing:", self.name)
        else:
            print(self.name, "is currently unavailable.")

    def changeDifficulty(self, newDifficulty):
        self.difficulty = newDifficulty

    def getAvailability(self):
        return self.__availability

    def setAvailability(self, newAvailability):
        if isinstance(newAvailability, bool):
            self.__availability = newAvailability


song1 = Song("livetune", "Hard", 17, "Tell Your World", True)
song2 = Song("ryo", "Expert", 25, "Melt", True)

print("BEFORE")

print("Object 1:")
song1.info()

print()

print("Object 2:")
song2.info()

print("\nChanging Object 1 availability...")
song1.setAvailability(False)

print("\nAFTER")

print("Object 1:")
song1.info()

print()

print("Object 2:")
song2.info()
