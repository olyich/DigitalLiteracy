class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
        title (str): Название книги (не может быть пустым)
        author (str): Автор книги (не может быть пустым)
        pages (int): Количество страниц (должно быть положительным числом)
    """

    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация объекта Book.

        Args:
            title: Название книги
            author: Автор книги
            pages: Количество страниц

        Raises:
            ValueError: Если title или author пустые, или pages <= 0
        """
        if not title:
            raise ValueError("Название книги не может быть пустым")
        if not author:
            raise ValueError("Автор книги не может быть пустым")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")

        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_read: int = 10) -> int:
        """
        Симулирует чтение книги, возвращая количество оставшихся страниц.

        Args:
            pages_read: Количество прочитанных страниц (по умолчанию 10)

        Returns:
            int: Оставшееся количество страниц

        Raises:
            ValueError: Если pages_read <= 0 или больше чем pages

        Examples:
            >>> book = Book("1984", "George Orwell", 100)
            >>> book.read(20)
            80
            >>> book.read()
            70
        """
        if pages_read <= 0:
            raise ValueError("Нельзя прочитать отрицательное или нулевое количество страниц")
        if pages_read > self.pages:
            raise ValueError("Нельзя прочитать больше страниц чем есть в книге")

        self.pages -= pages_read
        return self.pages

    def get_info(self) -> str:
        """
        Возвращает информацию о книге.

        Returns:
            str: Строка с информацией

        Examples:
            >>> book = Book("1984", "George Orwell", 100)
            >>> book.get_info()
            'Книга "1984" автор George Orwell, 100 страниц'
        """
        return f'Книга "{self.title}" автор {self.author}, {self.pages} страниц'


class BankAccount:
    """
    Класс, представляющий банковский счет.

    Атрибуты:
        owner (str): Владелец счета
        balance (float): Текущий баланс (не может быть отрицательным)
        currency (str): Валюта счета (3 символа, например 'USD')
    """

    def __init__(self, owner: str, balance: float, currency: str = 'USD'):
        """
        Инициализация объекта BankAccount.

        Args:
            owner: Владелец счета
            balance: Начальный баланс
            currency: Валюта счета (по умолчанию 'USD')

        Raises:
            ValueError: Если balance отрицательный или currency не 3 символа
        """
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        if len(currency) != 3:
            raise ValueError("Валюта должна состоять из 3 символов")

        self.owner = owner
        self.balance = balance
        self.currency = currency.upper()

    def deposit(self, amount: float) -> float:
        """
        Пополняет счет на указанную сумму.

        Args:
            amount: Сумма для пополнения

        Returns:
            float: Новый баланс

        Raises:
            ValueError: Если amount <= 0

        Examples:
            >>> account = BankAccount("John Doe", 100.0)
            >>> account.deposit(50.0)
            150.0
        """
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")

        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Снимает указанную сумму со счета.

        Args:
            amount: Сумма для снятия

        Returns:
            float: Новый баланс

        Raises:
            ValueError: Если amount <= 0 или недостаточно средств

        Examples:
            >>> account = BankAccount("John Doe", 100.0)
            >>> account.withdraw(30.0)
            70.0
        """
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")

        self.balance -= amount
        return self.balance

    def convert_currency(self, rate: float, new_currency: str) -> None:
        """
        Конвертирует баланс в другую валюту по указанному курсу.

        Args:
            rate: Курс конвертации (должен быть > 0)
            new_currency: Новая валюта (3 символа)

        Raises:
            ValueError: Если rate <= 0 или new_currency не 3 символа

        Examples:
            >>> account = BankAccount("John Doe", 100.0, 'USD')
            >>> account.convert_currency(0.85, 'EUR')
        """
        if rate <= 0:
            raise ValueError("Курс конвертации должен быть положительным")
        if len(new_currency) != 3:
            raise ValueError("Новая валюта должна состоять из 3 символов")

        self.balance *= rate
        self.currency = new_currency.upper()


class Smartphone:
    """
    Класс, представляющий смартфон.

    Атрибуты:
        brand (str): Бренд смартфона
        model (str): Модель смартфона
        battery_level (int): Уровень заряда батареи (0-100%)
        is_on (bool): Включен ли смартфон
    """

    def __init__(self, brand: str, model: str, battery_level: int = 100):
        """
        Инициализация объекта Smartphone.

        Args:
            brand: Бренд смартфона
            model: Модель смартфона
            battery_level: Начальный уровень заряда (по умолчанию 100%)

        Raises:
            ValueError: Если battery_level не в диапазоне 0-100
        """
        if not 0 <= battery_level <= 100:
            raise ValueError("Уровень заряда должен быть в диапазоне 0-100%")

        self.brand = brand
        self.model = model
        self.battery_level = battery_level
        self.is_on = False

    def power_on(self) -> str:
        """
        Включает смартфон, если есть заряд батареи.

        Returns:
            str: Сообщение о состоянии

        Examples:
            >>> phone = Smartphone("Apple", "iPhone 13")
            >>> phone.power_on()
            'iPhone 13 включен'

            >>> phone = Smartphone("Samsung", "Galaxy", 0)
            >>> phone.power_on()
            'Недостаточно заряда для включения'
        """
        if self.battery_level > 0:
            self.is_on = True
            return f"{self.model} включен"
        return "Недостаточно заряда для включения"

    def charge(self, minutes: int = 30) -> int:
        """
        Заряжает смартфон (1 минута = 1% заряда).

        Args:
            minutes: Время зарядки в минутах (по умолчанию 30)

        Returns:
            int: Новый уровень заряда

        Raises:
            ValueError: Если minutes <= 0

        Examples:
            >>> phone = Smartphone("Xiaomi", "Redmi", 20)
            >>> phone.charge(15)
            35
            >>> phone.charge()
            65
        """
        if minutes <= 0:
            raise ValueError("Время зарядки должно быть положительным")

        self.battery_level = min(100, self.battery_level + minutes)
        return self.battery_level

    def use_app(self, app_name: str, battery_usage: int = 5) -> str:
        """
        Использует приложение, расходуя заряд батареи.

        Args:
            app_name: Название приложения
            battery_usage: Расход батареи в % (по умолчанию 5)

        Returns:
            str: Сообщение о результате

        Raises:
            ValueError: Если battery_usage <= 0 или > 20
            RuntimeError: Если смартфон выключен или недостаточно заряда

        Examples:
            >>> phone = Smartphone("Apple", "iPhone", 50)
            >>> phone.power_on()
            'iPhone включен'
            >>> phone.use_app("Safari", 10)
            'Приложение Safari использовано, осталось 40% заряда'
        """
        if not self.is_on:
            raise RuntimeError("Смартфон выключен")
        if battery_usage <= 0 or battery_usage > 20:
            raise ValueError("Расход батареи должен быть от 1 до 20%")
        if self.battery_level < battery_usage:
            raise RuntimeError("Недостаточно заряда для использования приложения")

        self.battery_level -= battery_usage
        return f"Приложение {app_name} использовано, осталось {self.battery_level}% заряда"