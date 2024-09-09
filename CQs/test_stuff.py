def big_func(a: int) -> int:
    return a + 2


def bigger_func(b: int) -> int:
    return big_func(a=b) * 2


def biggest_func(num: int) -> int:
    return bigger_func(b=num) ** 2


def main() -> None:
    print(str(biggest_func(num=110)) + "is a big number.")


main()
