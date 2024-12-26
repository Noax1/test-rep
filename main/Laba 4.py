from typing import List

# Интерфейс стратегии
class SortingStrategy:
    def sort(self, data: List[int]) -> List[int]:
        pass

# Конкретная стратегия: Сортировка пузырьком
class BubbleSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        print("Sorting using Bubble Sort")
        return data

# Конкретная стратегия: Быстрая сортировка
class QuickSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        pivot = data[0]
        less = [x for x in data[1:] if x <= pivot]
        greater = [x for x in data[1:] if x > pivot]
        print("Sorting using Quick Sort")
        return self.sort(less) + [pivot] + self.sort(greater)

# Контекст
class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy

    def sort(self, data: List[int]) -> List[int]:
        return self.strategy.sort(data)

# Пример использования
data = [5, 3, 8, 4, 2]
sorter = Sorter(BubbleSortStrategy())
print(sorter.sort(data))

sorter.set_strategy(QuickSortStrategy())
print(sorter.sort(data))


# Интерфейс обработчика
class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None

# Конкретный обработчик A
class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            return "ConcreteHandlerA handled request A"
        return super().handle(request)

# Конкретный обработчик B
class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            return "ConcreteHandlerB handled request B"
        return super().handle(request)

# Пример использования
handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB()

handler_a.set_next(handler_b)

print(handler_a.handle("A"))
print(handler_a.handle("B"))


# Интерфейс итератора
class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.collection)

    def next(self):
        if not self.has_next():
            raise StopIteration("No more elements")
        result = self.collection[self.index]
        self.index += 1
        return result

# Пример использования
items = [1, 2, 3, 4, 5]
iterator = Iterator(items)

while iterator.has_next():
    print(iterator.next())
