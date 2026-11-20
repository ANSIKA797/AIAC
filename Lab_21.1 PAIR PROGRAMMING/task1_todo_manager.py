"""Task 1: AI-Assisted Pair Programming — Enhanced To-Do List Manager."""


class TodoManager:
    def __init__(self):
        self.tasks: list[dict] = []

    def add_task(self, title: str, priority: str = "medium") -> None:
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        self.tasks.append({"title": title.strip(), "priority": priority, "done": False})

    def complete_task(self, index: int) -> None:
        if not (0 <= index < len(self.tasks)):
            raise IndexError("Invalid task index")
        self.tasks[index]["done"] = True

    def summary(self) -> list[str]:
        return [f"[{'x' if t['done'] else ' '}] ({t['priority']}) {t['title']}" for t in self.tasks]


if __name__ == "__main__":
    tm = TodoManager()
    tm.add_task("Finish Lab 21", "high")
    tm.add_task("Push to Git", "medium")
    tm.complete_task(0)
    for line in tm.summary():
        print(line)
