from google.cloud import bigquery, monitoring_v3, billing_v1
# Remove unavailable imports
# from google.cloud import logging_v2, resourcemanager_v3
from google.auth.exceptions import DefaultCredentialsError
from google.api_core.exceptions import GoogleAPIError
import os
