import json

import requests
from requests import HTTPError

from freshsales.errors import *

from freshsales.models import *


class ContactAPI(object):
    def __init__(self, api):
        self._api = api

    def create_contact(self, **kwargs):
        url = f'/contacts'
        data = kwargs.copy()
        response = self._api._post(url, data=json.dumps(data)).get('contact', {})
        if response.get('sales_accounts'):
            response['sales_accounts'] = [Account(**account)
                                    for account in response['sales_accounts']]
        return Contact(**response)

    def view_contact(self, contact_id, *include):
        url = f'/contacts/{contact_id}'
        url += f'?include={",".join(include)}' if include else ''
        contact = self._api._get(url)
        response = contact.get("contact", {})
        if response.get('sales_accounts'):
            response['sales_accounts'] = [Account(**account)
                                    for account in response['sales_accounts']]
        return Contact(**response)

    def list_views(self):
        url = '/contacts/filters'
        response = self._api._get(url)
        return [View(**view) for view in response.get('filters', [])]

    def list_contacts(self, view_id, sort=None, sort_type=None, page=None, per_page=100):
        url = f'/contacts/view/{view_id}'
        params = {}

        if sort:
            params['sort'] = sort

        if sort_type:
            params['sort_type'] = sort_type

        response = self._api._get(url)
        total_pages = response.get('meta', {}).get('total_pages', 1)
        contacts = response.get('contacts', [])

        if page is None:
            # Fetch all pages
            contacts = [Contact(**contact) for contact in contacts]
            for current_page in range(2, total_pages + 1):
                page_contacts = self._api._get(
                    url + f"?page={current_page}&per_page={per_page}").get('contacts', [])
                contacts.extend([Contact(**contact)
                                for contact in page_contacts])
        elif 1 <= page <= total_pages:
            # Fetch specified page
            page_contacts = self._api._get(
                url + f"?page={page}&per_page={per_page}").get('contacts', [])
            contacts = [Contact(**contact) for contact in page_contacts]

        return contacts

    def update_contact(self, contact_id, **data):
        url = f'/contacts/{contact_id}'
        response = self._api._put(url, data=json.dumps(data)).get('contact', {})
        if response.get('sales_accounts'):
            response['sales_accounts'] = [Account(**account)
                                    for account in response['sales_accounts']]        
        return Contact(**response)

    def upsert_contact(self, unique_identifier, **contact_properties):
        url = '/contacts/upsert'
        unique_field_name, unique_field_value = unique_identifier
        unique_identifier = {unique_field_name: unique_field_value}
        data = {
            'unique_identifier': unique_identifier,
            'contact': contact_properties
        }
        response = self._api._post(url, data=json.dumps(data)).get('contact', {})
        if response.get('sales_accounts'):
            response['sales_accounts'] = [Account(**account)
                                    for account in response['sales_accounts']]           
        return Contact(**response)

    def clone_contact(self, contact_id, **data):
        url = f'/contacts/{contact_id}/clone'
        payload = {'contact': data} if data else {}
        contact = self._api._post(
            url, data=json.dumps(payload)).get('contact', {})
        if contact.get('sales_accounts'):
            contact['sales_accounts'] = [Account(**account)
                                    for account in contact['sales_accounts']]
        return Contact(**contact)

    def delete_contact(self, contact_id):
        url = f'/contacts/{contact_id}'
        return self._api._delete(url)

    def forget_contact(self, contact_id):
        url = f'/contacts/{contact_id}/forget'
        return self._api._delete(url)

    def list_fields(self, include_groups=False):
        url = '/settings/contacts/fields'
        url += '?include=field_group' if include_groups else ''
        response = self._api._get(url)
        return [Field(**field) for field in response.get('fields', [])]

    def list_activities(self, contact_id, **kwargs):
        url = f'/contacts/{contact_id}/activities'
        response = self._api._get(url, params=kwargs)
        return response['activities']


