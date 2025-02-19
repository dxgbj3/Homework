class TaskManager:
    def __init__(self):
        self.__tasks = []  # Приватный список задач

    def add_task(self, title, description):
        self.__tasks.append({"title": title, "description": description, "done": False})
        print(f'Задача "{title}" добавлена.')

    def remove_task(self, title):
        for task in self.__tasks:
            if task["title"] == title:
                self.__tasks.remove(task)
                print(f'Задача "{title}" удалена.')
                return
        print(f'Задача "{title}" не найдена.')

    def mark_as_done(self, title):
        for task in self.__tasks:
            if task["title"] == title:
                task["done"] = True
                print(f'Задача "{title}" отмечена как выполненная.')
                return
        print(f'Задача "{title}" не найдена.')

    def show_tasks(self):
        if not self.__tasks:
            print("Список задач пуст.")
            return

        for task in self.__tasks:
            status = "[Выполнено]" if task["done"] else "[Не выполнено]"
            print(f'{status} {task["title"]}: {task["description"]}')


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Купить продукты", "Купить хлеб, молоко и яйца")
    manager.add_task("Сделать ДЗ", "Закончить задание по математике")
    manager.show_tasks()
    manager.mark_as_done("Купить продукты")
    manager.show_tasks()
    manager.remove_task("Сделать ДЗ")
    manager.show_tasks()
