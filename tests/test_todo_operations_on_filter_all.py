def test_add_first_todo(desctop_todomvc):
    desctop_todomvc.open()

    desctop_todomvc.should_be_empty()

    desctop_todomvc.add('a')

    desctop_todomvc.should_be('a')
    desctop_todomvc.should_be_items_left(1)


def test_add_todos(desctop_todomvc):
    desctop_todomvc.open()

    desctop_todomvc.should_be_empty()

    desctop_todomvc.add('a', 'b', 'c')

    desctop_todomvc.should_be('a', 'b', 'c')
    desctop_todomvc.should_be_items_left(3)


def test_edit(desctop_todomvc):
    desctop_todomvc.given_opened('a', 'b', 'c')

    desctop_todomvc.edit('a', 'a edited')

    desctop_todomvc.should_be('a edited', 'b', 'c')
    desctop_todomvc.should_be_items_left(3)


def test_edit_by_focus_change(desctop_todomvc):
    desctop_todomvc.given_opened('a', 'b', 'c')

    desctop_todomvc.edit_by_focus_change('b', 'b edited')

    desctop_todomvc.should_be('a', 'b edited', 'c')
    desctop_todomvc.should_be_items_left(3)


def test_cancel_edit(desctop_todomvc):
    desctop_todomvc.given_opened('a', 'b', 'c')

    desctop_todomvc.cancel_edit('c', 'to be canceled')

    desctop_todomvc.should_be('a', 'b', 'c')
    desctop_todomvc.should_be_items_left(3)


def test_complete(desctop_todomvc):
    desctop_todomvc.given_opened('a', 'b', 'c')

    desctop_todomvc.toggle('a')

    desctop_todomvc.should_be_completed('a')
    desctop_todomvc.should_be_active('b', 'c')
    desctop_todomvc.should_be_items_left(2)


def test_activate(desctop_todomvc):
    desctop_todomvc.given_opened('a', 'b', 'c')
    desctop_todomvc.toggle('b')

    desctop_todomvc.toggle('b')

    desctop_todomvc.should_be_active('a', 'b', 'c')
    desctop_todomvc.should_be_completed()
    desctop_todomvc.should_be_items_left(3)


def test_complete_all(desctop_todomvc):
    desctop_todomvc.given_opened('a', 'b', 'c')

    desctop_todomvc.toggle_all()

    desctop_todomvc.should_be_completed('a', 'b', 'c')
    desctop_todomvc.should_be_active()
    desctop_todomvc.should_be_items_left(0)


def test_activate_all(desctop_todomvc):
    desctop_todomvc.given_opened('a', 'b', 'c')
    desctop_todomvc.toggle_all()

    desctop_todomvc.toggle_all()

    desctop_todomvc.should_be_active('a', 'b', 'c')
    desctop_todomvc.should_be_completed()
    desctop_todomvc.should_be_items_left(3)


def test_clear_completed(desctop_todomvc):
    desctop_todomvc.given_opened('a', 'b', 'c', 'd', 'e')
    desctop_todomvc.toggle('d')
    desctop_todomvc.toggle('e')

    desctop_todomvc.clear_completed()

    desctop_todomvc.should_be('a', 'b', 'c')
    desctop_todomvc.should_be_items_left(3)


def test_delete(desctop_todomvc):
    desctop_todomvc.given_opened('a', 'b', 'c')

    desctop_todomvc.delete('a')

    desctop_todomvc.should_be('b', 'c')
    desctop_todomvc.should_be_items_left(2)


def test_delete_last_todo(desctop_todomvc):
    desctop_todomvc.given_opened('a')

    desctop_todomvc.delete('a')

    desctop_todomvc.should_be_empty()


