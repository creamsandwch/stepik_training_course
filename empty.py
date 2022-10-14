
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def __init__(self, training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        output_msg = (f'Тип тренировки: {self.training_type}; \n'
                      f'Длительность: {self.duration:.3f} ч.; \n'
                      f'Дистанция: {self.distance:.3f} км; \n'
                      f'Ср. скорость: {self.speed:.3f} км/ч; \n'
                      f'Потрачено ккал: {self.calories:.3f}.')
        return output_msg


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: float = 1000
    MIN_IN_HR: float = 60

    action: int
    duration: float  # Время тренировки - в часах
    weight: float

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий.
           Этот метод задаётся только в дочерних классах"""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        info_object = InfoMessage(
            type(self).__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories()
            )
        return info_object


class Running(Training):
    """Тренировка: бег."""

    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        spent_calories = (
            (coeff_calorie_1 * self.get_mean_speed() - coeff_calorie_2)
            * self.weight
            / self.M_IN_KM
            * self.duration
            * self.MIN_IN_HR
        )
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    height: float

    def __init__(
        self,
        action: int,
        duration: float,
        weight: float,
        height: float
    ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Return spent calories during
        training type specified in the class"""
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 2
        coeff_calorie_3 = 0.029

        spent_calories = (
            (
                coeff_calorie_1
                * self.weight
                + (self.get_mean_speed() ** coeff_calorie_2 // self.height)
                * coeff_calorie_3
                * self.weight
            )
            * self.duration
            * self.MIN_IN_HR
        )

        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38

    length_pool: float
    count_pool: float
    mean_speed: float

    def __init__(
        self,
        action: int,
        duration: float,
        weight: float,
        length_pool: float,
        count_pool: float
    ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        mean_speed = (
            self.length_pool
            * self.count_pool
            / self.M_IN_KM
            / self.duration)
        return mean_speed

    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 1.1
        coeff_calorie_2 = 2
        spent_calories = (
            (self.get_mean_speed()
             + coeff_calorie_1)
            * coeff_calorie_2
            * self.weight)
        return spent_calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    id_to_training = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    for key, value in id_to_training.items():
        if key == workout_type:
            training_class = value(*data)
    return training_class


def main(training: Training) -> None:
    """Главная функция."""
    info_message = training.show_training_info()

    print(info_message.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
