import datetime

import pytest

from freshsales.v2.models import Contact, Field, View


@pytest.fixture
def contact(api):
    return api.contacts.view_contact(31016358306)


def test_create_contact(api):
    contact_data = {
        "first_name": "Jane",
        "last_name": "Sampleton",
        "emails": "janesampleton@gmail.com"
    }

    contact = api.contacts.create_contact(**contact_data)
    assert isinstance(contact, Contact)
    assert contact.first_name == contact_data["first_name"]
    assert contact.last_name == contact_data["last_name"]
    assert contact.emails[0]['value'] == contact_data["emails"]


def test_view_contact(contact):
    assert isinstance(contact, Contact)
    assert contact.first_name == "Jane"
    assert contact.last_name == "Sampleton"
    assert contact.emails[0]['value'] == "janesampleton@gmail.com"
    assert contact.id == 31016358306


def test_list_views(api):
    views = api.contacts.list_views()
    assert isinstance(views, list)
    assert len(views) > 0
    assert isinstance(views[0], View)
    assert views[3].name == "All Contacts"


def test_list_contacts(api):
    contacts = api.contacts.list_contacts(view_id=31003548176,
                                          sort="open_deals_amount",      sort_type="desc",
                                          page=1,
                                          per_page=20)
    assert isinstance(contacts, list)
    assert isinstance(contacts[0], Contact)
    assert len(contacts) > 0
    assert contacts[0].first_name == "Jane"
    assert contacts[1].first_name == "Spector"
    assert contacts[2].first_name == "Laura"
    assert contacts[3].first_name == "Jay"


def test_update_contact(api):
    contact = api.contacts.update_contact(
        31016358306, first_name="New", last_name="Name", display_name="New Name")
    assert isinstance(contact, Contact)
    assert contact.display_name == "New Name"


def test_clone_contact(api):

    contact = api.contacts.clone_contact(
        31016358306, first_name="New", last_name="Name", display_name="New Name")
    assert isinstance(contact, Contact)
    assert contact.first_name == "New"
    assert contact.last_name == "Name"
    assert contact.display_name == "New Name"


def test_upsert_contact(api):
    contact_data = {
        "first_name": "Jane",
        "last_name": "Sampleton",
        "display_name": "Jane Sampleton"
    }
    unique_identifier = ('email', 'janesampleton@gmail.com')
    contact = api.contacts.upsert_contact(unique_identifier, **contact_data)

    assert isinstance(contact, Contact)
    assert contact.first_name == "Jane"
    assert contact.last_name == "Sampleton"
    assert contact.display_name == "Jane Sampleton"


def test_delete_contact(api):
    assert api.contacts.delete_contact(31016358306) is True


def test_forget_contact(api):
    assert api.contacts.forget_contact(31016358306) is True


def test_list_fields(api):
    fields = api.contacts.list_fields()
    assert isinstance(fields, list)
    assert isinstance(fields[0], Field)
    assert len(fields) > 0
    assert fields[0].label == "First name"


def test_contact_datetime(contact):
    assert isinstance(contact.created_at, datetime.datetime)
    assert isinstance(contact.updated_at, datetime.datetime)


def test_contact_str(contact):
    assert str(contact) == "Jane Sampleton"


def test_contact_repr(contact):
    assert repr(contact) == "<Contact 'Jane Sampleton' #31016358306>"
