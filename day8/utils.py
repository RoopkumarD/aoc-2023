import math
from typing import List


def prime_factorize(num: int) -> List:
    i = 2
    factorized = []

    while num != 1:
        if num % i == 0:
            num = math.floor(num / i)
            factorized.append(i)
        else:
            i += 1

    return factorized


def common_number(nums: List):
    factorized = []
    for i in nums:
        factorized.append(prime_factorize(i))

    common_nums = []
    new_zeroth = []
    for factor in factorized[0]:
        count = 0
        for k in range(1, len(factorized)):
            if factor in factorized[k]:
                count += 1

        if count == len(factorized) - 1:
            common_nums.append(factor)
            for factors_list_k in range(1, len(factorized)):
                factorized[factors_list_k].remove(factor)
        else:
            new_zeroth.append(factor)

    final = 1
    for i in common_nums:
        final = final * i

    for i in new_zeroth:
        final = final * i

    for factors_list_k in range(1, len(factorized)):
        for k in factorized[factors_list_k]:
            final = final * k

    return final