class ListAPI(object):
    def __init__(self, api):
        self._api = api

    def create_list(self, name):
        url = '/lists'
        response = self._api._post(url, data=json.dumps({'name': name}))
        return List(**response.get('list', {}))

    def fetch_all_lists(self):
        url = '/lists'
        response = self._api._get(url)
        return [List(**list_dict) for list_dict in response.get('lists', [])]

    def update_list(self, list_id, name):
        url = f'/lists/{list_id}'
        response = self._api._put(url, data=json.dumps({'name': name}))
        return List(**response.get('list', {}))

    def fetch_contacts_from_list(self, list_id):
        url = f'/contacts/lists/{list_id}'
        response = self._api._get(url)
        contacts_data = response.get('contacts', [])
        return [Contact(**contact_data) for contact_data in contacts_data]

    def add_contacts_to_list(self, list_id, ids):
        # Note: copy_contacts_to_list is similar to add_contacts_to_list
        url = f'/lists/{list_id}/add_contacts'
        response = self._api._put(url, data=json.dumps({'ids': ids}))
        return response.get('message', '')

    def remove_contacts_from_list(self, list_id, ids, remove_all=False):
        url = f'/lists/{list_id}/remove_contacts'
        if remove_all:
            data = {"all": True}
        else:
            data = {"ids": ids}
        response = self._api._put(url, data=json.dumps(data))
        return response.get('message')

    def move_contacts_between_lists(self, list_id, ids, from_list_id):
        url = f'/lists/{list_id}/move_contacts'
        data = {'ids': ids}
        if from_list_id:
            data['from_list_id'] = from_list_id
        response = self._api._put(url, data=json.dumps(data))
        return response.get('message')


class AccountAPI(object):
    def __init__(self, api):
        self._api = api

    def create_account(self, **kwargs):
        url = f'/sales_accounts'
        data = kwargs.copy()
        response = self._api._post(url, data=json.dumps(data))
        return Account(**response.get('sales_account', {}))

    def view_account(self, account_id, *include):
        url = f'/sales_accounts/{account_id}'
        url += f'?include={",".join(include)}' if include else ''
        response = self._api._get(url)
        return Account(**response.get('sales_account', {}))

    def list_views(self):
        url = '/sales_accounts/filters'
        response = self._api._get(url)
        return [View(**view) for view in response.get('filters', [])]

    def list_accounts(self, view_id, sort=None, sort_type=None, page=None, per_page=100):
        url = f'/sales_accounts/view/{view_id}'
        params = {}

        if sort:
            params['sort'] = sort

        if sort_type:
            params['sort_type'] = sort_type

        response = self._api._get(url)
        total_pages = response.get('meta', {}).get('total_pages', 0)
        accounts = response.get('sales_accounts', [])

        if page is None:
            # Fetch all pages
            accounts = [Account(**account) for account in accounts]
            for current_page in range(2, total_pages + 1):
                page_accounts = self._api._get(
                    url + f"?page={current_page}&per_page={per_page}").get('sales_accounts', [])
                accounts.extend([Account(**account)
                                for account in page_accounts])
        elif 1 <= page <= total_pages:
            # Fetch specified page
            page_accounts = self._api._get(
                url + f"?page={page}&per_page={per_page}").get('sales_accounts', [])
            accounts = [Account(**account) for account in page_accounts]

        return accounts

    def update_account(self, account_id, **data):
        url = f'/sales_accounts/{account_id}'
        response = self._api._put(url, data=json.dumps(data))
        return Account(**response.get('sales_account', {}))

    def upsert_account(self, unique_identifier, **account_properties):
        url = '/sales_accounts/upsert'
        unique_field_name, unique_field_value = unique_identifier
        unique_identifier = {unique_field_name: unique_field_value}
        data = {
            'unique_identifier': unique_identifier,
            'sales_account': account_properties
        }
        response = self._api._post(url, data=json.dumps(data))
        return Account(**response.get('sales_account', {}))

    def clone_account(self, account_id, **data):
        url = f'/sales_accounts/{account_id}/clone'
        payload = {'sales_account': data} if data else {}
        response = self._api._post(url, data=json.dumps(payload))
        return Account(**response.get('sales_account', {}))

    def delete_account(self, account_id):
        url = f'/sales_accounts/{account_id}'
        return self._api._delete(url)

    def forget_account(self, account_id):
        url = f'/sales_accounts/{account_id}/forget'
        return self._api._delete(url)

    def list_fields(self, include_groups=False):
        url = '/settings/sales_accounts/fields'
        url += '?include=field_group' if include_groups else ''
        response = self._api._get(url)
        return [Field(**field) for field in response.get('fields', [])]


