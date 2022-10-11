from typing import TextIO
from typing import Callable

"""_Gamepack class for emulator_
"""
class Gamepack():
    def __init__(self, name: str) -> None:
        self.name = name # 게임 제목입니다.

    """_txt 파일을 읽고 0.1초 단위로 글자를 출력합니다. 줄 간 0.5초의 텀이 있습니다._
    """
    def read(scene: TextIO) -> None:
        import time

        script = scene.readlines()

        for story in script:
            for word in story:
                print(word, end = '', flush = True)
                time.sleep(0.1)
            time.sleep(0.5)
        print()

    """_파일을 읽고 read 함수로 출력합니다._ 
    """
    def startscene(self, name: str) -> None: 
        with open(f"./source/{name}.txt", 'r', encoding='utf-8') as scene:
            Gamepack.read(scene)
            print("-" * 60)

    """_사용자의 선택을 받습니다. 기본 2개, 최대 3개의 선택지를 입력받습니다._
    """
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