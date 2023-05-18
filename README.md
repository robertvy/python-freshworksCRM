# Python Wrapper for Freshsales Suite CRM

[![PyPI](https://img.shields.io/pypi/v/python-freshworks-crm)](https://pypi.org/project/python-freshworks-crm/)
![Stars](https://img.shields.io/github/stars/robertvy/python-freshworksCRM)
![Forks](https://img.shields.io/github/forks/robertvy/python-freshworksCRM)

[![Build Status](https://app.travis-ci.com/robertvy/python-freshworksCRM.svg?branch=main)](https://app.travis-ci.com/robertvy/python-freshworksCRM)
[![codecov](https://codecov.io/github/robertvy/python-freshworksCRM/branch/main/graph/badge.svg?token=M6E8FH72KD)](https://codecov.io/github/robertvy/python-freshworksCRM)
![Downloads](https://img.shields.io/pypi/dm/python-freshworks-crm)
![License](https://img.shields.io/github/license/robertvy/python-freshworksCRM)

This is a library for the [Freshsales Suite CRM](https://www.freshworks.com/crm/features/) for Python 3.6+.

It includes the following features from the [Freshsales Suite CRM API](https://developers.freshworks.com/crm/api/):

- [Contacts](https://developers.freshworks.com/crm/api/#contacts)
  - [Create](https://developers.freshworks.com/crm/api/#create_a_contact)
  - [View](https://developers.freshworks.com/crm/api/#view_a_contact)
  - [List](https://developers.freshworks.com/crm/api/#list_all_contacts)
  - [Update](https://developers.freshworks.com/crm/api/#update_a_contact)
  - [Upsert](https://developers.freshworks.com/crm/api/#upsert_a_contact)
  - [Clone](https://developers.freshworks.com/crm/api/#clone_a_contact)
  - [Delete](https://developers.freshworks.com/crm/api/#delete_a_contact)
  - [Forget](https://developers.freshworks.com/crm/api/#forget_a_contact)
  - [List Fields](https://developers.freshworks.com/crm/api/#list_all_contact_fields)
  - [List Activities](https://developers.freshworks.com/crm/api/#list_all_contact_activities)
- [Marketing Lists](https://developers.freshworks.com/crm/api/#marketing-lists)
  - [Create](https://developers.freshworks.com/crm/api/#create_list)
  - [List](https://developers.freshworks.com/crm/api/#fetch_all_lists)
  - [Update](https://developers.freshworks.com/crm/api/#update_a_list)
  - [List Contacts](https://developers.freshworks.com/crm/api/#fetch_all_contacts_from_list)
  - [Copy Contacts](https://developers.freshworks.com/crm/api/#copy_to_list)
  - [Add Contacts](https://developers.freshworks.com/crm/api/#add_to_list)
  - [Remove Contacts](https://developers.freshworks.com/crm/api/#remove_contact_from_list)
  - [Move Contacts](https://developers.freshworks.com/crm/api/#move_contact_from_list)
- [Accounts](https://developers.freshworks.com/crm/api/#accounts)
  - [Create](https://developers.freshworks.com/crm/api/#create_account)
  - [View](https://developers.freshworks.com/crm/api/#view_account)
  - [List](https://developers.freshworks.com/crm/api/#list_all_accounts)
  - [Update](https://developers.freshworks.com/crm/api/#update_a_account)
  - [Upsert](https://developers.freshworks.com/crm/api/#upsert_an_account)
  - [Clone](https://developers.freshworks.com/crm/api/#clone_an_account)
  - [Delete](https://developers.freshworks.com/crm/api/#delete_account)
  - [Forget](https://developers.freshworks.com/crm/api/#forget_account)
  - [List Fields](https://developers.freshworks.com/crm/api/#list_all_account_fields)
- [Deals](https://developers.freshworks.com/crm/api/#deals)
  - [Create](https://developers.freshworks.com/crm/api/#create_a_deal)
  - [View](https://developers.freshworks.com/crm/api/#view_a_deal)
  - [List](https://developers.freshworks.com/crm/api/#list_all_deals)
  - [Update](https://developers.freshworks.com/crm/api/#update_a_deal)
  - [Upsert](https://developers.freshworks.com/crm/api/#upsert_a_deal)
  - [Clone](https://developers.freshworks.com/crm/api/#clone_a_deal)
  - [Delete](https://developers.freshworks.com/crm/api/#delete_a_deal)
  - [Forget](https://developers.freshworks.com/crm/api/#forget_a_deal)
  - [List Fields](https://developers.freshworks.com/crm/api/#list_all_deal_fields)
- [Notes](https://developers.freshworks.com/crm/api/#notes)
  - [Create](https://developers.freshworks.com/crm/api/#create_note)
  - [Update](https://developers.freshworks.com/crm/api/#update_note)
  - [Delete](https://developers.freshworks.com/crm/api/#delete_a_note)
- [Tasks](https://developers.freshworks.com/crm/api/#tasks)
  - [Create](https://developers.freshworks.com/crm/api/#create_task)
  - [View](https://developers.freshworks.com/crm/api/#view_task)
  - [List](https://developers.freshworks.com/crm/api/#list_all_task)
  - [Update](https://developers.freshworks.com/crm/api/#update_task)
  - [Mark as Done](https://developers.freshworks.com/crm/api/#mark_task_done)
  - [Delete](https://developers.freshworks.com/crm/api/#delete_task)
- [Appointments](https://developers.freshworks.com/crm/api/#appointments)
  - [Create](https://developers.freshworks.com/crm/api/#create_appointment)
  - [View](https://developers.freshworks.com/crm/api/#view_an_appointment)
  - [List](https://developers.freshworks.com/crm/api/#list_all_appointment)
  - [Update](https://developers.freshworks.com/crm/api/#update_an_appointment)
  - [Delete](https://developers.freshworks.com/crm/api/#delete_an_appointment)
- [Sales Activities](https://developers.freshworks.com/crm/api/#sales-activities)
  - [Create](https://developers.freshworks.com/crm/api/#create_sales_activity)
  - [View](https://developers.freshworks.com/crm/api/#view_a_sales_activity)
  - [List](https://developers.freshworks.com/crm/api/#list_all_sales_activities)
  - [List Fields](https://developers.freshworks.com/crm/api/#list_all_sales_activity_fields)
  - [Update](https://developers.freshworks.com/crm/api/#update_a_sales_activity)
  - [Delete](https://developers.freshworks.com/crm/api/#delete_a_sales_activity)
- [Products](https://developers.freshworks.com/crm/api/#products)
  - [Create](https://developers.freshworks.com/crm/api/#create_product)
  - [View](https://developers.freshworks.com/crm/api/#view_a_product)
  - [Update](https://developers.freshworks.com/crm/api/#update_a_product)
  - [Delete](https://developers.freshworks.com/crm/api/#delete_a_product)
  - [Restore](https://developers.freshworks.com/crm/api/#restore_a_product)
  - [Add Prices](https://developers.freshworks.com/crm/api/#add_prices_to_the_product)
  - [Edit Prices](https://developers.freshworks.com/crm/api/#edit_prices_of_the_product)
  - [Delete Prices](https://developers.freshworks.com/crm/api/#delete_prices_of_the_product)
  - [Add to Deal](https://developers.freshworks.com/crm/api/#add_products_to_the_deal)
  - [Edit in Deal](https://developers.freshworks.com/crm/api/#edit_products_of_the_deal)
  - [Delete from Deal](https://developers.freshworks.com/crm/api/#delete_products_of_the_deal)
- [Documents](https://developers.freshworks.com/crm/api/#documents)
  - [Create](https://developers.freshworks.com/crm/api/#create_document)
  - [View](https://developers.freshworks.com/crm/api/#view_a_document)
  - [Update](https://developers.freshworks.com/crm/api/#update_a_document)
  - [Delete](https://developers.freshworks.com/crm/api/#delete_a_document)
  - [Restore](https://developers.freshworks.com/crm/api/#restore_a_document)
  - [Forget](https://developers.freshworks.com/crm/api/#forget_a_document)
  - [Add Products](https://developers.freshworks.com/crm/api/#add_products_to_the_document)
  - [Edit Products](https://developers.freshworks.com/crm/api/#edit_products_of_the_document)
  - [Delete Products](https://developers.freshworks.com/crm/api/#delete_products_of_the_document)
  - [Related Products](https://developers.freshworks.com/crm/api/#related_products)
- [Selectors](https://developers.freshworks.com/crm/api/#admin_configuration)

## Installation

The easiest way to install is from [PyPi](https://pypi.org/project/python-freshworks-crm/) inside a virtualenv:

1. Create the virtualenv (Python 3.6+ supported) and activate it:

   ```
   $ virtualenv env
   $ source env/bin/activate
   ```

2. Install from PyPi:

   ```
   $ pip install python-freshworks-crm
   ```

3. Optionally, run the test suite:

   ```
   $ pip install python-freshworks-crm[test]
   $ pytest
   ```

## Usage

Please note the domain and API key are not real and the example will not work without changing these.

```python
>>> from freshsales.api import API
>>> a = API('company.myfreshworks.com/crm/sales', 'fsdajfl323kj423rj2')
```

To find your API key, follow Freshworks CRM step-by-step solution article
[How to find your API key](https://crmsupport.freshworks.com/en/support/solutions/articles/50000002503-how-to-find-my-api-key-).

The `API` class provides access to all the methods exposed by the Freshsales Suite CRM API.

### General

Attributes are automatically converted to native Python objects where appropriate:

```python
>>> a.contacts.list_contacts()[0].created_at
datetime.datetime(2023, 12, 5, 14, 7, 44)
```

### Contacts

The Contacts API is accessed by using the methods assigned to the `a.contacts` instance. Contacts are loaded as instances of the `freshsales.models.Contact` class.

#### Create

```python
>>> a.contacts.create_contact(first_name='Jane',
                              last_name='Sampleton',
                              emails='janesampleton@gmail.com',
                              custom_field=custom_field)
<Contact 'Jane Sampleton'>
```

With custom fields:

```python
>>> custom_field = {'custom_field_1': 'custom_value_1',
                     'custom_field_2': 'custom_value_2'}

>>> a.contacts.create_contact(first_name='Jane',
                              last_name='Sampleton',
                              emails='janesampleton@gmail.com',
                              custom_field=custom_field)
<Contact 'Jane Sampleton'>
```

To access any attribute of the contact, use the dot notation:

```python
>>> contact.first_name
'Jane'
```

#### View

```python
>>> a.contacts.view_contact(1)
<Contact 'John Doe'>
```

#### Views

```python
>>> a.contacts.list_views()
[<View 'All Contacts'>, <View 'My Contacts'>]
```

#### List

```python
>>> a.contacts.list_contacts()
[<Contact 'John Doe'>, <Contact 'Jane Sampleton'>]
```

Get specific page of contacts:

```python
>>> a.contacts.list_contacts(page=2, per_page=5)
[<Contact 'John Doe'>, <Contact 'Jane Sampleton'>,...]
```

[<Contact 'Jane Sampleton'>]

```
[<Contact 'Jane Sampleton'>]
```

#### Update

```python
>>> a.contacts.update_contact(1,
                              first_name='Jane',
                              last_name='Updated')
<Contact 'Jane Updated'></Contact>
```

### Upsert

```python
>>> a.contacts.upsert_contact(unique_identifier=('emails', 'janesampleton@gmail.com'),
                              first_name='Jane',
                              last_name='Upserted')
<Contact 'Jane Upserted'></Contact>
```

#### Delete

```python
>>> a.contacts.delete_contact(1)
True
```

#### Forget

```python
>>> a.contacts.forget_contact(1)
True
```

#### List Fields

```python
>>> a.contacts.list_fields()
[<Field 'first_name'>, <Field 'last_name'>, <Field 'emails'>, ...]
```

#### List Activities

```python
>>> a.contacts.list_activities(1)
[<Activity 'Call'>, <Activity 'Email'>, <Activity 'Meeting'>, ...]
```

### Marketing Lists

The Marketing Lists API is accessed by using the methods assigned to the `a.lists` instance. Marketing Lists are loaded as instances of the `freshsales.models.List` class.

#### Create

```python
>>> a.lists.create_list(name='My List')
<List 'My List'>
```

#### View

```python
>>> a.lists.view_list(1)
<List 'My List'>
```

#### List

```python
>>> a.lists.fetch_all_lists()
[<List 'My List'>, <List 'My Other List'>]
```

#### Update

```python
>>> a.lists.update_list(1,
                        name='My Updated List')
<List 'My Updated List'></List>
```

#### Fetch Contacts

```python
>>> a.lists.fetch_contacts_from_list(1)
[<Contact 'John Doe'>, <Contact 'Jane Sampleton'>]
```

#### Add Contacts

```python
>>> a.lists.add_contacts_to_list(1, [1, 2])
'2 contacts updated.'
```

#### Remove Contacts

```python
>>> a.lists.remove_contacts_from_list(1, [1, 2])
'2 contacts updated.'
```

#### Move Contacts

```python
>>> a.lists.move_contacts_to_list(2, [1, 2])
'2 contacts updated.'
```

### Accounts

The Accounts API is accessed by using the methods assigned to the `a.accounts` instance. Accounts are loaded as instances of the `freshsales.models.Account` class.

#### Create

```python
>>> a.accounts.create_account(name='My Account')
<Account 'My Account'>
```

#### View

```python
>>> a.accounts.view_account(1)
<Account 'My Account'>
```

#### Views

```python
>>> a.accounts.list_views()
[<View 'My View'>, <View 'My Other View'>]
```

#### List

```python
>>> a.accounts.list_accounts()
[<Account 'My Account'>, <Account 'My Other Account'>]
```

Note: supports pagination similar to contacts.

#### Update

```python
>>> a.accounts.update_account(1,
                              name='My Updated Account')
<Account 'My Updated Account'>
```

#### Upsert

```python
>>> a.accounts.upsert(unique_identifier=('name', 'My Account'),
name='My Upserted Account')
<Account 'My Upserted Account'>
```

#### Clone

```python
>>> a.accounts.clone_account(1)
<Account 'My Cloned Account'>
```

#### Delete

```python
>>> a.accounts.delete_account(1)
True
```

#### Forget

```python
>>> a.accounts.forget_account(1)
True
```

#### List Fields

```python
>>> a.accounts.list_fields()
[<Field 'name'>, <Field 'website'>, <Field 'industry'>, ...]
```

### Deals

The Deals API is accessed by using the methods assigned to the `a.deals` instance. Deals are loaded as instances of the `freshsales.models.Deal` class.

#### Create

```python
>>> a.deals.create_deal(name='My Deal')
<Deal 'My Deal'>
```

#### View

```python
>>> a.deals.view_deal(1)
<Deal 'My Deal'>
```

#### Views

```python
>>> a.deals.list_views()
[<View 'My View'>, <View 'My Other View'>]
```

#### List

```python
>>> a.deals.list_deals()
[<Deal 'My Deal'>, <Deal 'My Other Deal'>]
```

Note: supports pagination similar to contacts.

#### Update

```python
>>> a.deals.update_deal(1,
                        name='My Updated Deal')
<Deal 'My Updated Deal'>
```

#### Upsert

```python
>>> a.deals.upsert(unique_identifier=('name', 'My Deal'),
                   name='My Upserted Deal')
<Deal 'My Upserted Deal'>
```

#### Clone

```python
>>> a.deals.clone_deal(1)
<Deal 'My Cloned Deal'>
```

#### Delete

```python
>>> a.deals.delete_deal(1)
True
```

#### Forget

```python
>>> a.deals.forget_deal(1)
True
```

#### List Fields

```python
>>> a.deals.list_fields()
[<Field 'name'>, <Field 'amount'>, <Field 'stage'>, ...]
```

### Notes

The Notes API is accessed by using the methods assigned to the `a.notes` instance. Notes are loaded as instances of the `freshsales.models.Note` class.

#### Create

```python
>>> a.notes.create_note(description='My Note',
                        targetable_type='Contact',
                        targetable_id=1)
<Note 'My Note'></Note>
```

#### Update

```python
>>> a.notes.update_note(1,
                        description='My Updated Note')
<Note 'My Updated Note'>
```

#### Delete

```python
>>> a.notes.delete_note(1)
True
```

### Tasks

The Tasks API is accessed by using the methods assigned to the `a.tasks` instance. Tasks are loaded as instances of the `freshsales.models.Task` class.

#### Create

```python
>>> a.tasks.create_task(title='Sample Task',
                        description='This is just a sample task.',
                        due_date='Tue Jun 21 2099 11:00:00 GMT+0000',
                        owner_id=1,
                        targetable_id=1,
                        targetable_type='Contact')
<Task 'Sample Task'>`
```

#### View

```python
>>> a.tasks.view_task(1)
<Task 'Sample Task'>
```

#### List

```python
>>> a.tasks.list_tasks()
[<Task 'Sample Task'>, <Task 'My Other Task'>]
```

Note: supports pagination similar to contacts.

#### Update

```python
>>> a.tasks.update_task(1,
                        title='Updated Task')
<sk 'Updated Task'>
```

#### Mark as Done

```python
>>> a.tasks.mark_task_as_done(1)
<Task 'Updated Task'>
```

#### Delete

```python
>>> a.tasks.delete_task(1)
True
```

### Appointments

The Appointments API is accessed by using the methods assigned to the `a.appointments` instance. Appointments are loaded as instances of the `freshsales.models.Appointment` class.

#### Create

```python
>>> a.appointments.appointments.create_appointment(
        title='Sample Appointment',
        description='This is just a sample Appointment.',
        from_date='Mon Jun 20 2016 10:30:00 GMT+0530 (IST)',
        end_date='Mon Jun 20 2016 11:30:00 GMT+0530 (IST)',
        creater_id=1,
        time_zone='Chennai',
        location='Chennai, TN, India',
        targetable_id=1,
        targetable_type='Contact')
<Appointment 'Sample Appointment'>
```

#### View

```python
>>> a.appointments.view_appointment(1)
<Appointment 'Sample Appointment'>
```

#### List

```python
>>> a.appointments.list_appointments()
[<Appointment 'Sample Appointment'>, <Appointment 'My Other Appointment'>]
```

Note: supports pagination similar to contacts.

#### Update

```python
>>> a.appointments.update_appointment(1,
                                      title='Updated Appointment')
< 'Updated Appointment'>
```

#### Delete

```python
>>> a.appointments.delete_appointment(1)
True
```

### Sales Activities

The Sales Activities API is accessed by using the methods assigned to the `a.sales_activities` instance. Sales Activities are loaded as instances of the `freshsales.models.SalesActivity` class.

#### Create

```python
>>> a.sales_activities.sales_activities.create_activity(
        title='My Activity',
        notes='sample',
        targetable_id=1,
        targetable_type='Contact',
        start_date='2017-12-04T17:00:00+05:30',
        end_date='2017-12-04T17:30:00+05:30',
        owner_id=1,
        sales_activity_type_id=1)
<SalesActivity 'My Activity'>
```

#### View

```python
>>> a.sales_activities.view_activity(1)
<SalesActivity 'My Activity'>
```

#### List

```python
>>> a.sales_activities.list_activities()
[<SalesActivity 'My Activity'>, <SalesActivity 'My Other Activity'>]
```

Note: supports pagination similar to contacts.

#### Activity Fields

```python
>>> a.sales_activities.list_fields()
[<Field 'title'>, <Field 'notes'>, <Field 'start_date'>, ...]
```

#### Update

```python
>>> a.sales_activities.update_activity(1,
                                      title='Updated Activity')
<Activity 'Updated Activity'>
```

#### Delete

```python
>>> a.sales_activities.delete_activity(1)
True
```

### Products

The Products API is accessed by using the methods assigned to the `a.products` instance. Products are loaded as instances of the `freshsales.models.Product` class.

#### Create

```python
>>> a.products.create_product(
        name='My Product',
        description='This is a sample product',
        category='Software',
        is_active=True,
        product_code='sample_product',
        sku_number='sample_sku',
    )
<Product 'My Product'>
```

#### View

```python
>>> a.products.view_product(1)
<Product 'My Product'>
```

#### Update

```python
>>> a.products.update_product(1,
                              name='Updated Product')
<Product 'Updated Product'>
```

#### Delete

```python
>>> a.products.delete_product(1)
True
```

#### Restore

```python
>>> a.products.restore_product(1)
<Product 'Updated Product'>
```

#### Edit Product Prices

```python
>>> product_pricings = [
        {"currency_code": "USD", "unit_price": 2000}
    ]
    product = api.products.edit_product_prices(
        1,
        product_pricings=product_pricings
    )
<Product 'Updated Product'>
```

#### Delete Product Prices

```python
>>> product = api.products.delete_product_prices(1,
                                                 [100, 101])

<Product 'Updated Product'>
```

### Add Products to Deal

```python
>>> products = [{"id": 100}]
    deal = api.products.add_products_to_deal(
        1,
        products=products
    )
<Deal 'Updated Deal'>
```

### Edit Deal Products

```python
>>> products = [{"id": 100, "quantity": 2}]
    deal = api.products.edit_deal_products(
        1,
        products=products
    )
<Deal 'Updated Deal'>
```

### Delete All Deal Products

```python
>>> deal = api.products.delete_all_deal_products(1)
<Deal 'Updated Deal'>
```

### Documents

The Documents API is accessed by using the methods assigned to the `a.documents` instance. Documents are loaded as instances of the `freshsales.models.Document` class.

#### Create

```python
>>> a.documents.create_document(
        deal_id=1,
        contact_id=1,
        display_name='Sample Document',
        document_type='Quote',
        cpq_document_template_name='Sample Template',
        currency_code='USD'
    )
<Document 'Sample Document'>
```

#### View

```python
>>> a.documents.view_document(1)
<Document 'Sample Document'>
```

#### Update

```python
>>> a.documents.update_document(1,
                                display_name='Updated Document')
<Document 'Updated Document'>
```

#### Delete

```python
>>> a.documents.delete_document(1)
True
```

#### Restore

```python
>>> a.documents.restore_document(1)
<Document 'Updated Document'>
```

#### Forget

```python
>>> a.documents.forget_document(1)
True
```

#### Add Products to Document

```python
>>> products = [
        {"id": 100, "quantity": 2}
    ]
    document = api.documents.add_products_to_document(
        1,
        products=products
    )
<Document 'Updated Document'>
```

#### Edit Products of Document

```python
>>> products = [
        {"id": 100, "quantity": 3}
    ]
    document = api.documents.edit_products_of_document(
        1,
        products=products
    )
<Document 'Updated Document'>
```

#### Delete All Products from Document

```python
>>> document = api.documents.delete_products_from_document(1)
<Document 'Updated Document'>
```

### Selectors

The Selectors API is accessed by using the methods assigned to the `a.selectors` instance. Selectors are loaded as instances of the `freshsales.models.Selector` class.

#### Users

```python
>>> a.selectors.get_users()
[<User 'John Doe'>, <User 'Jane Doe'>]
```

#### Territories

```python
>>> a.selectors.get_territories()
[<Territory 'North America'>, <Territory 'South America'>]
```

#### Deal Stages

```python
>>> a.selectors.get_deal_stages()
[<DealStage 'Prospecting'>, <DealStage 'Qualification'>]
```

#### Currencies

```python
>>> a.selectors.get_currencies()
[<Currency 'USD'>, <Currency 'EUR'>]
```

#### Deal Reasons

```python
>>> a.selectors.get_deal_reasons()
[<DealReason 'New Business'>, <DealReason 'Renewal'>]
```

#### Deal Types

```python
>>> a.selectors.get_deal_types()
[<DealType 'New Business'>, <DealType 'Renewal'>]
```

#### Lead Sources

```python
>>> a.selectors.get_lead_sources()
[<LeadSource 'Website'>, <LeadSource 'Email'>]
```

#### Industry Types

```python
>>> a.selectors.get_industry_types()
[<IndustryType 'Agriculture'>, <IndustryType 'Construction'>]
```

#### Business Types

```python
>>> a.selectors.get_business_types()
[<BusinessType 'Customer'>, <BusinessType 'Competitor'>]
```

#### Deal Payment Statuses

```python
>>> a.selectors.get_deal_payment_statuses()
[<DealPaymentStatus 'Paid'>, <DealPaymentStatus 'Unpaid'>]
```

#### Deal Products

```python
>>> a.selectors.get_deal_products()
[<DealProduct 'Product 1'>, <DealProduct 'Product 2'>]
```

#### Deal Pipelines

```python
>>> a.selectors.get_deal_pipelines()
[<DealPipeline 'Sales Pipeline'>, <DealPipeline 'Renewal Pipeline'>]
```

#### Contact Statuses

```python
>>> a.selectors.get_contact_statuses()
[<ContactStatus 'Open'>, <ContactStatus 'Closed'>]
```

#### Sales Activity Types

```python
>>> a.selectors.get_sales_activity_types()
[<SalesActivityType 'Call'>, <SalesActivityType 'Email'>]
```

#### Sales Activity Entity Types

```python
>>> a.selectors.get_sales_activity_entity_types()
[<SalesActivityEntityType 'Contact'>, <SalesActivityEntityType 'Deal'>]
```

#### Sales Activity Outcomes

```python
>>> a.selectors.get_sales_activity_outcomes()
[<SalesActivityOutcome 'Success'>, <SalesActivityOutcome 'Failure'>]
```

#### Lifecycle Stages

```python
>>> a.selectors.get_lifecycle_stages()
[<LifecycleStage 'Lead'>, <LifecycleStage 'Customer'>]
```

### Testing

To run the tests, you'll need to install the development dependencies:

```bash
$ pip install python-freshworks-crm[test]
```

Then, you can run the tests with:

```bash
$ pytest
```

Travis CI will run the tests against Python 3.6, 3.7, 3.8, 3.9., 3.10, and 3.11

You can also use Tox to run the tests against all supported versions of Python:

```bash
$ tox
```

### Contributing

Contributions are welcome! Bulk APIs as well as endpoints such as Files, Search, Phone, .. are not implemented yet. Feel free to open a pull request.
