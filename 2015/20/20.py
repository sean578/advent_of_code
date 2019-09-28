
def prime_factors(nr):
    i = 2
    factors = []
    while i <= nr:
        if (nr % i) == 0:
            factors.append(i)
            nr = nr / i
        else:
            i = i + 1
    return factors


def sum_of_factors(prime_factors):
    prime_factor_dict = {}
    for factor in prime_factors:
        prime_factor_dict[factor] = prime_factors.count(factor)

    factor_sum = 1
    for key, value in prime_factor_dict.items():
        sum = 0
        for i in range(value+1):
            sum = sum + key**i
        factor_sum = factor_sum * sum

    return factor_sum

presents_max = 0
houses = 1
not_found = True

while not_found:
    the_prime_factors = prime_factors(houses)
    presents = 10*sum_of_factors(the_prime_factors)
    if presents >= 34000000:
        not_found = False
    else:
        houses = houses + 1

    if presents > presents_max:
        presents_max = presents
        print(houses, presents)

print('answer', houses)



