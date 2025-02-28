class Todo:
    IS_DONE = 'X'
    IS_UNDONE = ' '


    def __init__(self, title):
        self._title = title
        self._done = False

    @property
    def title(self):
        return self._title

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, boolean):
        if not isinstance(boolean, bool):
            raise TypeError('\'done\' value must be True or False')

        self._done = boolean

    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented

        return self.title == other.title and self.done == other.done

    def __str__(self):
        marker = Todo.IS_DONE if self.done else Todo.IS_UNDONE
        return f'[{marker}] {self.title}'


class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title

    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError('Can only add Todo objects to TodoList')

        self._todos.append(todo)

    def remove_at(self, idx):
        self._todos.pop(idx)

    def mark_done(self, title):
        target = self.find_by_title(title)

        target.done = True

    def mark_done_at(self, idx):
        self.todo_at(idx).done = True

    def mark_undone_at(self, idx):
        self.todo_at(idx).done = False

    def mark_all_done(self):
        self.each(lambda todo: setattr(todo, 'done', True))

    def mark_all_undone(self):
        self.each(lambda todo: setattr(todo, 'done', False))

    def all_done(self):
        return all(todo.done for todo in self._todos)

    def first(self):
        return self._todos[0]

    def last(self):
        return self._todos[-1]

    def todo_at(self, idx):
        return self._todos[idx]

    def to_list(self):
        return self._todos.copy()

    def find_by_title(self, title):
        target = self.select(lambda todo: todo.title == title)

        return target.todo_at(0)

    def done_todos(self):
        return self.select(lambda todo: todo.done)

    def undone_todos(self):
        return self.select(lambda todo: not todo.done)

    def select(self, callback):
        new_todo = TodoList(self.title)

        def choose(todo):
            if callback(todo):
                new_todo.add(todo)

        self.each(choose)

        return new_todo

    def each(self, callback):
        for todo in self._todos:
            callback(todo)

    def __len__(self):
        return len(self._todos)

    def __str__(self):
        return (f'----- {self.title} -----\n' +
                '\n'.join(str(item) for item in self._todos))


empty_todo_list = TodoList('Nothing Doing')

def setup():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list

