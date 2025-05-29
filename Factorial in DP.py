fact_cache = [1]

def factorial(n):
    for i in range(len(fact_cache), n + 1):
        fact_cache.append(fact_cache[-1] * i)
    return fact_cache[n]

print("factorial for 5 = ", factorial(5))
print("factorial for 4 = ", factorial(4))
print("factorial for 7 = ", factorial(7))