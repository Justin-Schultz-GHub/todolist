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