class DealAPI(object):
    def __init__(self, api):
        self._api = api

    def create_deal(self, **kwargs):
        url = f'/deals'
        data = kwargs.copy()
        response = self._api._post(url, data=json.dumps(data))
        return Deal(**response.get('deal', {}))

    def view_deal(self, deal_id, *include):
        url = f'/deals/{deal_id}'
        url += f'?include={",".join(include)}' if include else ''
        deal = self._api._get(url)
        response = deal.get("deal", {})
        return Deal(**response)

    def list_views(self):
        url = '/deals/filters'
        response = self._api._get(url)
        return [View(**view) for view in response.get('filters', [])]

    def list_deals(self, view_id, sort=None, sort_type=None, page=None, per_page=100):
        url = f'/deals/view/{view_id}'
        params = {}

        if sort:
            params['sort'] = sort

        if sort_type:
            params['sort_type'] = sort_type

        response = self._api._get(url)
        total_pages = response.get('meta', {}).get('total_pages', 0)
        deals = response.get('deals', [])

        if page is None:
            # Fetch all pages
            deals = [Deal(**deal) for deal in deals]
            for current_page in range(2, total_pages + 1):
                page_deals = self._api._get(
                    url + f"?page={current_page}&per_page={per_page}").get('deals', [])
                deals.extend([Deal(**deal)
                              for deal in page_deals])
        elif 1 <= page <= total_pages:
            # Fetch specified page
            page_deals = self._api._get(
                url + f"?page={page}&per_page={per_page}").get('deals', [])
            deals = [Deal(**deal) for deal in page_deals]
        return deals

    def update_deal(self, deal_id, **data):
        url = f'/deals/{deal_id}'
        response = self._api._put(url, data=json.dumps(data))
        return Deal(**response.get('deal', {}))

    def upsert_deal(self, unique_identifier, **deal_properties):
        url = '/deals/upsert'
        unique_field_name, unique_field_value = unique_identifier
        unique_identifier = {unique_field_name: unique_field_value}
        data = {
            'unique_identifier': unique_identifier,
            'deal': deal_properties
        }
        response = self._api._post(url, data=json.dumps(data))
        return Deal(**response.get('deal', {}))

    def clone_deal(self, deal_id, **data):
        url = f'/deals/{deal_id}/clone'
        payload = {'deal': data} if data else {}
        deal = self._api._post(url, data=json.dumps(payload))
        return Deal(**deal.get('deal', {}))

    def delete_deal(self, deal_id):
        url = f'/deals/{deal_id}'
        return self._api._delete(url)

    def forget_deal(self, deal_id):
        url = f'/deals/{deal_id}/forget'
        return self._api._delete(url)

    def list_fields(self, include_groups=False):
        url = '/settings/deals/fields'
        url += '?include=field_group' if include_groups else ''
        response = self._api._get(url)
        return [Field(**field) for field in response.get('fields', [])]


class NoteAPI(object):
    def __init__(self, api):
        self._api = api

    def create_note(self, **note_properties):
        url = '/notes'
        data = {'note': note_properties}
        response = self._api._post(url, data=json.dumps(data))
        return Note(**response.get('note', {}))

    def update_note(self, note_id, **note_properties):
        url = f'/notes/{note_id}'
        data = {'note': note_properties}
        response = self._api._put(url, data=json.dumps(data))
        return Note(**response.get('note', {}))

    def delete_note(self, note_id):
        url = f'/notes/{note_id}'
        return self._api._delete(url).get('success') == "200"


