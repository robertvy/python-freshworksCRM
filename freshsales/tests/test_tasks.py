import datetime

import pytest

from freshsales.models import (
    Task,
    Contact,
    User,
    Account,
    Deal,
)


@pytest.fixture
def task(api):
    return api.tasks.view_task(31001308220).get('task')


def test_create_task(api):
    task = api.tasks.create_task(title='Sample Task',
                                 description='This is just a sample task.',
                                 due_date='Tue Jun 21 2099 11:00:00 GMT+0000',
                                 owner_id=31000148397,
                                 targetable_id=31016358306,
                                 targetable_type='Contact')
    assert isinstance(task, Task)
    assert task.title == "Sample Task"
    assert task.description == "This is just a sample task."
    assert isinstance(task.due_date, datetime.datetime)


def test_view_task(api):
    response = api.tasks.view_task(31001308220)
    contacts = response.get('contacts')
    users = response.get('users')
    task = response.get('task')

    assert isinstance(task, Task)
    assert task.title == "Sample Task"
    assert task.description == "This is just a sample task."
    assert isinstance(task.due_date, datetime.datetime)

    if contacts:
        assert isinstance(contacts, list)
        assert isinstance(contacts[0], Contact)

    if users:
        assert isinstance(users, list)
        assert isinstance(users[0], User)


def test_list_all_tasks(api):
    response = api.tasks.list_all_tasks("open")
    contacts = response.get('contacts')
    users = response.get('users')
    tasks = response.get('tasks')
    accounts = response.get('accounts')
    deals = response.get('deals')

    if tasks:
        task = tasks[1]
        assert isinstance(task, Task)
        assert task.title == "Weekly follow up (sample)"
        assert isinstance(task.due_date, datetime.datetime)

    if contacts:
        assert isinstance(contacts, list)
        assert isinstance(contacts[0], Contact)

    if users:
        assert isinstance(users, list)
        assert isinstance(users[0], User)

    if accounts:
        assert isinstance(accounts, list)
        assert isinstance(accounts[0], Account)

    if deals:
        assert isinstance(deals, list)
        assert isinstance(deals[0], Deal)


def test_update_task(api):
    task = api.tasks.update_task(31001308220, title='Updated Task')
    assert isinstance(task, Task)
    assert task.title == "Updated Task"
    assert task.description == "This is just a sample task."
    assert isinstance(task.due_date, datetime.datetime)


def test_mark_as_done(api):
    task = api.tasks.mark_as_done(31001308220)
    assert isinstance(task, Task)
    assert task.title == "Updated Task"
    assert task.status == 1


def test_delete_task(api):
    assert api.tasks.delete_task(31001308220) is True


def test_task_datetime(task):
    assert isinstance(task.created_at, datetime.datetime)
    assert isinstance(task.updated_at, datetime.datetime)


def test_task_str(task):
    assert str(
        task) == "Sample Task"


def test_task_repr(task):
    assert repr(
        task) == "<Task 'Sample Task' #31001308220>"
