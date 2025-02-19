
def isProst(number : int) -> bool:
    for i in range(number):
        if number % i == 0:
            return False
    return True