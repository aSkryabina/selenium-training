import pytest

def test_new_product(app):

    for i in range(3):
        app.add_items()

    count = app.get_trash_count()

    for i in range(count):
        app.delete_items(count)