class TaskAPI(object):
    def __init__(self, api):
        self._api = api

    def create_task(self, **kwargs):
        url = '/tasks'
        data = kwargs.copy()
        response = self._api._post(url, data=json.dumps(data))
        return Task(**response.get('task', {}))

    def view_task(self, task_id, *include):
        url = f'/tasks/{task_id}'
        url += f'?include={",".join(include)}' if include else ''
        response = self._api._get(url)
        if response.get('contacts'):
            response['contacts'] = [Contact(**contact)
                                    for contact in response['contacts']]
        if response.get('users'):
            response['users'] = [User(**user) for user in response['users']]
        if response.get('task'):
            response['task'] = Task(**response['task'])
        if response.get('sales_accounts'):
            response['sales_accounts'] = [Account(**account)
                                          for account in response['sales_accounts']]
        if response.get('deals'):
            response['deals'] = Deal(**response['deal'])
        return response

    def list_tasks(self, filter_param, *include, page=None, per_page=100):
        url = f'/tasks?filter={filter_param}'
        url += f'&include={",".join(include)}' if include else ''

        tasks = self._api._get(url)

        if not tasks.get("tasks"):
            return tasks

        task_objects = {
            'contacts': Contact,
            'users': User,
            'tasks': Task,
            'sales_accounts': Account,
            'deals': Deal
        }

        for key, obj in task_objects.items():
            if tasks.get(key):
                tasks[key] = [obj(**item) for item in tasks[key]]

        total_pages = tasks.get('meta', {}).get('total_pages', 1)

        # in case pagination is required (not tested)
        if page is None:
            # Fetch all pages
            for current_page in range(2, total_pages + 1):
                page_tasks = self._api._get(
                    url + f"?page={current_page}&per_page={per_page}").get('tasks', [])
                tasks['tasks'].extend([Task(**task) for task in page_tasks])
        elif 1 <= page <= total_pages:
            # Fetch specified page
            page_tasks = self._api._get(
                url + f"?page={page}&per_page={per_page}").get('tasks', [])
            tasks['tasks'] = [Task(**task) for task in page_tasks]

        return tasks

    def update_task(self, task_id, **kwargs):
        url = f'/tasks/{task_id}'
        data = {'task': kwargs}
        response = self._api._put(url, data=json.dumps(data))
        return Task(**response.get('task', {}))

    def mark_as_done(self, task_id):
        url = f'/tasks/{task_id}'
        data = {"task": {"status": 1}}
        response = self._api._put(url, data=json.dumps(data))
        return Task(**response.get('task', {}))

    def delete_task(self, task_id):
        url = f'/tasks/{task_id}'
        return self._api._delete(url).get('success') == "200"


class AppointmentAPI(object):
    def __init__(self, api):
        self._api = api

    def create_appointment(self, **kwargs):
        url = '/appointments'
        data = kwargs.copy()
        response = self._api._post(url, data=json.dumps(data))
        response['appointment'] = Appointment(**response['appointment'])
        response['notes'] = [Note(**note) for note in response['notes']]
        return response

    def view_appointment(self, appointment_id):
        url = f'/appointments/{appointment_id}'
        response = self._api._get(url)
        response['appointment'] = Appointment(**response['appointment'])
        response['notes'] = [Note(**note) for note in response['notes']]
        return response

    def list_appointments(self, filter_param, *include, page=None, per_page=100):
        url = f'/appointments?filter={filter_param}'
        url += f'&include={",".join(include)}' if include else ''

        response = self._api._get(url)
        total_pages = response.get('meta', {}).get('total_pages', 1)
        appointments = response.get('appointments', [])

        # in case pagination is required (not tested)
        if page is None:
            # Fetch all pages
            appointments = [Appointment(**appointment)
                            for appointment in appointments]
            for current_page in range(2, total_pages + 1):
                page_appointments = self._api._get(
                    url + f"?page={current_page}&per_page={per_page}").get('appointments', [])
                appointments['appointments'].extend(
                    [Appointment(**appointment) for appointment in page_appointments])
        elif 1 <= page <= total_pages:
            # Fetch specified page
            page_appointments = self._api._get(
                url + f"?page={page}&per_page={per_page}").get('appointments', [])
            appointments['appointments'] = [Appointment(
                **appointment) for appointment in page_appointments]

        return appointments

    def update_appointment(self, appointment_id, **kwargs):
        url = f'/appointments/{appointment_id}'
        response = self._api._put(
            url, data=json.dumps({'appointment': kwargs}))
        response['appointment'] = Appointment(**response['appointment'])
        response['notes'] = [Note(**note) for note in response['notes']]
        return response

    def delete_appointment(self, appointment_id):
        url = f'/appointments/{appointment_id}'
        return self._api._delete(url).get('success') == "200"


