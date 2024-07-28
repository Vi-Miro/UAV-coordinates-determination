import math

'''ввод градусов магнитного склонения, среднего сближения меридиан, 
   а также своих координат взлета'''

print("Режим - Предварительная подготовка: ")
mag = input("Введите градусы магнитного склонения: ")
mid = input("Введите градусы среднего сближения: ")
print("\n")

print("Режим - Предполетная подготовка: ")
self_x = float(input("Введите свои координаты (Х): "))
self_y = float(input("Введите свои координаты (У): "))
print("\n")

''' функция для определения дистанции до объекта. 
    Входные данные: угол наклона камеры, данные дальномера'''


def get_distance(camera_angle, lazer_distance):
    distance = lazer_distance * math.cos(math.radians(camera_angle))
    return distance


'''функция перевода угла из градусов, минут, координат 
    в десятичный формат'''


def dms_to_dd(x):
    x = x.split(',')
    #print(x)
    return int(x[0]) + int(x[1]) / 60


'''преобразование магнитного склонения и 
   среднего сближения в десятичный формат'''

declination = dms_to_dd(mag)
# print("Магнитное склонение (десятичное): ", declination)

convergence = dms_to_dd(mid)
# print("Среднее сближение (десятичное): ", convergence, "\n")


'''функция определения угла направления относительно линии сетки.
    Входные данные: магнитный курс, магнитное склонение, среденее сближение'''


def get_map_angle(magnetic_course, declination, convergence):
    map_angle = magnetic_course + declination + convergence
    return map_angle


'''функция определения координат объекта в зависимости от угла направления.
    Входные данные: расстояние до объекта, угол направления, собсьвенные координаты'''


def get_obj_coordinates(distance, map_angle, self_x, self_y):
    if 0 <= map_angle <= 90:
        delta_x = distance * math.cos(math.radians(map_angle))
        delta_y = distance * math.sin(math.radians(map_angle))

        obj_x = self_x + delta_x
        obj_y = self_y + delta_y

    elif 90 < map_angle <= 180:
        map_angle = 180 - map_angle

        delta_x = distance * math.cos(math.radians(map_angle))
        delta_y = distance * math.sin(math.radians(map_angle))

        obj_x = self_x - delta_x
        obj_y = self_y + delta_y

    elif 180 < map_angle <= 270:
        map_angle = 270 - map_angle

        delta_x = distance * math.sin(math.radians(map_angle))
        delta_y = distance * math.cos(math.radians(map_angle))

        obj_x = self_x - delta_x
        obj_y = self_y - delta_y

    elif 270 < map_angle <= 360:
        map_angle = 360 - map_angle

        delta_x = distance * math.cos(math.radians(map_angle))
        delta_y = distance * math.sin(math.radians(map_angle))

        obj_x = self_x + delta_x
        obj_y = self_y - delta_y

    return int(obj_x), int(obj_y)


'''функция внесения данных с дрона и получения координат объекта'''


def flight_mode(declination, convergence, self_x, self_y):
    print("Режим - Полет: ")
    camera_angle = float(input("Введите угол наклона камеры: "))
    lazer_distance = float(input("Введите показания дальномера: "))
    magnetic_course = float(input("Введите магнитный курс: "))

    distance = get_distance(camera_angle, lazer_distance)
    print("Расстояние до объекта: ", int(distance))

    map_angle = get_map_angle(magnetic_course, declination, convergence)
    # print("Угол направления: ", map_angle, "\n")
    print("\n")

    obj_coordinates = get_obj_coordinates(distance, map_angle, self_x, self_y)
    print("Координаты объекта (Х, У): ", obj_coordinates, "\n")


if __name__ == '__main__':
    flight_mode(declination, convergence, self_x, self_y)

    answer = input("Хотите продолжить? (y - да, n - нет): ")

    while answer != 'n':
        pre_answer = input("Изменить координаты взлета? (y - да, n - нет): ")
        print("\n")

        if pre_answer == 'y':
            print("Режим - Изменение координат взлета: ")
            self_x = float(input("Введите свои координаты (Х): "))
            self_y = float(input("Введите свои координаты (У): "))
            print("\n")

        flight_mode(declination, convergence, self_x, self_y)

        answer = input("Хотите продолжить? (y - да, n - нет): ")
        print("\n")