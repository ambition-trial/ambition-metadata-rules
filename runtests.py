#!/usr/bin/env python
import django
import logging
import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings
from os.path import abspath, dirname, join


app_name = 'ambition_metadata_rules'
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ETC_DIR=os.path.join(base_dir, app_name, "tests", "etc"),
    SUBJECT_CONSENT_MODEL="ambition_subject.subjectconsent",
    SUBJECT_VISIT_MODEL="ambition_subject.subjectvisit",
    SUBJECT_REQUISITION_MODEL="ambition_subject.subjectrequisition",
    RANDOMIZATION_LIST_PATH=join(
        base_dir, app_name, "tests", "test_randomization_list.csv"),
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django_crypto_fields.apps.AppConfig',
        'django_revision.apps.AppConfig',
        'edc_action_item.apps.AppConfig',
        'edc_appointment.apps.AppConfig',
        'edc_base.apps.AppConfig',
        'edc_lab.apps.AppConfig',
        'edc_visit_tracking.apps.AppConfig',
        'edc_visit_schedule.apps.AppConfig',
        'edc_identifier.apps.AppConfig',
        'edc_device.apps.AppConfig',
        'edc_offstudy.apps.AppConfig',
        'edc_protocol.apps.AppConfig',
        'edc_registration.apps.AppConfig',
        'edc_reference.apps.AppConfig',
        'edc_metadata_rules.apps.AppConfig',
        'edc_notification.apps.AppConfig',
        'ambition_labs.apps.AppConfig',
        'ambition_lists.apps.AppConfig',
        'ambition_reference.apps.AppConfig',
        'ambition_prn.apps.AppConfig',
        'ambition_rando.apps.AppConfig',
        'ambition_visit_schedule.apps.AppConfig',
        'ambition_screening.apps.AppConfig',
        'ambition_subject.apps.AppConfig',
        'ambition_metadata_rules.apps.EdcFacilityAppConfig',
        'ambition_metadata_rules.apps.EdcMetadataAppConfig',
        'ambition_metadata_rules.apps.AppConfig',
    ],
    add_dashboard_middleware=True,
    add_lab_dashboard_middleware=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    failures = DiscoverRunner(failfast=True).run_tests(
        [f'{app_name}.tests'])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()