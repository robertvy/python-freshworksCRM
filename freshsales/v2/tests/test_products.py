import datetime

import pytest

from freshsales.v2.models import (
    Product,
    Deal,
)


@pytest.fixture
def product(api):
    return api.products.view_product(31000985829)


def test_create_product(api):
    product = api.products.create_product(
        name='Updated Product',
        description='This is a sample product',
        category='Software',
        is_active=True,
        product_code='sample_product',
        sku_number='sample_sku',
    )

    assert isinstance(product, Product)
    assert product.name == 'Updated Product Name'
    assert product.description == 'This is a sample product'
    assert isinstance(product.created_at, datetime.datetime)
    assert isinstance(product.updated_at, datetime.datetime)


def test_view_product(product):
    assert isinstance(product, Product)
    assert product.name == 'Updated Product Name'
    assert product.description == 'This is a sample product'
    assert isinstance(product.created_at, datetime.datetime)
    assert isinstance(product.updated_at, datetime.datetime)


def test_update_product(api):
    product = api.products.update_product(
        31000985829, name="Updated Product Name")
    assert isinstance(product, Product)
    assert product.name == "Updated Product Name"


def test_delete_product(api):
    assert api.products.delete_product(31000985829) == True


def test_restore_product(api):
    product = api.products.restore_product(31000985829)
    assert isinstance(product, Product)
    assert product.name == "Updated Product Name"


def test_add_product_prices(api):
    product_pricings = [
        {"currency_code": "USD", "unit_price": 2000}
    ]
    product = api.products.add_product_prices(
        31000985829,
        pricing_type=1,
        product_pricings=product_pricings
    )

    assert isinstance(product, Product)
    assert product.name == "Sample Product"
    assert product.base_currency_amount == 2000


def test_edit_product_prices(api):
    product_pricings = [
        {"currency_code": "USD", "unit_price": 2000}
    ]
    product = api.products.edit_product_prices(
        31000985829,
        product_pricings=product_pricings
    )

    assert isinstance(product, Product)
    assert product.name == "Sample Product"
    assert product.base_currency_amount == 2000


def test_delete_product_prices(api):
    product = api.products.delete_product_prices(31000985854, [31000864003])
    assert isinstance(product, Product)
    pricings = product.product_pricings
    is_deleted = True
    for pricing in pricings:
        if pricing['id'] == 31000864003:
            is_deleted = False
            break

    assert is_deleted


def test_add_products_to_deal(api):
    products = [{"id": 31000985829}]
    deal = api.products.add_products_to_deal(
        31001944158,
        products=products
    )
    assert isinstance(deal, Deal)
    assert deal.name == "Widgetz.io // Gold plan // 70 users // New business"
    assert isinstance(deal.products, list)
    assert isinstance(deal.products[0], Product)
    assert deal.products[0].name == "Sample Product"


def test_edit_deal_products(api):
    products = [{"id": 31000985829}]
    deal = api.products.edit_deal_products(
        31001944158,
        products=products
    )
    assert isinstance(deal, Deal)
    assert deal.name == "Widgetz.io // Gold plan // 70 users // New business"
    assert isinstance(deal.products, list)
    assert isinstance(deal.products[0], Product)
    assert deal.products[0].name == "Sample Product"


def test_delete_all_deal_products(api):
    deal = api.products.delete_all_deal_products(31001944160)
    assert isinstance(deal, Deal)
    assert deal.products == []


def test_product_str(product):
    assert str(
        product) == "Updated Product Name"


def test_product_repr(product):
    assert repr(
        product) == "<Product 'Updated Product Name' #31000985825>"
