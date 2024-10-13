# python-lec11-oct-09-24

## subjects learned:

1) function all() on List (like every() in js):

   receive a list of boolean values and returns True if all values are True, else returns False.
    * same for [1,0,1,True,2<2]
2) function any() on list (like some() in js):

   receive a list of boolean values and returns True if at **least one** is True
3) Strings-Functions:
    * len(string)- size of the string
      after the string:
   ```
   'string'.strip()
   ```  
    * strip()- like trim() in js- remove the spaces in the start and end of the string
    * upper() - changes all characters to CAPITAL letters.
    * lower() - changes all characters to small letters.
    * replace(oldValue, newValue)- changes the substring 'oldValue' to the newValue, case sensitive with the values,
      replace all occurrences
    * split() - creates and returns a new list from the origin string by the given char. if not giving the char, the
      default is space ' '
    * join()- receive a list, separator and returned a new string:

      ```
      'separator'.join([list of chars])
      ```
      ** works only on list of strings, else raised 'TypeError' exception

      ** on empty list will return empty string("")
    * startwith(searchString),endswith(searchString)- returns true if the string starts with the searchString.
    * endswith(searchString)- returns true if the string ends with the searchString.
    * capitalize()- capital only the first letter
    * title()- capital each first letter in the list
    * isalpha()- returns true if all chars are letters a-z and not numbers/ special letters
    * isdigit()- returns true if all chars are digits 0-9
    * islower() - returns True if all chars are small letters
    * isupper()- returns True if all chars are capital letters
    * swapcase()- swap all letters from capital to lower and reverse.
    * zfill(5) fill with zeros to 5 digits - on the left
    * center(with=12, fillChar='-')- put the string in the center,fill to be 12 chars with given fill char
    * isspaces()- returns true if all string is spaces
    * indexes: string[:::] like in lists

## extra subjects:
