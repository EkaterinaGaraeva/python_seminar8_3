

def Intface(i:str):
    match i:
        case "Welcome":
            print('---------------------------------------------')
            print('Вы вошли в базу данных')
        case "Menu":
            print('---------------------------------------------')
            print('МЕНЮ базы данных')
            # print('1. Импортиовать данные в справочник')
            # print('2. Экспортировать данные из справочника')
            print('3. добавление данных в базу данных')
            print('4. Выход из базы данных')
        case "End":
            print('----------------------------------------------')
            print('Выберите дальнейшее действие')
            print('1. Выход в главное меню')
            print('2. Выход из программы')
