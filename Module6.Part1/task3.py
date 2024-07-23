# Використання протоколів
from typing import Protocol


class Speaker(Protocol):
    def speak(self) -> None:
        pass


class A:
    def speak(self) -> None:
        print("Hello")


def f(speaker: Speaker) -> None:
    speaker.speak()


f(A())
f(12)
