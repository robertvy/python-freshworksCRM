import dateutil.parser


class FreshsalesModel(object):
    _keys = None

    def __init__(self, **kwargs):
        self._keys = set()

        if "custom_field" in kwargs.keys() and len(kwargs["custom_field"]) > 0:
            custom_fields = kwargs.pop("custom_field")
            kwargs.update(custom_fields)
        for k, v in kwargs.items():
            if hasattr(Contact, k):
                k = "_" + k
            setattr(self, k, v)
            self._keys.add(k)

        timestamp_fields = [
            "created_at",
            "updated_at",
            "due_date",
            "stage_updated_time",
            "last_assigned_at",
            "last_contacted",
            "last_contacted_via_sales_activity",
            "from_date",
            "end_date",
            "start_date",
        ]

        for field in timestamp_fields:
            if field in kwargs:
                setattr(self, field, self._to_timestamp(getattr(self, field)))

    def _to_timestamp(self, timestamp_str):
        """Converts a timestamp string as returned by the API to
        a native datetime object and return it."""
        if timestamp_str is None:
            return None
        return dateutil.parser.parse(timestamp_str)


class Contact(FreshsalesModel):
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"<Contact '{self.first_name} {self.last_name}' #{self.id}>"


class List(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<List '{self.name}' #{self.id}>"


class Account(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Account '{self.name}' #{self.id}>"


class Deal(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Deal '{self.name}' #{self.id}>"


class Note(FreshsalesModel):
    def __str__(self):
        return f"{self.description}"

    def __repr__(self):
        return f"<Note '{self.description}' #{self.id}>"


class Task(FreshsalesModel):
    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"<Task '{self.title}' #{self.id}>"


class Appointment(FreshsalesModel):
    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"<Appointment '{self.title}' #{self.id}>"


class SalesActivity(FreshsalesModel):
    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"<SalesActivity '{self.title}' #{self.id}>"


class Product(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Product '{self.name}' #{self.id}>"


class Document(FreshsalesModel):
    def __str__(self):
        return f"{self.display_name}"

    def __repr__(self):
        return f"<Document '{self.display_name}' #{self.id}>"


class Field(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Field '{self.name}' #{self.id}>"


class View(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Filter '{self.name}' #{self.id}>"


class User(FreshsalesModel):
    def __str__(self):
        return f"{self.display_name}"

    def __repr__(self):
        return f"<User '{self.display_name}' #{self.id}>"


class Territory(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Territory '{self.name}' #{self.id}>"


class DealStage(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<DealStage '{self.name}' #{self.id}>"


class Currency(FreshsalesModel):
    def __str__(self):
        return f"{self.currency_code}"

    def __repr__(self):
        return f"<Currency '{self.currency_code}' #{self.id}>"


class DealReason(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<DealReason '{self.name}' #{self.id}>"


class DealType(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<DealType '{self.name}' #{self.id}>"


class LeadSource(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<LeadSource '{self.name}' #{self.id}>"


class IndustryType(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<IndustryType '{self.name}' #{self.id}>"


class BusinessType(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<BusinessType '{self.name}' #{self.id}>"


class Campaign(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Campaign '{self.name}' #{self.id}>"


class DealPaymentStatus(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<DealPaymentStatus '{self.name}' #{self.id}>"


class DealProduct(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<DealProduct '{self.name}' #{self.id}>"


class DealPipeline(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<DealPipeline '{self.name}' #{self.id}>"


class ContactStatus(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<ContactStatus '{self.name}' #{self.id}>"


class SalesActivityType(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<SalesActivityType '{self.name}' #{self.id}>"


class SalesActivityOutcome(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<SalesActivityOutcome '{self.name}' #{self.id}>"


class SalesActivityEntityType(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<SalesActivityEntityType '{self.name}' #{self.id}>"


class LifecycleStage(FreshsalesModel):
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<LifecycleStage '{self.name}' #{self.id}>"
