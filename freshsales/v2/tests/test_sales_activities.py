import datetime

import pytest

from freshsales.v2.models import (
    SalesActivity,
    Field,
)


@pytest.fixture
def sales_activity(api):
    return api.sales_activities.view_sales_activity(31000274656)


def test_create_sales_activity(api):
    sales_activity = api.sales_activities.create_sales_activity(
        title='ticket',
        notes='sample',
        targetable_id=31016358306,
        targetable_type='Contact',
        start_date='2017-12-04T17:00:00+05:30',
        end_date='2017-12-04T17:30:00+05:30',
        owner_id=31000148397,
        sales_activity_type_id=31000559503,)

    assert isinstance(sales_activity, SalesActivity)
    assert sales_activity.title == "ticket"
    assert sales_activity.notes == "sample"
    assert sales_activity.targetable_id == 31016358306
    assert isinstance(sales_activity.start_date, datetime.datetime)
    assert isinstance(sales_activity.end_date, datetime.datetime)
    assert isinstance(sales_activity.created_at, datetime.datetime)


def test_view_sales_activity(sales_activity):
    assert isinstance(sales_activity, SalesActivity)
    assert sales_activity.title == "ticket"
    assert sales_activity.notes == "sample"
    assert sales_activity.targetable_id == 31016358306
    assert isinstance(sales_activity.start_date, datetime.datetime)
    assert isinstance(sales_activity.end_date, datetime.datetime)
    assert isinstance(sales_activity.created_at, datetime.datetime)


def test_list_all_sales_activities(api):
    sales_activities = api.sales_activities.list_all_sales_activities()
    assert isinstance(sales_activities[0], SalesActivity)
    assert sales_activities[0].title == "ticket"
    assert sales_activities[1].title == "ticket 2"
    assert sales_activities[0].targetable_id == 31016358306
    assert isinstance(sales_activities[0].start_date, datetime.datetime)
    assert isinstance(sales_activities[0].end_date, datetime.datetime)
    assert isinstance(sales_activities[0].created_at, datetime.datetime)


def test_list_all_sales_activity_fields(api):
    fields = api.sales_activities.list_all_sales_activity_fields()
    assert isinstance(fields, list)
    assert isinstance(fields[0], Field)
    assert fields[1].name == "start_date"


def test_update_sales_activity(api):
    sales_activity = api.sales_activities.update_sales_activity(
        31000274656, title='ticket Updated')
    assert isinstance(sales_activity, SalesActivity)
    assert sales_activity.title == "ticket Updated"


def test_delete_sales_activity(api):
    assert api.sales_activities.delete_sales_activity(31000274656) == True


def test_sales_activity_str(sales_activity):
    assert str(
        sales_activity) == "ticket"


def test_sales_activity_repr(sales_activity):
    assert repr(
        sales_activity) == "<SalesActivity 'ticket' #31000274656>"
