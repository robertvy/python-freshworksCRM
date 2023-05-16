from freshsales.v2.models import (
    List,
    Contact,
)


def test_create_list(api):
    mlist = api.lists.create_list("Brand Lovers")
    assert isinstance(mlist, List)
    assert mlist.name == "Brand Lovers"
    assert mlist.id > 0


def test_fetch_all_lists(api):
    mlists = api.lists.fetch_all_lists()
    assert isinstance(mlists, list)
    assert len(mlists) > 0
    assert isinstance(mlists[0], List)
    assert mlists[0].name == "Sample list"
    assert mlists[1].id == 31000044990
    assert mlists[3].name == "Brand Lovers"


def test_update_list(api):
    mlist = api.lists.update_list(31000045356, 'Fans')
    assert isinstance(mlist, List)
    assert mlist.name == "Fans"
    assert mlist.id > 0


def test_add_contacts_to_list(api):
    ids = [31000045356, 31000045357]
    message = api.lists.add_contacts_to_list(31000045356,
                                             ids)
    assert message == f"{len(ids)} contacts updated." if len(
        ids) > 1 else f"{len(ids)} contact updated."


def test_fetch_contacts_from_list(api):
    contacts = api.lists.fetch_contacts_from_list(31000045356)
    assert isinstance(contacts, list)
    assert len(contacts) > 0
    assert isinstance(contacts[0], Contact)
    assert contacts[0].id == 31016358307
    assert contacts[1].first_name == "Jane"


def test_remove_contacts_from_list(api):
    ids = [31016358306, 31016358307]
    message = api.lists.remove_contacts_from_list(31000045351,
                                                  ids)
    assert message == f"{len(ids)} contacts updated." if len(
        ids) > 1 else f"{len(ids)} contact updated."

    # Note: remove all paramter tested on live API


def test_move_contacts_between_lists(api):
    ids = [31016358306, 31016358307]
    message = api.lists.move_contacts_between_lists(list_id=31000045351,
                                                    ids=ids,
                                                    from_list_id=31000045356)
    assert message == f"{len(ids)} contacts updated." if len(
        ids) > 1 else f"{len(ids)} contact updated."


def test_deal_str(api):
    lists = api.lists.fetch_all_lists()
    assert str(
        lists[0]) == "Sample list"


def test_deal_repr(api):
    lists = api.lists.fetch_all_lists()
    assert repr(
        lists[0]) == "<List 'Sample list' #31000036946>"
