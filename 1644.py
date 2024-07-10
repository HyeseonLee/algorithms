import sys
import math

n = int(sys.stdin.readline().strip())

def find_prime_arr(n): # O(10^6 log(log10^6))
    is_prime = [True] * (n+1)
    is_prime[0]=is_prime[1] = False
    for i in range(2, int(math.sqrt(n))+1):
        if is_prime[i]:
            for j in range(2*i, n+1, i):
                is_prime[j] = False
    return [k for k in range(2,n+1) if is_prime[k]]

prime_arr = find_prime_arr(n)

# print(prime_arr)

def find_prime_sum_case(prime_arr, n):
    left = 0
    right = 0
    prime_sum = 0
    case = 0

    while right < len(prime_arr):
        if prime_sum == n:
            case += 1
            prime_sum -= prime_arr[left]
            left += 1
        elif prime_sum > n:
            prime_sum -= prime_arr[left]
            left += 1
        else:
            prime_sum += prime_arr[right]
            right += 1

    # prime_sum이 n과 같을 경우 체크
    while prime_sum >= n and left < len(prime_arr):
        if prime_sum == n:
            case += 1
        prime_sum -= prime_arr[left]
        left += 1

    return case

res = find_prime_sum_case(prime_arr, n)

print(res)