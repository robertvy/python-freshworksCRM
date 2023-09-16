from freshsales.api import API
import pytest
import json
import os.path
import re

DOMAIN = 'apiwrapperinc.myfreshworks.com/crm/sales'
API_KEY = 'AIaj6VTSzNm0hoNdzTSJUg'


def read_test_file(filename):
    """
    Helper function to read JSON data from a file.
    """
    path = os.path.join(os.path.dirname(__file__),
                        "sample_json_data", filename)
    return json.loads(open(path, "r").read())


def read_first_from_test_file(filename, key=None):
    """
    Helper function to read the first object from a JSON file.
    """
    path = os.path.join(os.path.dirname(__file__),
                        "sample_json_data", filename)
    all_objs = json.loads(open(path, "r").read())
    if key:
        return all_objs.get(key)[0]
    return all_objs


@pytest.fixture()
def api(mocker):
    """
    This fixture mocks the API object's internal methods with mocked data.
    """
    # Create a new API object.
    api = API(DOMAIN, API_KEY)

    # Define the resolver containing the mocked data.
    def get_data(pair):
        return re.compile(pair[0]), read_test_file(pair[1])

    resolver_raw = {
        "get": [
            (r"/contacts/31016358306", "contact.json"),
            (r"/contacts/filters", "contact_views.json"),
            (r"/settings/contacts/fields", "contact_fields.json"),
            (r"/contacts/view", "contacts.json"),
            (r"/settings/sales_accounts/fields", "account_fields.json"),
            (r"/sales_accounts/filters", "account_views.json"),
            (r"/sales_accounts/view", "accounts.json"),
            (r"/sales_accounts", "account.json"),
            (r"/deals/31003638276", "deal.json"),
            (r"/deals/filters", "deal_views.json"),
            (r"/deals/view", "deals.json"),
            (r"/settings/deals/fields", "deal_fields.json"),
            (r"/contacts/lists", "list_fetch_contact.json"),
            (r"/lists", "lists.json"),
            (r"/selector/owners", "selectors_users.json"),
            (r"/selector/territories", "selectors_territories.json"),
            (r"/selector/deal_stages", "selectors_deal_stages.json"),
            (r"/selector/currencies", "selectors_currencies.json"),
            (r"/selector/deal_reasons", "selectors_deal_reasons.json"),
            (r"/selector/deal_types", "selectors_deal_types.json"),
            (r"/selector/lead_sources", "selectors_lead_sources.json"),
            (r"/selector/industry_types", "selectors_industry_types.json"),
            (r"/selector/business_types", "selectors_business_types.json"),
            (r"/selector/deal_payment_statuses",
             "selectors_deal_payment_statuses.json"),
            (r"/selector/deal_pipelines", "selectors_deal_pipelines.json"),
            (r"/selector/contact_statuses", "selectors_contact_statuses.json"),
            (r"/selector/sales_activity_entity_types",
             "selectors_sales_activity_entity_types.json"),
            (r"/selector/sales_activity_types/31000477933/sales_activity_outcomes",
             "selectors_sales_activity_types_outcomes.json"),
            (r"/selector/sales_activity_outcomes",
             "selectors_sales_activity_outcomes.json"),
            (r"/selector/sales_activity_types",
             "selectors_sales_activity_types.json"),
            (r"/selector/lifecycle_stages", "selectors_lifecycle_stages.json"),
            (r"/tasks\?filter", "tasks.json"),
            (r"/tasks", "task_view.json"),
            (r"/appointments\?filter", "appointments.json"),
            (r"/appointments", "appointment.json"),
            (r"/sales_activities/", "sales_activity.json"),
            (r"/sales_activities", "sales_activities.json"),
            (r"/settings/sales_activities/fields", "sales_activity_fields.json"),
            (r"/cpq/cpq_documents/31000039151/related_products", "document_related_products.json"),
            (r"/cpq/products", "product_updated.json"),
            (r"/cpq/cpq_documents", "document.json"),
        ],
        "post": [
            (r"/contacts/31016358306/clone", "contact_updated.json"),
            (r"/contacts", "contact.json"),
            (r"/sales_accounts", "account.json"),
            (r"/deals", "deal.json"),
            (r"/lists", "list.json"),
            (r"/notes", "note.json"),
            (r"/tasks", "task.json"),
            (r"/appointments", "appointment.json"),
            (r"/sales_activities", "sales_activity.json"),
            (r"/cpq/products", "product_updated.json"),
            (r"/cpq/cpq_documents", "document.json"),
            (r"/filtered_search/contact", "filter_contacts.json"),
        ],
        "put": [
            (r"/lists/31000045351/remove_contacts", "list_message.json"),
            (r"/lists/31000045351/move_contacts", "list_message.json"),
            (r"/contacts", "contact_updated.json"),
            (r"/sales_accounts", "account_updated.json"),
            (r"/deals/31001944158", "product_deal.json"),
            (r"/deals/31001944160", "product_deal_deleted.json"),
            (r"/deals", "deal_updated.json"),
            (r"/lists/31000045356/add_contacts", "list_message.json"),
            (r"/lists", "list_updated.json"),
            (r"/notes", "note_updated.json"),
            (r"/tasks", "task_updated.json"),
            (r"/appointments", "appointment_updated.json"),
            (r"/sales_activities", "sales_activity_updated.json"),
            (r"/cpq/products/31000985829\?include", "product_pricing.json"),
            (r"/cpq/products/31000985854\?include", "product_pricing_deleted.json"),
            (r"/cpq/products", "product_updated.json"),
            (r"/cpq/cpq_documents/31000039151\?include", "document_product.json"),
            (r"/cpq/cpq_documents/31000039150\?include", "document_product_delete.json"),
            (r"/cpq/cpq_documents", "document_updated.json"),
        ],
        "delete": [
            (r"/contacts", "deleted.json"),
            (r"/sales_accounts", "deleted.json"),
            (r"/deals", "deleted.json"),
            (r"/notes", "deleted_200.json"),
            (r"/tasks", "deleted_200.json"),
            (r"/appointments", "deleted_200.json"),
            (r"/sales_activities", "deleted_200.json"),
            (r"/cpq/products", "deleted_200.json"),
            (r"/cpq/cpq_documents", "delete_success.json"),
        ],
    }

    resolver = {method: dict(get_data(pair) for pair in pairs)
                for method, pairs in resolver_raw.items()}

    # Helper function to handle the mocked API calls.
    def mocked_api_call(method, url, *args, **kwargs):
        """
        Iterate through the resolver's items for the specified method.
        Check if the pattern matches the requested URL.
        Return the corresponding mocked data.
        If no match is found, raise a 404 error.
        """
        for pattern, data in resolver[method].items():
            if pattern.match(url):
                return data
        from requests.exceptions import HTTPError
        raise HTTPError(
            f"404: mocked_api_call() has no pattern for '{url}'")

    # Patch the API object's internal methods to use the mocked data.
    mocker.patch.object(api, '_get', side_effect=lambda url, *args,
                        **kwargs: mocked_api_call("get", url, *args, **kwargs))
    mocker.patch.object(api, '_post', side_effect=lambda url, *args,
                        **kwargs: mocked_api_call("post", url, *args, **kwargs))
    mocker.patch.object(api, '_put', side_effect=lambda url, *args,
                        **kwargs: mocked_api_call("put", url, *args, **kwargs))
    mocker.patch.object(api, '_delete', side_effect=lambda url, *args,
                        **kwargs: mocked_api_call("delete", url, *args, **kwargs))

    # Return the mocked API object.
    return api
