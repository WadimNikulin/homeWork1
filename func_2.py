def my_func(name, surname, year, town, email, telephone):
    data = "Имя: " + name + ", " + "Фамилия: " + surname + ", " + "Год рождения: " + str(year) + ", " \
           + "Город проживания: " + town + ", " + "Адрес электронной почты: " + str(email) + ", "\
           + "Номер телефона: " + str(telephone)
    return data


name = input("Введите имя: ")
surname = input("Введите фамилию: ")
year = input("Введите год рождения: ")
town = input("введите город проживания: ")
email = input("Введите адрем электронной почты: ")
telephone = input("Введите номер телефона: ")

print(my_func(name, surname, year, town, email, telephone))
