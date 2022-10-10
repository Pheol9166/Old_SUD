import os
from hanlim import *

class Emulator():
    def __init__(self, gamepack: Gamepack) -> None:
        # it gets Gamepack
        self.gamepack = gamepack 
    
    # start the game
    def start(self) -> None:
        print(self.gamepack.name)
        print("-" * 60)
        while(1):
            answer = input("게임을 시작하시겠습니까? (네/아니오) ")
            if answer == "네":
                self.gamepack.intro()
            elif answer == "아니오":
                print("다음에 기회가 있길...")
                break
            else:
                print("입력이 잘못되었습니다. 다시 시도해주세요.")
                

game = Hanlim("新방한림전")
emul = Emulator(game)
emul.start()
os.system('pause')