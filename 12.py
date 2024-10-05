"""Problem 12
    Given a number n, what is the smallest triangular number with over n divisors?"""


def prime_factorise(number: int) -> list[tuple[int]]:
    """Returns a dictionary of prime factors of a number, with their multiplicity as value."""

    n = number
    factor = 2
    prime_factors = {}

    while n > 1:
        if n % factor == 0:
            mult = prime_factors.get(factor, 0)
            prime_factors[factor] = mult + 1
            n = n // factor
        else:
            factor += 1
    return prime_factors


def number_of_factors(number: int) -> int:
    """Returns the number of factors of a number."""

    prime_factors = prime_factorise(number)
    multiplicities = prime_factors.values()

    no_factors = 1
    for mult in multiplicities:
        no_factors *= mult + 1

    return no_factors


def solution(number: int) -> int:
    """What is the smallest triangular number with over this many factors?"""

    i = 1
    while True:
        if i % 2 == 0:
            number_1 = i // 2
            number_2 = i + 1
        else:
            number_1 = i
            number_2 = (i+1)//2
        if number_of_factors(number_1)*number_of_factors(number_2) > number:
            return number_1 * number_2
        i += 1


if __name__ == "__main__":

    print(solution(500))