class SalesActivityAPI(object):
    def __init__(self, api):
        self._api = api

    def create_activity(self, **kwargs):
        url = '/sales_activities'
        data = {'sales_activity': kwargs}
        response = self._api._post(url, data=json.dumps(data))
        return SalesActivity(**response.get('sales_activity', {}))

    def view_activity(self, sales_activity_id):
        url = f'/sales_activities/{sales_activity_id}'
        response = self._api._get(url)
        return SalesActivity(**response.get('sales_activity', {}))

    def list_activities(self, page=None, per_page=10):
        url = '/sales_activities'
        response = self._api._get(url)

        sales_activities = response.get('sales_activities', [])
        total_pages = response.get('meta', {}).get('total_pages', 1)

        # In case pagination is required
        if page is None:
            # Fetch all pages
            sales_activities = [SalesActivity(**activity)
                                for activity in sales_activities]
            for current_page in range(2, total_pages + 1):
                page_sales_activities = self._api._get(
                    url + f"?page={current_page}&per_page={per_page}").get('sales_activities', [])
                sales_activities.extend(
                    [SalesActivity(**activity) for activity in page_sales_activities])
        elif 1 <= page <= total_pages:
            # Fetch specified page
            page_sales_activities = self._api._get(
                url + f"?page={page}&per_page={per_page}").get('sales_activities', [])
            sales_activities = [SalesActivity(
                **activity) for activity in page_sales_activities]

        return sales_activities

    def list_fields(self):
        url = '/settings/sales_activities/fields'
        response = self._api._get(url)
        return [Field(**field) for field in response.get('fields', [])]

    def update_activity(self, sales_activity_id, **kwargs):
        url = f'/sales_activities/{sales_activity_id}'
        data = {'sales_activity': kwargs}
        response = self._api._put(url, data=json.dumps(data))
        return SalesActivity(**response.get('sales_activity', {}))

    def delete_activity(self, sales_activity_id):
        url = f'/sales_activities/{sales_activity_id}'
        return self._api._delete(url).get('success') == "200"


class ProductAPI(object):
    def __init__(self, api):
        self._api = api

    def create_product(self, **kwargs):
        url = f'/cpq/products'
        data = {'product': kwargs}
        response = self._api._post(url, data=json.dumps(data))
        return Product(**response.get('product', {}))

    def view_product(self, product_id):
        url = f'/cpq/products/{product_id}'
        response = self._api._get(url)
        return Product(**response.get('product', {}))

    def update_product(self, product_id, **kwargs):
        url = f'/cpq/products/{product_id}'
        data = {'product': kwargs}
        response = self._api._put(url, data=json.dumps(data))
        return Product(**response.get('product', {}))

    def delete_product(self, product_id):
        url = f'/cpq/products/{product_id}'
        return self._api._delete(url).get('success') == "200"

    def restore_product(self, product_id):
        url = f'/cpq/products/{product_id}/restore'
        response = self._api._put(url)
        return Product(**response.get('product', {}))

    def add_product_prices(self, product_id, pricing_type, product_pricings):
        url = f'/cpq/products/{product_id}?include=product_pricings'
        data = {
            'product': {
                'pricing_type': pricing_type,
                'product_pricings': product_pricings
            }
        }
        response = self._api._put(url, data=json.dumps(data))
        return Product(**response.get('product', {}))

    def edit_product_prices(self, product_id, product_pricings):
        url = f'/cpq/products/{product_id}?include=product_pricings'
        data = {'product': {'product_pricings': product_pricings}}
        response = self._api._put(url, data=json.dumps(data))
        return Product(**response.get('product', {}))

    def delete_product_prices(self, product_id, price_ids):
        url = f'/cpq/products/{product_id}?include=product_pricings'
        data = {
            'product': {
                'product_pricings': [
                    {'id': price_id, '_destroy': True} for price_id in price_ids
                ]
            }
        }
        response = self._api._put(url, data=json.dumps(data))
        return Product(**response.get('product', {}))

    def add_products_to_deal(self, deal_id, products):
        url = f'/deals/{deal_id}?include=products'
        data = {'deal': {'products': products}}
        response = self._api._put(url, data=json.dumps(data))
        response['deal']['products'] = [
            Product(**product) for product in response['deal']['products']]
        return Deal(**response.get('deal', {}))

    def edit_deal_products(self, deal_id, products):
        url = f'/deals/{deal_id}'
        data = {'deal': {'products': products}}
        response = self._api._put(url, data=json.dumps(data))
        response['deal']['products'] = [
            Product(**product) for product in response['deal']['products']]
        return Deal(**response.get('deal', {}))

    def delete_all_deal_products(self, deal_id):
        url = f'/deals/{deal_id}?include=products'
        data = {'deal': {'products': []}}
        response = self._api._put(url, data=json.dumps(data))
        return Deal(**response.get('deal', {}))


