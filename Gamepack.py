from typing import TextIO

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