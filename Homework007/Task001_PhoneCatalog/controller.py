import view
import model

def UserMainMenu():
    view.printMainMenu()
    inp=""
    while inp != '6':
        inp=input("Введите Ваш выбор:")
        match inp:
            case "1":
                model.view_guide()
            case "2":
                name=input("Введите имя для поиска:")
                rec = model.find_by_name(name)
                if rec != 'default':
                    print(f'Найден номер: {rec}')
                else:
                    print("Имя не найдено")
            case "3":
                name=input("Введите имя:")
                number=input("Введите номер:")
                if model.add_record(name,number) != "default":
                    print("Запись добавлена")
                else:
                    print("Такое имя уже существует")
            case "4":
                model.exportXML()
                print("Файл XML записан")
            case "5":
                model.exportHTML()
                print("Файл HTML записан")
