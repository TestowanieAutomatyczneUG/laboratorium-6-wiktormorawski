password = 'Wicia'
special_characters = ['!', '"', '#', '$', '%', '&', ',', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<',
                      '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']


def program(password, special_characters):
    result = False
    for character in password:
        def helper(one_character):

            for special in special_characters:
                print(character, special)
                if one_character == special:
                    print("zgadza sie")

                    return True
                else:
                    pass


        if helper(character) == True:
            result = True
    return result


print(program(password, special_characters))
