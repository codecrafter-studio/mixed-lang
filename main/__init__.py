class Mixed():
    def __init__(self, file) -> None:
        self.file = file

    def add(self, suma : int, sumb: int):
        try:
            return suma + sumb
        except:
            print("Error from <{}> :\n    add() only can use int".format(self.file.upper()))