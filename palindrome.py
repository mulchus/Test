def is_palindrome(string: str) -> bool:
    # filtered_string = ''.join(filter(str.isalnum, string)).lower()
    filtered_string = ''.join(char.lower() for char in string if char.isalnum())
    return filtered_string == filtered_string[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(is_palindrome("Шалаш"))
