import easygui
from typing import List

class FileUtils:

    def getNumerosFromFile(self) -> List[int]:
        numbers = []
        file_path = easygui.fileopenbox()
        file = open(f"{file_path}", "r")
        for line in file:
            valor = int(line.replace("\n", ""))
            numbers.append(valor)
        return numbers