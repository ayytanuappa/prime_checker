def is_prime(n):
   if n < 2:
      return False
   for i in range(2, int(n**0.5) + 1):
     if n % i == 0:
        return False
    return True

   number = int(input("Enter a number: "))
   if is_prime(number):
       print(f"{number} is prime")
   else:
       print(f"{number} is not prime")
                                                
