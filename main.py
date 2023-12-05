from visma.api import VismaAPI
from bigquery.api import BigQueryApi, WriteDisposition
from visma.models.accounts import bq_schema as accounts_bq_schema
from visma.models.account_types import bq_schema as account_types_bq_schema
from visma.models.article_account_codings import bq_schema as article_account_codings_bq_schema
from visma.models.article_labels import bq_schema as article_labels_bq_schema
from visma.models.articles import bq_schema as articles_bq_schema
from visma.models.customer_invoices import bq_schema as customer_invoices_bq_schema
from visma.models.customer_labels import bq_schema as customer_labels_bq_schema
from visma.models.orders import bq_schema as orders_bq_schema
from visma.models.supplier_invoices import bq_schema as supplier_invoices_bq_schema

from storage.api import LocalStorage, GoogleCloudStorage

import os

def run():
    PROJECT_ID = os.environ.get('PROJECT_ID')
    DATASET_ID = os.environ.get('DATASET_ID')
    TABLE_ID = os.environ.get('TABLE_ID')
    TABLE_WRITE_METHOD = os.environ.get("TABLE_WRITE_METHOD")
    if TABLE_WRITE_METHOD not in WriteDisposition.__dict__.keys():
        TABLE_WRITE_METHOD = WriteDisposition.WRITE_APPEND
    
    API_CLIENT_ID = os.environ.get('API_CLIENT_ID')
    API_CLIENT_SECRET = os.environ.get('API_CLIENT_SECRET')
    API_TOKEN_STORAGE = os.environ.get('API_TOKEN_STORAGE')
    API_TOKEN_PATH = os.environ.get('API_TOKEN_PATH')
    API_ENDPOINT = os.getenv("API_ENDPOINT")

    if(API_TOKEN_STORAGE == 'GCS'):
        storage = GoogleCloudStorage(API_TOKEN_PATH)
    else:
        storage = LocalStorage(API_TOKEN_PATH)

    api = VismaAPI(API_CLIENT_ID, API_CLIENT_SECRET, storage)
    bq = BigQueryApi(write_method=TABLE_WRITE_METHOD)
    schema = None
    rows = []

    if API_ENDPOINT == '/accounts':
        schema = accounts_bq_schema
    elif API_ENDPOINT == '/accountTypes':
        schema = account_types_bq_schema
    elif API_ENDPOINT == '/articleaccountcodings':
        schema = article_account_codings_bq_schema
    elif API_ENDPOINT == '/articlelabels':
        schema = article_labels_bq_schema
    elif API_ENDPOINT == '/articles':
        schema = articles_bq_schema
    elif API_ENDPOINT == '/customerinvoices':
        schema = customer_invoices_bq_schema
    elif API_ENDPOINT == '/customerlabels':
        schema = customer_labels_bq_schema
    # elif API_ENDPOINT == '/orders':
    #     schema = orders_bq_schema
    elif API_ENDPOINT == '/supplierinvoices':
        schema = supplier_invoices_bq_schema
    else:
        print(f"API_METHOD {API_ENDPOINT} is not implemented")
        
    api.get_pagination_init(API_ENDPOINT)

    while api.pagination_end is not True:
        print(f"Downloading data from '{API_ENDPOINT}'")
        rows = api.get_query_pagination_next()
        print(f"Downloaded '{len(rows)}' rows of data")
        print(f"Inserting downloaded data to BigQuery")
        bq.insert(PROJECT_ID, DATASET_ID, TABLE_ID, rows, schema=schema)
        print(f"Data has been inserted to BigQuery")

run()