class DocumentAPI(object):
    def __init__(self, api):
        self._api = api

    def create_document(self, **kwargs):
        url = '/cpq/cpq_documents'
        data = {'cpq_document': kwargs}
        response = self._api._post(url, data=json.dumps(data))
        return Document(**response.get('cpq_document', {}))

    def view_document(self, document_id, include=None):
        url = f'/cpq/cpq_documents/{document_id}'
        if include:
            url += f'?include={include}'
        response = self._api._get(url)
        return Document(**response.get('cpq_document', {}))

    def update_document(self, document_id, **kwargs):
        url = f'/cpq/cpq_documents/{document_id}'
        data = {'cpq_document': kwargs}
        response = self._api._put(url, data=json.dumps(data))
        return Document(**response.get('cpq_document', {}))

    def delete_document(self, document_id):
        url = f'/cpq/cpq_documents/{document_id}'
        response = self._api._delete(url)
        return response.get('msg', {}).get('code') == 'success'

    def restore_document(self, document_id):
        url = f'/cpq/cpq_documents/{document_id}/restore'
        response = self._api._put(url)
        return Document(**response.get('cpq_document', {}))

    def forget_document(self, document_id):
        url = f'/cpq/cpq_documents/{document_id}/forget'
        response = self._api._delete(url)
        return response.get('msg', {}).get('code') == 'success'

    def add_products_to_document(self, document_id, products):
        url = f'/cpq/cpq_documents/{document_id}?include=products'
        data = {'cpq_document': {'products': products}}
        response = self._api._put(url, data=json.dumps(data))
        response['cpq_document']['products'] = [
            Product(**product) for product in response['cpq_document']['products']]
        return Document(**response.get('cpq_document', {}))

    def edit_products_of_document(self, document_id, products):
        url = f'/cpq/cpq_documents/{document_id}?include=products'
        data = {'cpq_document': {'products': products}}
        response = self._api._put(url, data=json.dumps(data))
        response['cpq_document']['products'] = [
            Product(**product) for product in response['cpq_document']['products']]
        return Document(**response.get('cpq_document', {}))

    def delete_products_from_document(self, document_id):
        url = f'/cpq/cpq_documents/{document_id}?include=products'
        data = {'cpq_document': {'products': []}}
        response = self._api._put(url, data=json.dumps(data))
        return Document(**response.get('cpq_document', {}))

    def get_related_products(self, document_id):
        url = f'/cpq/cpq_documents/{document_id}/related_products'
        response = self._api._get(url)
        return [Product(**product) for product in response.get('products', [])]


