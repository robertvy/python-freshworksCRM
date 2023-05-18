import datetime

import pytest

from freshsales.models import (
    User,
    Territory,
    DealStage,
    Currency,
    DealReason,
    DealType,
    LeadSource,
    IndustryType,
    BusinessType,
    DealPaymentStatus,
    DealProduct,
    DealPipeline,
    ContactStatus,
    SalesActivityType,
    SalesActivityEntityType,
    SalesActivityOutcome,
    LifecycleStage,
)


def test_get_users(api):
    users = api.selectors.get_users()
    assert isinstance(users, list)
    assert isinstance(users[0], User)
    assert len(users) > 0
    assert users[0].id == 31000148397
    assert users[0].email == "rvy@go.com"


def test_get_territories(api):
    territories = api.selectors.get_territories()
    assert isinstance(territories, list)
    assert isinstance(territories[0], Territory)
    assert len(territories) > 0
    assert territories[0].id == 31000000775
    assert territories[0].name == "DACH"


def test_get_deal_stages(api):
    deal_stages = api.selectors.get_deal_stages()
    assert isinstance(deal_stages, list)
    assert isinstance(deal_stages[0], DealStage)
    assert len(deal_stages) > 0
    assert deal_stages[1].id == 31000425872
    assert deal_stages[1].name == "Follow-up"
    assert isinstance(deal_stages[1].updated_at, datetime.datetime)


def test_get_currencies(api):
    currencies = api.selectors.get_currencies()
    assert isinstance(currencies, list)
    assert isinstance(currencies[0], Currency)
    assert len(currencies) > 0
    assert currencies[0].id == 31000060446
    assert currencies[0].currency_code == "USD"


def test_get_deal_reasons(api):
    deal_reasons = api.selectors.get_deal_reasons()
    assert isinstance(deal_reasons, list)
    assert isinstance(deal_reasons[0], DealReason)
    assert len(deal_reasons) > 0
    assert deal_reasons[1].id == 31000538252
    assert deal_reasons[1].name == "Price is too high"


def test_get_deal_types(api):
    deal_types = api.selectors.get_deal_types()
    assert isinstance(deal_types, list)
    assert isinstance(deal_types[0], DealType)
    assert len(deal_types) > 0
    assert deal_types[1].id == 31000179101
    assert deal_types[1].name == "Existing Business-Renewal"


def test_get_lead_sources(api):
    lead_sources = api.selectors.get_lead_sources()
    assert isinstance(lead_sources, list)
    assert isinstance(lead_sources[0], LeadSource)
    assert len(lead_sources) > 0
    assert lead_sources[1].id == 31000836319
    assert lead_sources[1].name == "Organic Search"


def test_get_industry_types(api):
    industry_types = api.selectors.get_industry_types()
    assert isinstance(industry_types, list)
    assert isinstance(industry_types[0], IndustryType)
    assert len(industry_types) > 0
    assert industry_types[2].id == 31004057006
    assert industry_types[2].name == "Aerospace"


def test_get_business_types(api):
    business_types = api.selectors.get_business_types()
    assert isinstance(business_types, list)
    assert isinstance(business_types[0], BusinessType)
    assert len(business_types) > 0
    assert business_types[1].id == 31000596652
    assert business_types[1].name == "Competitor"


def test_get_deal_payment_statuses(api):
    deal_payment_statuses = api.selectors.get_deal_payment_statuses()
    assert isinstance(deal_payment_statuses, list)
    assert isinstance(deal_payment_statuses[0], DealPaymentStatus)
    assert len(deal_payment_statuses) > 0
    assert deal_payment_statuses[1].id == 31000119235
    assert deal_payment_statuses[1].name == "Online"


# cannot test deal products, campaigns (empty list)


def test_get_deal_pipelines(api):
    deal_pipelines = api.selectors.get_deal_pipelines()
    assert isinstance(deal_pipelines, list)
    assert isinstance(deal_pipelines[0], DealPipeline)
    assert len(deal_pipelines) > 0
    assert deal_pipelines[0].id == 31000060739
    assert deal_pipelines[0].name == "Default Pipeline"
    assert isinstance(
        deal_pipelines[0].deal_stages[0].updated_at, datetime.datetime)


def test_get_contact_statuses(api):
    contact_statuses = api.selectors.get_contact_statuses()
    assert isinstance(contact_statuses, list)
    assert isinstance(contact_statuses[0], ContactStatus)
    assert len(contact_statuses) > 0
    assert contact_statuses[1].id == 31000543558
    assert contact_statuses[1].name == "Contacted"


def test_get_sales_activity_types(api):
    sales_activity_types = api.selectors.get_sales_activity_types()
    assert isinstance(sales_activity_types, list)
    assert isinstance(sales_activity_types[0], SalesActivityType)
    assert len(sales_activity_types) > 0
    assert sales_activity_types[1].id == 31000477934
    assert sales_activity_types[1].name == "Phone"


def test_get_sales_activity_entity_types(api):
    sales_activity_entity_types = api.selectors.get_sales_activity_entity_types()
    assert isinstance(sales_activity_entity_types, list)
    assert isinstance(sales_activity_entity_types[0], SalesActivityEntityType)
    assert len(sales_activity_entity_types) > 0
    assert sales_activity_entity_types[1].id == 31000179230
    assert sales_activity_entity_types[1].name == "Call reminder"


def test_get_sales_activity_outcomes(api):
    sales_activity_outcomes = api.selectors.get_sales_activity_outcomes()
    assert isinstance(sales_activity_outcomes, list)
    assert isinstance(sales_activity_outcomes[0], SalesActivityOutcome)
    assert len(sales_activity_outcomes) > 0
    assert sales_activity_outcomes[1].id == 31002091456
    assert sales_activity_outcomes[1].name == "Interested"


def test_get_sales_activity_type_outcomes(api):
    sales_activity_type_outcomes = api.selectors.get_sales_activity_type_outcomes(
        31000477933)
    assert isinstance(sales_activity_type_outcomes, list)
    assert isinstance(
        sales_activity_type_outcomes[0], SalesActivityOutcome)
    assert len(sales_activity_type_outcomes) > 0
    assert sales_activity_type_outcomes[1].id == 31002091472
    assert sales_activity_type_outcomes[1].name == "Left message"


def test_get_lifecycle_stages(api):
    life_cycle_stages = api.selectors.get_lifecycle_stages()
    assert isinstance(life_cycle_stages, list)
    assert isinstance(life_cycle_stages[0], LifecycleStage)
    assert len(life_cycle_stages) > 0
    assert life_cycle_stages[1].id == 32009647299
    assert life_cycle_stages[1].name == "Sales Qualified Lead"
