import pytest

from freshsales.models import (
    Contact,
)


@pytest.fixture
def contact(api):
    return api.contacts.view_contact(31016358306)


def test_filter_contacts(api):
    filter_data = [
        {'attribute': 'name', 'operator': 'equals', 'value': 'John'}
    ]

    contacts = api.search.filter_contacts(filter_data)
    print(contacts)
    assert isinstance(contacts, list)
    assert isinstance(contacts[0], Contact)
    assert len(contacts) > 0


