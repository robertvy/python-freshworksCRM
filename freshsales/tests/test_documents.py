import datetime

import pytest

from freshsales.models import (
    Document,
    Product,
)


@pytest.fixture
def document(api):
    return api.documents.view_document(31000039106)


def test_create_document(api):
    document = api.documents.create_document(
        deal_id=31002174127,
        contact_id=31020103346,
        display_name='Sample Document',
        document_type='Quote',
        cpq_document_template_name='Sample Template',
        currency_code='USD'
    )

    assert isinstance(document, Document)
    assert document.display_name == 'Sample Document'
    assert isinstance(document.created_at, datetime.datetime)
    assert isinstance(document.updated_at, datetime.datetime)


def test_view_document(document):
    assert isinstance(document, Document)
    assert document.display_name == 'Sample Document'
    assert isinstance(document.created_at, datetime.datetime)
    assert isinstance(document.updated_at, datetime.datetime)


def test_update_document(api):
    document = api.documents.update_document(
        31000039106,
        display_name='Sample Document 2')

    assert isinstance(document, Document)
    assert document.display_name == 'Sample Document 2'


def test_delete_document(api):
    assert api.documents.delete_document(31000039106) == True


def test_restore_document(api):
    document = api.documents.restore_document(31000039106)
    assert isinstance(document, Document)
    assert document.display_name == 'Sample Document 2'


def test_forget_document(api):
    assert api.documents.forget_document(31000039106) == True


def test_add_products_to_document(api):
    products = [
        {"id": 31000986007, "quantity": 2}
    ]
    document = api.documents.add_products_to_document(
        31000039151,
        products=products
    )

    assert isinstance(document, Document)
    assert document.display_name == 'Sample1 Document'
    assert isinstance(document.products[0], Product)
    assert document.products[0].id == 31000986007


def test_edit_products_of_document(api):
    products = [
        {"id": 31000986007, "quantity": 2, "discount": 10}
    ]
    document = api.documents.edit_products_of_document(
        31000039151,
        products=products
    )

    assert isinstance(document, Document)
    assert document.display_name == 'Sample1 Document'
    assert isinstance(document.products[0], Product)
    assert document.products[0].id == 31000986007
    assert document.products[0].quantity == 2
    assert document.products[0].discount == 10


def test_delete_products_from_document(api):
    document = api.documents.delete_products_from_document(
        31000039150
    )

    assert isinstance(document, Document)
    assert document.display_name == 'Sample1 Document'
    assert document.products == []


def test_get_related_products(api):
    products = api.documents.get_related_products(31000039151)
    assert isinstance(products, list)
    assert isinstance(products[0], Product)
    assert products[0].id == 31000986007


def test_document_str(document):
    assert str(
        document) == "Sample Document"


def test_document_repr(document):
    assert repr(
        document) == "<Document 'Sample Document' #31000039106>"
