import datetime

import pytest

from freshsales.v2.models import Note


@pytest.fixture
def note(api):
    return api.notes.view_note(31003638276)


def test_create_note(api):
    note = api.notes.create_note(description='Sample note for contact create',
                                 targetable_type='Contact',
                                 targetable_id=31016358306)
    assert isinstance(note, Note)
    assert note.description == 'Sample note for contact create'
    assert note.targetables[0].get('type') == 'Contact'
    assert note.targetables[0].get('id') == 31016358306


def test_update_note(api):
    note = api.notes.update_note(
        31003638276, description='Updated note for contact create')
    assert isinstance(note, Note)
    assert note.description == 'Updated note for contact create'
    assert note.targetables[0].get('type') == 'Contact'
    assert note.targetables[0].get('id') == 31016358306


def test_delete_note(api):
    assert api.notes.delete_note(31003638276) is True


def test_note_datetime(api):
    note = api.notes.update_note(
        31003638276, description='Updated note for contact create')
    assert isinstance(note.created_at, datetime.datetime)
    assert isinstance(note.updated_at, datetime.datetime)


def test_note_str(api):
    note = api.notes.update_note(
        31003638276, description='Updated note for contact create')
    assert str(
        note) == "Updated note for contact create"


def test_note_repr(api):
    note = api.notes.update_note(
        31003638276, description='Updated note for contact create')
    assert repr(
        note) == "<Note 'Updated note for contact create' #31004348670>"
