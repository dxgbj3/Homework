import tkinter as tk
from tkinter import messagebox


class TaskManager:
    def __init__(self):
        self.__tasks = []

    def add_task(self, title, description):
        self.__tasks.append({"title": title, "description": description, "done": False})

    def remove_task(self, title):
        for task in self.__tasks:
            if task["title"] == title:
                self.__tasks.remove(task)
                return True
        return False

    def mark_as_done(self, title):
        for task in self.__tasks:
            if task["title"] == title:
                task["done"] = True
                return True
        return False

    def get_tasks(self):
        return self.__tasks


class TaskApp:
    def __init__(self, root):
        self.manager = TaskManager()
        self.root = root
        self.root.title("Task Manager")

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.title_label = tk.Label(self.frame, text="Название:")
        self.title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(self.frame)
        self.title_entry.grid(row=0, column=1)

        self.desc_label = tk.Label(self.frame, text="Описание:")
        self.desc_label.grid(row=1, column=0)
        self.desc_entry = tk.Entry(self.frame)
        self.desc_entry.grid(row=1, column=1)

        self.add_button = tk.Button(self.frame, text="Добавить", command=self.add_task)
        self.add_button.grid(row=2, columnspan=2, pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack()

        self.done_button = tk.Button(root, text="Отметить выполненной", command=self.mark_done)
        self.done_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Удалить", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.show_desc_button = tk.Button(root, text="Показать описание", command=self.show_description)
        self.show_desc_button.pack(pady=5)

    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()
        if title:
            self.manager.add_task(title, description)
            self.update_task_list()
            self.title_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Ошибка", "Название задачи не может быть пустым!")

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            title = self.task_listbox.get(selected[0]).split(" - ")[0]
            if self.manager.remove_task(title):
                self.update_task_list()
        else:
            messagebox.showwarning("Ошибка", "Выберите задачу для удаления!")

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            title = self.task_listbox.get(selected[0]).split(" - ")[0]
            if self.manager.mark_as_done(title):
                self.update_task_list()
        else:
            messagebox.showwarning("Ошибка", "Выберите задачу для отметки как выполненную!")

    def show_description(self):
        selected = self.task_listbox.curselection()
        if selected:
            title = self.task_listbox.get(selected[0]).split(" - ")[0]
            for task in self.manager.get_tasks():
                if task["title"] == title:
                    messagebox.showinfo("Описание", f"Описание задачи:\n{task['description']}")
                    return
        else:
            messagebox.showwarning("Ошибка", "Выберите задачу для просмотра описания!")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.manager.get_tasks():
            status = "[Выполнено]" if task["done"] else "[Не выполнено]"
            self.task_listbox.insert(tk.END, f'{task["title"]} - {status}')


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
