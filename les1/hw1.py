def is_it_palindrome(st):
    if st[::-1] == st:
        print(True)
    else:
        print(False)


is_it_palindrome('helloworld')