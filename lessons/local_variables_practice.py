def less_than_10(num: int) -> None:
    """tell me if num is less than 10"""
    dub: int = num * 2  # number goes from 5 to 10 and becomes dub
    dub = dub - 1  # dub becomes 10-1 so new dub is 9
    print(dub)  # prints updated dub (9)
    if num < 10:
        print("small number")
    else:
        print("Big number")
    print("have a nice day")


# less_than_10(num=10)


def number_info(num: int) -> int:
    if num < 10:
        print("Small number.")
    else:
        if num % 2 == 0:
            print("Even number.")
        else:
            print("Odd number.")
    return num


# number_info(num=11)
# print(number_info(num=4))


def get_weather_report() -> str:
    """Display weather information"""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket.")
    elif weather == "hot":
        print("Keep cool out there.")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
