import doctest, unittest


class ValidPassword:
    """
    Should return True if the password is correct , otherwise it raises ValueError
    >>> temp = ValidPassword()
    >>> temp.Create_Password('wiktor')
    Traceback (most recent call last):
      ...
    ValueError: Too short Password
    >>> temp.Create_Password('wiktorek')
    Traceback (most recent call last):
      ...
    ValueError: Doesn't contain Capital Letter
    >>> temp.Create_Password('Wiktorek')
    Traceback (most recent call last):
      ...
    ValueError: Doesn't contain any digit
    >>> temp.Create_Password('Wiktorek1')
    Traceback (most recent call last):
      ...
    ValueError: Doesn't contain special Characters
    >>> temp.Create_Password('1Wiktorek')
    Traceback (most recent call last):
      ...
    ValueError: Doesn't contain special Characters
    >>> temp.Create_Password('11111WWWW')
    Traceback (most recent call last):
      ...
    ValueError: Doesn't contain special Characters
    >>> temp.Create_Password('1Wiktorek$')
    True
    >>> temp.Create_Password(123)
    Traceback (most recent call last):
      ...
    TypeError: Not a string
    >>> temp.Create_Password('1Wiktorek$'+ 123)
    Traceback (most recent call last):
      ...
    TypeError: can only concatenate str (not "int") to str
    >>> temp.Create_Password('1111WWWW').helper()
    Traceback (most recent call last):
      ...
    ValueError: Doesn't contain special Characters

    """

    def Create_Password(self, password):
        special_characters = ['!', '"', '#', '$', '%', '&', ',', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<',
                              '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
        if type(password) == str:
            if len(password) >= 8:
                if password.islower() == False:
                    if any(char.isdigit() for char in password) == True:
                        def helper():
                            for character in password:
                                for special in special_characters:
                                    if character == special:
                                        return True
                                    else:
                                        pass

                        if helper():
                            return True
                        else:
                            raise ValueError("Doesn't contain special Characters")
                    else:
                        raise ValueError("Doesn't contain any digit")
                else:
                    raise ValueError("Doesn't contain Capital Letter")

            else:
                raise ValueError("Too short Password")
        else:
            raise TypeError("Not a string")


class Test_ValidPassword(unittest.TestCase):
    def setUp(self):
        self.temp = ValidPassword()

    def test_length_lower_than_8(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.Create_Password('Wikto1$')

    def test_no_digit(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.Create_Password('Wikto#rek')

    def test_not_a_string_passed(self):
        with self.assertRaisesWithMessage(TypeError):
            self.temp.Create_Password(123423534534)

    def test_no_CAPITAL_letter(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.Create_Password('12wiktorr#@$')

    def test_no_Special_Character(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.Create_Password('123441WWWIII')

    def test_with_everything_but_only_CAPITAL_LETTERS(self):
        self.assertEqual(self.temp.Create_Password('12WIKTOR#$%'), True)

    def test_with_everything_with_CAPITAL_LETTERS_and_lower_letters(self):
        self.assertEqual(self.temp.Create_Password('12WIkoR#$%'), True)

    def tearDown(self):
        self.temp = None

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
    doctest.testmod()
