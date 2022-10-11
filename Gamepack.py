from typing import TextIO
from typing import Callable

# Gamepack - Game(story)
class Gamepack():
    def __init__(self, name: str) -> None:
        # game title
        self.name = name

    # read text and print it 
    def read(scene: TextIO) -> None:
        import time

        script = scene.readlines()
        
        for story in script:
            for word in story:
                print(word, end = '', flush = True)
                time.sleep(0.1)
            time.sleep(0.5)
        print()

    def startscene(self, name: str) -> None:
        with open(f"./source/{name}.txt", 'r', encoding='utf-8') as scene:
            Gamepack.read(scene)
            print("-" * 60)

    def choice(self, left: Callable, right: Callable, third=None):
        while (1):
            answer = input("당신의 선택은: ")
            if answer == "ㄱ":
                left()
            elif answer == "ㄴ":
                right()
            elif answer == "ㄷ":
                third()
            else:
                print("다시 입력해주세요!")
                print()