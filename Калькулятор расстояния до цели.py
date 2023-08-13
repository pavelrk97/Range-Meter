def calculate_distance(height, finger_length, eye_to_finger_distance, finger_projection_ratio):
    object_length = (finger_projection_ratio * finger_length) / 100  # Проекция длины объекта на палец
    distance = (height * eye_to_finger_distance) / object_length  # Расчет расстояния

    return distance
height_of_object = 8  # Высота измеряемого объекта в метрах
finger_length = 6  # Длина вашего большого пальца в сантиметрах
eye_to_finger_distance = 60  # Расстояние от глаз до пальца в сантиметрах
finger_projection_ratio = 1  # Процент проекции длины объекта на палец (в данном случае треть пальца)

distance = calculate_distance(height_of_object, finger_length, eye_to_finger_distance, finger_projection_ratio)
print("Расстояние до объекта:", distance, "метров")