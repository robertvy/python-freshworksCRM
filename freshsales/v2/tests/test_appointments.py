import datetime

import pytest

from freshsales.v2.models import Appointment


@pytest.fixture
def appointment(api):
    return api.appointments.view_appointment(31001473829).get('appointment')


def test_create_appointment(api):
    response = api.appointments.create_appointment(
        title='Sample Appointment',
        description='This is just a sample Appointment.',
        from_date='Mon Jun 20 2016 10:30:00 GMT+0530 (IST)',
        end_date='Mon Jun 20 2016 11:30:00 GMT+0530 (IST)',
        creater_id=31000148397,
        time_zone='Chennai',
        location='Chennai, TN, India',
        targetable_id=31016358306,
        targetable_type='Contact')

    appointment = response.get('appointment')

    assert isinstance(appointment, Appointment)
    assert appointment.title == "Sample Appointment"
    assert appointment.description == "This is just a sample Appointment."
    assert isinstance(appointment.from_date, datetime.datetime)
    assert isinstance(appointment.end_date, datetime.datetime)


def test_view_apppointment(appointment):
    assert isinstance(appointment, Appointment)
    assert appointment.title == "Sample Appointment"
    assert appointment.description == "This is just a sample Appointment."
    assert isinstance(appointment.from_date, datetime.datetime)
    assert isinstance(appointment.end_date, datetime.datetime)


def test_list_all_appointments(api):
    appointments = api.appointments.list_all_appointments("upcoming")

    if appointments:
        appointment = appointments[1]
        assert isinstance(appointment, Appointment)
        assert appointment.title == "(Sample) Meeting - final discussion about the deal"
        assert isinstance(appointment.from_date, datetime.datetime)
        assert isinstance(appointment.end_date, datetime.datetime)


def test_update_appointment(api):
    response = api.appointments.update_appointment(
        31001473829, title='Updated Appointment')
    appointment = response.get('appointment')
    assert isinstance(appointment, Appointment)
    assert appointment.title == "Updated Appointment"
    assert appointment.description == "This is just a sample Appointment."
    assert isinstance(appointment.from_date, datetime.datetime)
    assert isinstance(appointment.end_date, datetime.datetime)


def test_delete_appointment(api):
    assert api.appointments.delete_appointment(31001473829) is True


def test_appointment_str(appointment):
    assert str(
        appointment) == "Sample Appointment"


def test_appointment_repr(appointment):
    assert repr(
        appointment) == "<Appointment 'Sample Appointment' #31001473829>"