class SelectorAPI(object):
    def __init__(self, api):
        self._api = api

    def get_users(self):
        url = '/selector/owners'
        response = self._api._get(url)
        return [User(**user) for user in response.get('users', [])]

    def get_territories(self):
        url = '/selector/territories'
        response = self._api._get(url)
        return [Territory(**territory) for territory in response.get('territories', [])]

    def get_deal_stages(self):
        url = '/selector/deal_stages'
        response = self._api._get(url)
        return [DealStage(**deal_stage) for deal_stage in response.get('deal_stages', [])]

    def get_currencies(self):
        url = '/selector/currencies'
        response = self._api._get(url)
        return [Currency(**currency) for currency in response.get('currencies', [])]

    def get_deal_reasons(self):
        url = '/selector/deal_reasons'
        response = self._api._get(url)
        return [DealReason(**deal_reason) for deal_reason in response.get('deal_reasons', [])]

    def get_deal_types(self):
        url = '/selector/deal_types'
        response = self._api._get(url)
        return [DealType(**deal_type) for deal_type in response.get('deal_types', [])]

    def get_lead_sources(self):
        url = '/selector/lead_sources'
        response = self._api._get(url)
        return [LeadSource(**lead_source) for lead_source in response.get('lead_sources', [])]

    def get_industry_types(self):
        url = '/selector/industry_types'
        response = self._api._get(url)
        return [IndustryType(**industry_type) for industry_type in response.get('industry_types', [])]

    def get_business_types(self):
        url = '/selector/business_types'
        response = self._api._get(url)
        return [BusinessType(**business_type) for business_type in response.get('business_types', [])]

    def get_campaigns(self):
        url = '/selector/campaigns'
        response = self._api._get(url)
        return [Campaign(**campaign) for campaign in response.get('campaigns', [])]

    def get_deal_payment_statuses(self):
        url = '/selector/deal_payment_statuses'
        response = self._api._get(url)
        return [DealPaymentStatus(**deal_payment_status) for deal_payment_status in response.get('deal_payment_statuses', [])]

    def get_deal_prodcuts(self):
        url = '/selector/deal_products'
        response = self._api._get(url)
        return [DealProduct(**deal_product) for deal_product in response.get('deal_products', [])]

    def get_deal_pipelines(self):
        url = '/selector/deal_pipelines'
        response = self._api._get(url)
        pipelines = [DealPipeline(**deal_pipeline)
                     for deal_pipeline in response.get('deal_pipelines', [])]
        for pipeline in pipelines:
            pipeline.deal_stages = [
                DealStage(**deal_stage) for deal_stage in pipeline.deal_stages]
        return pipelines

    def get_deal_pipeline_stages(self, pipeline_id):
        url = f'/selector/deal_pipelines{pipeline_id}/deal_stages'
        response = self._api._get(url)
        return [DealStage(**deal_stage) for deal_stage in response.get('deal_stages', [])]

    def get_contact_statuses(self):
        url = '/selector/contact_statuses'
        response = self._api._get(url)
        return [ContactStatus(**contact_status) for contact_status in response.get('contact_statuses', [])]

    def get_sales_activity_types(self):
        url = '/selector/sales_activity_types'
        response = self._api._get(url)
        return [SalesActivityType(**sales_activity_type) for sales_activity_type in response.get('sales_activity_types', [])]

    def get_sales_activity_entity_types(self):
        url = '/selector/sales_activity_entity_types'
        response = self._api._get(url)
        return [SalesActivityEntityType(**sales_activity_entity_type) for sales_activity_entity_type in response.get('sales_activity_entity_types', [])]

    def get_sales_activity_outcomes(self):
        url = '/selector/sales_activity_outcomes'
        response = self._api._get(url)
        return [SalesActivityOutcome(**sales_activity_outcome) for sales_activity_outcome in response.get('sales_activity_outcomes', [])]

    def get_sales_activity_type_outcomes(self, type_id):
        url = f'/selector/sales_activity_types/{type_id}/sales_activity_outcomes'
        response = self._api._get(url)
        return [SalesActivityOutcome(**sales_activity_entity_outcome) for sales_activity_entity_outcome in response.get('sales_activity_outcomes', [])]

    def get_lifecycle_stages(self):
        url = '/selector/lifecycle_stages'
        response = self._api._get(url)
        return [LifecycleStage(**lifecycle_stage) for lifecycle_stage in response.get('lifecycle_stages', [])]

