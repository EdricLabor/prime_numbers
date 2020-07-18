Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> for n in range (1, 101):
    count = 0
    for i in range(2, (n//2 + 1)):
        if(n % i == 0):
            count = count + 1
            break
    if (count == 0 and n != 1):
        print(" %d" %n, end = '  ')

        
 2   3   5   7   11   13   17   19   23   29   31   37   41   43   47   53   59   61   67   71   73   79   83   89   97  
>>> 