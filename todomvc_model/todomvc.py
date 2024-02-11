from playwright.sync_api import sync_playwright, Playwright


class TodoMVC:
    def __init__(self,playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()


    def open(self):
        self.page.goto('https://todomvc.com/examples/emberjs/todomvc/dist/')
        self.page.wait_for_selector('.new-todo')
        return self

    def add(self, *todos):
        for todo in todos:
            self.page.type('.new-todo', todo)
            self.page.press('.new-todo', 'Enter')
        return self

    def given_opened(self, *todos: str):
        self.open()
        self.add(*todos)

    def should_be(self, *todos):
        todo_texts = self.page.eval_on_selector_all('.todo-list>li', '(todos) => todos.map(todo => todo.textContent)')
        assert [todo.strip() for todo in todo_texts] == list(todos), f'Expected todos: {todos}, but got: {todo_texts}'
        return self

    def start_editing(self, todo, new_text):
        self.page.dblclick(f'//label[text()="{todo}"]')
        self.page.wait_for_selector(f'.todo-list>li.editing .edit').fill(new_text)
        return self

    def edit(self, todo, new_text):
        self.start_editing(todo, new_text)
        self.page.press(f'.todo-list>li.editing .edit', 'Enter')
        return self

    def toggle(self, todo):
        self.page.click(f'//label[text()="{todo}"]/preceding-sibling::input')
        return self

    def toggle_all(self):
        self.page.click('#toggle-all')
        return self

    def clear_completed(self):
        self.page.click('.clear-completed')
        return self

    def delete(self, todo):
        self.page.hover(f'//label[text()="{todo}"]/following-sibling::button')
        self.page.click(f'//label[text()="{todo}"]/following-sibling::button')
        return self

    def cancel_edit(self, todo, new_text):
        self.start_editing(todo, new_text)
        self.page.press(f'.todo-list>li.editing .edit', 'Escape')

    def should_be_completed(self, *todos):
        completed_todos = self.page.query_selector_all('.todo-list>li.completed')
        completed_texts = [todo.text_content() for todo in completed_todos]
        assert [todo.strip() for todo in completed_texts] == list(todos), f'Expected completed todos: {todos}, but got: {completed_texts}'
        return self

    def should_be_active(self, *todos):
        active_todos = self.page.query_selector_all('.todo-list>li:not(.completed)')
        active_texts = [todo.text_content() for todo in active_todos]
        assert [todo.strip() for todo in active_texts] == list(todos), f'Expected active todos: {todos}, but got: {active_texts}'
        return self

    def should_be_empty(self):
        todos = self.page.query_selector_all('.todo-list>li')
        assert len(todos) == 0, f'Expected an empty todo list, but found {len(todos)} todos'
        return self

    def edit_by_focus_change(self, todo, new_text):
        self.start_editing(todo, new_text)
        self.page.press(f'.todo-list>li.editing .edit', 'Tab')
        return self

    def should_be_items_left(self, count):
        items_left_text = self.page.text_content('.todo-count>strong')
        assert int(items_left_text) == count, f'Expected items left: {count}, but got: {items_left_text}'
        return self

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
