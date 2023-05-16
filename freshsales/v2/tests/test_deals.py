import datetime

import pytest

from freshsales.v2.models import (
    Deal,
    View,
    Field,
)


@pytest.fixture
def deal(api):
    return api.deals.view_deal(31003638276)


def test_create_deal(api):
    deal = api.deals.create_deal(name='Widgetz.io // Gold plan // 70 users // New business',
                                 amount=5600.0,
                                 tags=["Sample Deal"])
    assert isinstance(deal, Deal)
    assert deal.name == "Widgetz.io // Gold plan // 70 users // New business"
    assert float(deal.amount) == 5600.0
    assert deal.tags == ["Sample Deal"]


def test_view_deal(deal):
    assert isinstance(deal, Deal)
    assert deal.name == "Widgetz.io // Gold plan // 70 users // New business"
    assert float(deal.amount) == 5600.0
    assert deal.tags == ["Sample Deal"]


def test_list_views(api):
    views = api.deals.list_views()
    assert isinstance(views, list)
    assert len(views) > 0
    assert isinstance(views[0], View)
    assert views[0].name == "Open Deals"


def test_list_deals(api):
    deals = api.deals.list_deals(view_id=31003548200,
                                 sort="open_deals_amount",      sort_type="desc",
                                 page=1,
                                 per_page=20)
    assert isinstance(deals, list)
    assert isinstance(deals[0], Deal)
    assert len(deals) > 0
    assert deals[0].id == 31001944158
    assert deals[1].probability == 100
    assert deals[2].name == "Acme Inc // Annual Maint. (sample)"


def test_update_deal(api):
    deal = api.deals.update_deal(31001944156, name="New Name")
    assert isinstance(deal, Deal)
    assert deal.name == "New Name"


def test_clone_deal(api):
    deal = api.deals.clone_deal(
        31001944158, name="Widgetz.io // Gold plan // 70 users // New business")
    assert isinstance(deal, Deal)
    assert deal.name == "Widgetz.io // Gold plan // 70 users // New business"
    assert float(deal.amount) == 5600.0
    assert deal.tags == ["Sample Deal"]


def test_upsert_deal(api):
    deal_data = {
        "amount": 5600.0,
        "tags": ["Sample Deal"]
    }
    unique_identifier = (
        'name', 'Widgetz.io // Gold plan // 70 users // New business')
    deal = api.deals.upsert_deal(unique_identifier, **deal_data)
    assert isinstance(deal, Deal)
    assert deal.name == "Widgetz.io // Gold plan // 70 users // New business"
    assert float(deal.amount) == deal_data["amount"]
    assert deal.tags == deal_data["tags"]


def test_delete_deal(api):
    assert api.deals.delete_deal(31003638276) is True


def test_forget_deal(api):
    assert api.deals.forget_deal(31003638276) is True


def test_list_fields(api):
    fields = api.deals.list_fields()
    assert isinstance(fields, list)
    assert isinstance(fields[0], Field)
    assert len(fields) > 0
    assert fields[0].label == "Name"


def test_deal_datetime(deal):
    assert isinstance(deal.created_at, datetime.datetime)
    assert isinstance(deal.updated_at, datetime.datetime)


def test_deal_str(deal):
    assert str(
        deal) == "Widgetz.io // Gold plan // 70 users // New business"


def test_deal_repr(deal):
    assert repr(
        deal) == "<Deal 'Widgetz.io // Gold plan // 70 users // New business' #31001944158>"
