class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги."""
        return self._author

    def __str__(self) -> str:
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """Класс бумажной книги."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц."""
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        """Устанавливает количество страниц с проверкой."""
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook(Book):
    """Класс аудиокниги."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        """Устанавливает продолжительность с проверкой."""
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной")
        self._duration = float(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"


if __name__ == "__main__":
    # Проверка базового класса
    book = Book("1984", "Джордж Оруэлл")
    print(book)
    print(repr(book))

    # Проверка бумажной книги
    paper_book = PaperBook("Война и мир", "Лев Толстой", 1225)
    print(paper_book)
    print(repr(paper_book))

    # Проверка аудиокниги
    audio_book = AudioBook("Преступление и наказание", "Фёдор Достоевский", 15.5)
    print(audio_book)
    print(repr(audio_book))

    # Проверка свойств
    try:
        paper_book.pages = -100  # Должно вызвать ValueError
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        audio_book.duration = "текст"  # Должно вызвать TypeError
    except TypeError as e:
        print(f"Ошибка: {e}")