class SearchAPI(object):
    def __init__(self, api):
        self._api = api

    def filter_contacts(self, filter_rules, page=None, per_page=100):
        url = '/filtered_search/contact'

        # Prepare filter rules for data payload
        data_rules = [{'attribute': rule['attribute'], 
                    'operator': rule['operator'], 
                    'value': rule['value']} for rule in filter_rules]
        
        data = {'filter_rule': data_rules}

        response = self._api._post(url, data=json.dumps(data))
        print(response)

        total_pages = response.get('meta', {}).get('total_pages', 1)
        contacts = response.get('contacts', [])

        if page is None:
            # Fetch all pages
            contacts = [Contact(**contact) for contact in contacts]
            for current_page in range(2, total_pages + 1):
                page_contacts = self._api._get(
                    url + f"?page={current_page}&per_page={per_page}").get('contacts', [])
                contacts.extend([Contact(**contact)
                                for contact in page_contacts])
        elif 1 <= page <= total_pages:
            # Fetch specified page
            page_contacts = self._api._get(
                url + f"?page={page}&per_page={per_page}").get('contacts', [])
            contacts = [Contact(**contact) for contact in page_contacts]

        return contacts

class API(object):

    def __init__(self, domain, api_key):
        self._session = self._create_session(api_key)
        self.contacts = ContactAPI(self)
        self.lists = ListAPI(self)
        self.accounts = AccountAPI(self)
        self.deals = DealAPI(self)
        self.notes = NoteAPI(self)
        self.tasks = TaskAPI(self)
        self.appointments = AppointmentAPI(self)
        self.sales_activities = SalesActivityAPI(self)
        self.products = ProductAPI(self)
        self.documents = DocumentAPI(self)
        self.search = SearchAPI(self)
        # self.phones = PhoneAPI(self)
        # self.files = FileAPI(self)
        # self.job_statuses = JobStatusAPI(self)
        # self.custom_modules = CustomModuleAPI(self)

        self.selectors = SelectorAPI(self)
        self._api_prefix = f"https://{domain.rstrip('/')}/api/".rstrip('/')

    def _create_session(self, api_key):
        session = requests.Session()
        session.headers.update({"Authorization": f"Token token={api_key}",
                                "Content-Type": "application/json"})
        session.params = {}
        return session

    def _action(self, req):

        try:
            j = req.json()
        except ValueError:
            j = {}

        if type(j) == bool:
            return j

        error_message = "Freshsales Request Failed"
        if "errors" in j:
            error_message = f"{j.get('description')}: {j.get('errors')}"
        elif "message" in j:
            error_message = j['message']

        if req.status_code == 400:
            raise FreshsalesBadRequest(error_message)
        elif req.status_code == 401:
            raise FreshsalesUnauthorized(error_message)
        elif req.status_code == 403:
            raise FreshsalesAccessDenied(error_message)
        elif req.status_code == 404:
            raise FreshsalesNotFound(error_message)
        elif req.status_code == 429:
            raise FreshsalesRateLimited(
                f"429 Rate Limit Exceeded: API rate-limit has been reached until {req.headers.get('Retry-After')} seconds."
            )
        elif 500 < req.status_code < 600:
            raise FreshsalesServerError(f"{req.status_code}: Server Error")

        # Catch any other errors
        try:
            req.raise_for_status()
        except HTTPError as e:
            raise FreshsalesError(f"{e}: {j}")

        return j

    def _get(self, url, params={}):
        """Wrapper around request.get() to use the API prefix. Returns a JSON response."""
        req = self._session.get(self._api_prefix + url, params=params)
        return self._action(req)

    def _post(self, url, data={}, **kwargs):
        """Wrapper around request.post() to use the API prefix. Returns a JSON response."""
        req = self._session.post(self._api_prefix + url, data=data, **kwargs)
        return self._action(req)

    def _put(self, url, data={}):
        """Wrapper around request.put() to use the API prefix. Returns a JSON response."""
        req = self._session.put(self._api_prefix + url, data=data)
        if req.status_code == 204:
            return True
        return self._action(req)

    def _delete(self, url):
        """Wrapper around request.delete() to use the API prefix. Returns a JSON response."""
        req = self._session.delete(self._api_prefix + url)
        return self._action(req)
