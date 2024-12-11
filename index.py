import json

# Функция вывода меню на экран.


def showMenu():
    # Вывод меню пользователю с описанием доступных действий.
    menu_str = """\n
        ____________________________________

          1) Вывести все записи
          2) Вывести запись по полю
          3) Добавить запись
          4) Удалить запись по полю
          5) Выйти из программы
        ____________________________________
        """
    return menu_str


# Функция вывода информации об автомобиле.
def showVehicleInfo(data, car_id=0):
    # Цикл перебора всех автомобилей в списке data.
    for car in data:
        if car_id == 0:
            # Вывод информации об автомобиле в удобном формате.
            print(f"""
                Номер записи: {car["id"]},
                Название модели: {car["name"]},
                Название производителя: {car["manufacturer"]},
                Заправляется бензином: {f"да" if car["is_petrol"] else "нет"},
                Объем бака: {car["tank_volume"]}
              """)
        else:
            if car_id == car.get("id"):
                print(f"""
                Номер записи: {car["id"]},
                Название модели: {car["name"]},
                Название производителя: {car["manufacturer"]},
                Заправляется бензином: {car["is_petrol"]},
                Объем бака: {car["tank_volume"]}
                """)


# Функция ввода информации о новом автомобиле.
def inputAndCheckNewCarInfo():

    # создание функции для вывода ошибки
    def errorMessage(value):
        print(f"""
          Недопустимое значение {value},
          Повторите ввод корректно:\n""")


    def is_string(input_str):
        if isinstance(input_str, str) and (not input_str.isdigit()):
            return True
        errorMessage(input_str)
        return False
   

    # создание функции для проверки корректного ввода ответа
    def checkAnswer(answer):
        is_string(answer)
        if (answer.lower() == "да") or (answer.lower() == "нет"):
            return True
        else:
            errorMessage(answer)
            return False

    # создание функции для преобразования значения в float тип
    def toFloat(input_num):
        try:
            return True, float(input_num)
        except (ValueError, TypeError):
            errorMessage(input_num)
            return False, float("NaN")

    current_step = 1
    new_data = []
    # Запрос данных о новом автомобиле у пользователя.
    while current_step < 5:
        if current_step == 1:
            new_name = input("Введите название модели: ")
            new_data.append(new_name)

        elif current_step == 2:
            new_manufacturer = input("Введите производителя: ")
            new_data.append(new_manufacturer)


        elif current_step == 3:
            new_is_petrol = input(
                "Машина заправляется бензином (да/нет): ").strip()
            if not checkAnswer(new_is_petrol):
                continue
            new_data.append(new_is_petrol)

        elif current_step == 4:
            is_float, new_tank_volume = toFloat(input("Введите объём бака: "))
            if not is_float:
                continue
            new_data.append(new_tank_volume)

        current_step += 1

        # Возвращает список с данными о новом автомобиле.
    return new_data


# Функция создания словаря с информацией о новом автомобиле.
def createNewCar(id, name, manufacturer, petrol, tank_volume):
    # Создание словаря с данными о новом автомобиле.
    new_car = {
        "id": id,
        "name": name,
        "manufacturer": manufacturer,
        "is_petrol": True if petrol.lower() == "да" else False,
        "tank_volume": tank_volume
    }
    # Возвращает словарь с данными о новом автомобиле.
    return new_car


# Функция добавления нового автомобиля в список.
def addNewCar(data, new_car):
    # Добавление нового автомобиля в список data.
    data.append(new_car)


# Функция удаления автомобиля из списка.
def deleteCar(data, id, flag):
    # Цикл перебора всех автомобилей в списке data.
    for car in data:
        # Если ID совпадает, удаляем автомобиль из списка и устанавливаем флаг find в True.
        if id == car.get("id", 0):
            data.remove(car)
            flag = True
            break
    return flag


# Функция вывода информации о завершении программы и количестве выполненных операций.
def output(count, actions_list, actions_count):
    # Вывод информации о завершении программы и количестве выполненных операций.
    print(f"""
        Программа завершена.
        Кол-во операций: {count}\n
       """)

    # Вывод статистики по каждой операции
    count = 1
    print("Количество выполненных операций: ")
    for act in actions_list:
        print(f"""
            {act} : {actions_count[count]}
           """)
        count += 1
    # Возвращает None, чтобы не выводить лишний None в консоль
    return None


def checkId(id):
    while not id.isdigit():
        print("Неверное значение. Введите id корректно!")
        id = input("Введите номер записи машины: ")
    return id


# Открытие файла cars.json в режиме чтения с кодировкой utf-8.
with open("ipo-lr7-4-3/cars.json", 'r', encoding='utf-8') as file:
    # Загрузка данных из файла в переменную data.
    data = json.load(file)

# Инициализация счетчика выполненных операций.
count = 0

# Список доступных действий.
actions_list = [
    "Вывести все записи",
    "Вывести запись по полю",
    "Добавить запись",
    "Удалить запись по полю",
    "Выйти из программы"
]

# Словарь для подсчета количества каждой операции.
actions_count = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
}

# Бесконечный цикл меню.
while True:
    # Вывод меню на экран.
    print(showMenu())

    # Получение номера действия от пользователя.
    num = int(input("Введите номер пункта: "))
    find = False

    # Обработка выбора пункта меню.
    if num == 1:
        # Вывод информации обо всех автомобилях.
        showVehicleInfo(data)
        # Увеличение счетчиков.
        count += 1
        actions_count[1] += 1

    elif num == 2:
        # Получение ID автомобиля от пользователя.
        id = input("Введите номер записи машины: ")
        id = checkId(id)

        # Поиск автомобиля по ID.
        for car in data:
            if id == car.get("id", 0):
                # Вывод информации об автомобиле.
                showVehicleInfo(data, id)
                find = True
                break

        # Увеличение счетчиков.
        count += 1
        actions_count[2] += 1

        # Вывод сообщения, если автомобиль не найден.
        if not find:
            print("Запись не найдена.")

    elif num == 3:
        find = False
        last_id = int(data[-1].get("id")) + 1

        new_name, new_manufacturer, new_is_petrol, new_tank_volume = inputAndCheckNewCarInfo()
        # Создание нового автомобиля и добавление его в список.
        new_car = createNewCar(
            last_id, new_name, new_manufacturer, new_is_petrol, new_tank_volume)
        addNewCar(data, new_car)
        # Сохранение изменений в файл.
        with open("cars.json", 'w', encoding='utf-8') as out_file:
            json.dump(data, out_file)

        print("Машина успешно добавлена.")

        # Увеличение счетчиков.
        count += 1
        actions_count[3] += 1

    elif num == 4:
        # Получение ID автомобиля для удаления.
        id = input("Введите номер записи машины: ")
        id = checkId(id)

        find = False

        # Удаление автомобиля из списка.
        find = deleteCar(data, id, find)
        # Вывод сообщения, если автомобиль не найден.
        if not find:
            print("Запись не найдена.")
        else:
            # Сохранение изменений в файл.
            with open("cars.json", 'w', encoding='utf-8') as out_file:
                json.dump(data, out_file)
            print("Запись успешно удалена.")
        # Увеличение счетчиков.
        count += 1
        actions_count[4] += 1

    elif num == 5:
        # Увеличение счетчика.
        actions_count[5] += 1
        # Вывод статистики и завершение программы.
        output(count, actions_list, actions_count)
        break

    # Обработка некорректного ввода.
    else:
        print("Такого номера нет.")

