from typing import Callable
from Gamepack import *

# story of Bang hallim jeon
class Hanlim(Gamepack):
    def __init__(self, name: str) -> None:
        super().__init__(name)
    
    def startscene(self, name: str) -> None:
        with open(f"./source/{name}.txt", 'r', encoding='utf-8') as scene:
            Hanlim.read(scene)
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

    def intro(self) -> None:
        self.startscene("intro")
        self.choice(self.writing, self.weaving)
    
    def writing(self) -> None:
        self.startscene("writing")
        self.choice(self.meet_Haebing, self.cut_Haebing)

    def weaving(self) -> None:
        self.startscene("weaving")
        self.choice(self.meet_son, self.cut_son)

    def meet_Haebing(self) -> None:
        self.startscene("meet_Haebing")
        self.choice(self.poet, self.no_poet)

    def cut_Haebing(self) -> None:
        self.startscene("cut_Haebing")
        self.choice(self.tell3, self.hide3)
    
    def meet_son(self) -> None:
        self.startscene("meet_son")
        self.choice(self.agree, self.reject)
    
    def cut_son(self) -> None:
        self.startscene("cut_son_ending")
        quit()
    
    def poet(self) -> None:
        self.startscene("poet")
        self.choice(self.child, self.oldman, third=self.fan)

    def no_poet(self) -> None:
        self.startscene("no_poet_ending")
        quit()
    
    def tell3(self) -> None:
        self.startscene("tell_ending3")
        quit()
    
    def hide3(self) -> None:
        self.startscene("hide_ending3")
        quit()
    
    def agree(self) -> None:
        self.startscene("agree_war")
        self.choice(self.boy1, self.girl1)

    def reject(self) -> None:
        self.startscene("reject_war")
        self.choice(self.boy2, self.girl2)
    
    def child(self) -> None:
        self.startscene("child")
        self.choice(self.tell1, self.hide1)

    def oldman(self)-> None:
        self.startscene("oldman")
        self.choice(self.tell2, self.hide2)
    
    def fan(self) -> None:
        self.startscene("fan")
        self.choice(self.use_fan, self.no_fan)
    
    def boy1(self) -> None:
        self.startscene("boy_ending1")
        quit()
    
    def girl1(self) -> None:
        self.startscene("girl_ending1")
        quit()
    
    def boy2(self) -> None:
        self.startscene("boy_ending2")
        quit()
    
    def girl2(self) -> None:
        self.startscene("girl_ending2")
        quit()
    
    def tell1(self) -> None:
        self.startscene("tell_ending1")
        quit()
    
    def hide1(self) -> None:
        self.startscene("hide_ending1")
        quit()
    
    def tell2(self) -> None:
        self.startscene("tell_ending2")
        quit()
    
    def hide2(self) -> None:
        self.startscene("hide_ending2")
        quit()
    
    def use_fan(self) -> None:
        self.startscene("use_fan_ending")
        quit()
    
    def no_fan(self) -> None:
        self.startscene("no_fan_ending")
        quit()


        


    
            