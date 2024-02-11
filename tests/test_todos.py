from playwright.sync_api import sync_playwright


def test_common_todo_functionality():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto('https://todomvc.com/examples/emberjs/todomvc/dist/')
        page.wait_for_selector('.new-todo')
        page.type('.new-todo', 'a')
        page.press('.new-todo', 'Enter')
        page.type('.new-todo', 'b')
        page.press('.new-todo', 'Enter')
        page.type('.new-todo', 'c')
        page.press('.new-todo', 'Enter')
        todo_texts = page.eval_on_selector_all('.todo-list>li', '(todos) => todos.map(todo => todo.textContent)')
        assert [todo.strip() for todo in todo_texts] == ['a', 'b', 'c'], f"Expected todos: ['a', 'b', 'c'], but got: {todo_texts}"
        page.dblclick(f'//label[text()="c"]')
        page.wait_for_selector(f'.todo-list>li.editing .edit').fill('c edited')
        page.press(f'.todo-list>li.editing .edit', 'Enter')

        page.click(f'//label[text()="c edited"]/preceding-sibling::input')
        page.click('.clear-completed')
        todo_texts = page.eval_on_selector_all('.todo-list>li', '(todos) => todos.map(todo => todo.textContent)')
        assert [todo.strip() for todo in todo_texts] == ['a', 'b'], f"Expected todos: ['a', 'b'], but got: {todo_texts}"


        page.dblclick(f'//label[text()="b"]')
        page.wait_for_selector(f'.todo-list>li.editing .edit').fill('to be canceled')
        page.press(f'.todo-list>li.editing .edit', 'Escape')


        page.hover(f'//label[text()="b"]/following-sibling::button')
        page.click(f'//label[text()="b"]/following-sibling::button')
        todo_texts = page.eval_on_selector_all('.todo-list>li', '(todos) => todos.map(todo => todo.textContent)')
        assert [todo.strip() for todo in todo_texts] == ['a'], f"Expected todos: ['a'], but got: {todo_texts}"

        # Закриття браузера
        browser.close()
