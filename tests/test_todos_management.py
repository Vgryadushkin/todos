def test_common_todo_functionality(desctop_todomvc):
    desctop_todomvc.open()
    desctop_todomvc.page.pause()
    desctop_todomvc.add('a', 'b', 'c')
    desctop_todomvc.should_be('a', 'b', 'c')

    desctop_todomvc.edit('c', 'c edited')

    desctop_todomvc.toggle('c edited')

    desctop_todomvc.clear_completed()
    desctop_todomvc.should_be('a', 'b')

    desctop_todomvc.cancel_edit('b', 'to be canceled')

    desctop_todomvc.delete('b')
    desctop_todomvc.should_be('a')