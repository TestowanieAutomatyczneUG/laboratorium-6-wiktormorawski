class ValidPassword:
    def Create_Password(self, password):
        special_characters = ['!', '"', '#', '$', '%', '&', ',', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<',
                              '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
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

                    if helper() == True:
                        return True
                    else:
                        raise ValueError("Doesn't contain special Characters")
                else:
                    raise ValueError("Doesn't contain any digit")
            else:
                raise ValueError("Doesn't contain Capital Letter")


        else:
            raise ValueError("Too short Password")


temp = ValidPassword()
haslo1 = temp.Create_Password("wiktoreK1!")
print(haslo1)
