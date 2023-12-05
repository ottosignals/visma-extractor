import json
import datetime
import iso8601
import requests
from .decorators.retry import retry


class VismaAPIException(Exception):
    """An error occurred in the Visma API """
    pass


class VismaClientException(Exception):
    """An error occurred in the Visma Client"""
    pass


class VismaAPI(object):
    """
    Class containing methods to interact with the Visma E-Accounting API
    """

    TOKEN_URL_TEST = 'https://identity-sandbox.test.vismaonline.com/connect/token'
    TOKEN_URL = 'https://identity.vismaonline.com/connect/token'

    API_URL = 'https://eaccountingapi.vismaonline.com/v2'
    API_URL_TEST = 'https://eaccountingapi-sandbox.test.vismaonline.com/v2'

    def __init__(self, client_id, client_secret,
                 storage,
                 test=False):
        """
        Parameters:
        - client_id (str): The client ID for authentication.
        - client_secret (str): The client secret for authentication.
        - token_path (str): The path where tokens will be stored or retrieved.
        - token_storage (str, optional): Type of storage for tokens. Default is None.
        - token_storage_bucket (str, optional): The bucket name in case token_storage is set to GCS (Google Cloud Storage). Default is None.
        - test (bool, optional): Flag indicating if the instance is in test mode. Default is False.
        """

        self.client_id = client_id
        self.client_secret = client_secret
        self._storage = storage
        self._file_name_tokens = "tokens.json"
        self.test = test
        self._load_tokens()

        if self.token_expired:
            self._refresh_token()

    @retry(tries=3, delay=10, max_delay=60, backoff=2)
    def get(self, endpoint, params=None, **kwargs):
        url = self._format_url(endpoint)
        headers = self.api_headers

        r = requests.get(url, params, headers=headers, **kwargs)
        if not r.ok:
            raise VismaAPIException(
                f'GET {r.request.url} :: HTTP:{r.status_code}, {r.content}')
        return r
    
    def get_pagination_init(self, endpoint):
        self.pagination_end = False
        self._pagination_endpoint = endpoint
        self._pagination_params = {
            "$pagesize": 500,
            '$page': 1
            }
        return True

    def get_query_pagination_next(self):
        if self.pagination_end:
            raise VismaClientException(f"All pages have been extracted!")
       
        response = self.get(self._pagination_endpoint, self._pagination_params).json()
        items = response.get('Data', [])
    
        print(f'CurrentPage: {response.get("Meta", {}).get("CurrentPage")}, size: {len(items)}, TotalNumberOfPages: {response.get("Meta", {}).get("TotalNumberOfPages")}')
        if response.get("Meta", {}).get("CurrentPage", 0) >= response.get("Meta", {}).get("TotalNumberOfPages", 0):
            self.pagination_end = True 

        self._pagination_params["$page"] += 1
        return items

    # def post(self, endpoint, data, *args, **kwargs):
    #     url = self._format_url(endpoint)
    #     r = requests.post(url, data, *args, headers=self.api_headers, **kwargs)
    #     if not r.ok:
    #         raise VismaAPIException(
    #             f'POST :: HTTP:{r.status_code}, {r.content}')
    #     return r

    # def put(self, endpoint, data, **kwargs):
    #     url = self._format_url(endpoint)
    #     r = requests.put(url, data, headers=self.api_headers, **kwargs)
    #     if not r.ok:
    #         raise VismaAPIException(
    #             f'PUT :: HTTP:{r.status_code}, {r.content}')
    #     return r

    # def delete(self, endpoint, **kwargs):
    #     url = self._format_url(endpoint)
    #     r = requests.delete(url, headers=self.api_headers, **kwargs)
    #     if not r.ok:
    #         raise VismaAPIException(
    #             f'DELETE :: HTTP:{r.status_code}, {r.content}')
    #     return r

    def _format_url(self, endpoint):
        if self.test:
            url = self.API_URL_TEST + endpoint
        else:
            url = self.API_URL + endpoint
        return url

    @property
    def api_headers(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json'
        }
        return headers

    @property
    def token_expired(self):
        if datetime.datetime.now(tz=datetime.timezone.utc) > self.token_expires:
            return True
        else:
            return False

    @retry(tries=3, delay=10, max_delay=60, backoff=2)
    def _refresh_token(self):

        if self.test:
            url = self.TOKEN_URL_TEST
        else:
            url = self.TOKEN_URL

        data = f'grant_type=refresh_token&refresh_token={self.refresh_token}'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        response = requests.post(url, data,
                                 auth=(self.client_id, self.client_secret),
                                 headers=headers)
        if response.status_code != 200:
            raise VismaAPIException(f'Couldn\'t refresh token: '
                                    f'{response.content}, Client_id={self.client_id}')
        else:
            auth_info = response.json()

            self.access_token = auth_info['access_token']
            self.refresh_token = auth_info['refresh_token']

            now = datetime.datetime.now(tz=datetime.timezone.utc)
            # removes a minute so we don't end up not being authenticated
            # because of time difference between client and server.
            expiry_time = datetime.timedelta(
                seconds=(auth_info['expires_in'] - 60))
            expires = now + expiry_time
            self.token_expires = expires

        self._save_tokens()

    def _load_tokens(self):
        """
        Load tokens from json file
        """
        tokens = self._storage.load_json(self._file_name_tokens)

        self.access_token = tokens['access_token']
        self.refresh_token = tokens['refresh_token']
        self.token_expires = iso8601.parse_date(tokens.get('expires'))
                  
    def _save_tokens(self):
        """
        Save tokens to json file in local env
        """
        tokens = {'access_token': self.access_token,
                  'refresh_token': self.refresh_token,
                  'expires': self.token_expires.isoformat()}
        print("Saving tokens")
        print(f"{tokens}")
        self._storage.save_json(self._file_name_tokens, tokens)



