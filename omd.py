# Guido van Rossum <guido@python.org>

import random


def weather_condition():
    """
    No args. Create random weather condition.
    Input: None
    Return: weather condition - int
    """
    condition_variant = random.randint(0, 1)
    if condition_variant > 0:
        print("Пошел дождь. Довольно сильный дождь с молниями.")
    else:
        print("Погода была солнечная, немного облачная.")
    return condition_variant > 0


def step2_umbrella():
    """
    Print what's next WITH umbrella.
    Input: None
    Return: None
    """
    print("Утка-маляр все же взяла зонтик. ☂️")
    is_raining = weather_condition()
    if is_raining:
        print(
            "Утка-маляр прикрылась зонтиком, не промокла.",
            "Лишь немного ноги замерзли.",
        )
    else:
        print("Утка-маляр пришла в бар, напилась и забыла там зонтик.")


def step2_no_umbrella():
    """
    Print what's next WITHOUT umbrella.
    Input: None
    Return: None
    """
    print("Утка-маляр все же не взяла зонтик. ☂️")
    is_raining = weather_condition()
    if is_raining:
        print(
            "Утка-маляр полностью промокла!",
            "В баре решила пить сразу крепкие напитки.",
        )
    else:
        print(
            "Утка-маляр довольна собой.", "Как будто знала что зонтик ей не пригодится."
        )


def step1():
    print("Утка-маляр 🦆 решила выпить зайти в бар. " "Взять ей зонтик? ☂️")
    option = ""
    options = {"да": True, "нет": False}
    while option not in options:
        print("Выберите: {}/{}".format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == "__main__":
    step1()
