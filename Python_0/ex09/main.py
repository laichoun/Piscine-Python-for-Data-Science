from ft_package.count_in_list import count_in_list


def main():
    '''
    call the function count_in_list imported from ft_package
    '''
    print(count_in_list(["toto", "tata", "toto"], "toto"))
    print(count_in_list(["toto", "tata", "toto"], "tutu"))


if (__name__ == "__main__"):
    main()
