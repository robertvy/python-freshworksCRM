import datetime

import pytest

from freshsales.v2.models import (
    Account,
    View,
    Field,
)


@pytest.fixture
def account(api):
    return api.accounts.view_account(31003638276)


def test_create_account(api):
    account_data = {
        "name": "Acme Inc",
        "city": "Toronto",
        "phone": "19266343001"
    }

    custom_fields = {
        "cf_is_vip": True,
    }

    account = api.accounts.create_account(
        **account_data, custom_field=custom_fields)
    assert isinstance(account, Account)
    assert account.name == account_data["name"]
    assert account.city == account_data["city"]
    assert account.phone == account_data["phone"]
    assert account.cf_is_vip == custom_fields["cf_is_vip"]


def test_view_account(account):
    assert isinstance(account, Account)
    assert account.name == "Acme Inc"
    assert account.city == "Toronto"
    assert account.phone == "19266343001"
    assert account.cf_is_vip is True


def test_list_views(api):
    views = api.accounts.list_views()
    assert isinstance(views, list)
    assert len(views) > 0
    assert isinstance(views[0], View)
    assert views[1].name == "All Accounts"


def test_list_accounts(api):
    accounts = api.accounts.list_accounts(view_id=31003548200,
                                          sort="open_deals_amount",      sort_type="desc",
                                          page=1,
                                          per_page=20)
    assert isinstance(accounts, list)
    assert isinstance(accounts[0], Account)
    assert len(accounts) > 0
    assert accounts[0].name == "Widgetz.io"
    assert accounts[1].name == "Techcave"
    assert accounts[2].name == "Acme Inc"
    assert accounts[3].name == "E Corp"


def test_update_account(api):
    account = api.accounts.update_account(31003638276, name="New Name")
    assert isinstance(account, Account)
    assert account.name == "New Name"


def test_clone_account(api):
    account = api.accounts.clone_account(31003638276, name="Acme Inc")
    assert isinstance(account, Account)
    assert account.name == "Acme Inc"
    assert account.city == "Toronto"
    assert account.phone == "19266343001"
    assert account.cf_is_vip is True


def test_upsert_account(api):
    account_data = {
        "name": "Acme Inc",
        "city": "Toronto",
        "phone": "19266343001"
    }
    unique_identifier = ('name', 'New Name')
    account = api.accounts.upsert_account(unique_identifier, **account_data)
    assert isinstance(account, Account)
    assert account.name == account_data["name"]
    assert account.city == account_data["city"]
    assert account.phone == account_data["phone"]
    assert account.cf_is_vip is True


def test_delete_account(api):
    assert api.accounts.delete_account(31003638276) is True


def test_forget_account(api):
    assert api.accounts.forget_account(31003638276) is True


def test_list_fields(api):
    fields = api.accounts.list_fields()
    assert isinstance(fields, list)
    assert isinstance(fields[0], Field)
    assert len(fields) > 0
    assert fields[0].label == "Name"


def test_account_datetime(account):
    assert isinstance(account.created_at, datetime.datetime)
    assert isinstance(account.updated_at, datetime.datetime)


def test_account_str(account):
    assert str(account) == "Acme Inc"


def test_account_repr(account):
    assert repr(account) == "<Account 'Acme Inc' #31003638276>"
