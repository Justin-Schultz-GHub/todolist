import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_length(self):
        self.assertEqual(3, len(self.todos))

    def test_to_list(self):
        self.assertEqual([self.todo1, self.todo2, self.todo3],
                        self.todos.to_list())

    def test_first(self):
        self.assertEqual(self.todo1, self.todos.first())

    def test_last(self):
        self.assertEqual(self.todo3, self.todos.last())

    def test_all_done(self):
        self.assertFalse(self.todos.all_done())

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todos.add(1)

        with self.assertRaises(TypeError):
            self.todos.add('1')

    def test_todo_at(self):
        with self.assertRaises(IndexError):
            self.todos.todo_at(len(self.todos) + 1)

    def test_mark_undone_at(self):
        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(len(self.todos) + 1)

        self.todo1.done = True
        self.todo2.done = True
        self.todo3.done = True

        self.assertTrue(self.todo1.done)
        self.assertTrue(self.todo2.done)
        self.assertTrue(self.todo3.done)

        self.assertFalse(self.todos.mark_undone_at(0))
        self.assertFalse(self.todos.mark_undone_at(1))
        self.assertFalse(self.todos.mark_undone_at(2))

    def test_mark_all_done(self):
        self.todo1.done = False
        self.todo2.done = False
        self.todo3.done = False

        self.todos.mark_all_done()

        self.assertTrue(self.todo1.done)
        self.assertTrue(self.todo2.done)
        self.assertTrue(self.todo3.done)
        self.assertTrue(self.todos.all_done())

    def test_remove_at(self):
        with self.assertRaises(IndexError):
            self.todos.remove_at(len(self.todos) + 1)

        self.todos.remove_at(2)
        self.assertEquals([self.todo1, self.todo2], self.todos.to_list())

    def test_str(self):
        todos_str = (
                    '----- Today\'s Todos -----\n'
                    '[ ] Buy milk\n'
                    '[ ] Clean room\n'
                    '[ ] Go to the gym'
                    )

        self.assertEqual(todos_str, str(self.todos))


    # def (self):
    #     self.assertEqual()

    # def (self):
    #     self.assertEqual()

    # def (self):
    #     self.assertEqual()

    # def (self):
    #     self.assertEqual()


if __name__ == "__main__":
    unittest.main()