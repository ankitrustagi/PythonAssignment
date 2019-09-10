"""
Write a program which asks the user to guess a predefined alphabet. 
Raise custom exceptions if the entered alphabet entered if smaller or greater than the predefined alphabet.
"""

class CustomException(Exception):
  """Base class for other exceptions"""
class ValueTooSmallError(CustomException):
   """Raised when the input value is too small"""
   pass
class ValueTooLargeError(CustomException):
   """Raised when the input value is too large"""
   pass


if __name__=="__main__":
  alphabet = 'V'
  while True:
    try:
       i_alp = input("Enter a alphabet: ")
       if i_alp < alphabet:
           raise ValueTooSmallError
       elif i_alp > alphabet:
           raise ValueTooLargeError
       break
    except ValueTooSmallError:
       print("This value is too small, try again!")
    except ValueTooLargeError:
       print("This value is too large, try again!")
  print("Congratulations! You guessed it correctly.")
