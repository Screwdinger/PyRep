
def factorial(n):
    fac = 1
    for  i in range(n, 0, -1):
        fac *= i
    print("Factorial of ",n, "is: ", fac)

def fib(n):
    prev_num = 0
    new_num = 1
    for i in range(0, n, 1):
        print(new_num, end=" ")
        temp = prev_num
        prev_num = new_num
        new_num += temp

def palindrome(word):
    flag = 0 
    size = len(word)
    for i in range(0, int(size/2), 1):
        if word[i] == word[size - i - 1]:
            # print("Word is palindrome")
            flag += 1
        
    if flag == int(size/2):
        print("Word is palindrome")
    else: 
        print("Word is not a palindrome")

def proper():

    for i in range(2, 100000):
        
        divisors = []

        for j in range(1, i):

            if i % j == 0:
                divisors.append(j)
        
        if sum(divisors) == i:
            print(i)

def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            z = 1
            break
        else:
            z = 0
    if z == 0:
        print("Number is prime")
    else:
        print("Number is not prime")

def table(n):
    for i in range(1,11):
        print(n, " x ", i, " = ", n*i)

def reverse(sentence):
    size = len(sentence)
    reversed_sentence = []
    sen = list(sentence) 
    for i in range(size-1, -1, -1):
        reversed_sentence.append(sen[i])
    reversed_sen = str(reversed_sentence)
    print(reversed_sen)

def main():
    #num = int(input("Enter a number: "))
    #table(num)
    #isprime(num)
    #fib(num)
    #proper()

    # word = input("Enter a word: ")
    # palindrome(word)

    sentence = input("Enter a string: ")
    reverse(sentence)

    print()
    #factorial(num)


if __name__ == '__main__':
    main()
    
