import json
import iso8601
import os

class StorageBase:
    def load_json(self):
        raise NotImplementedError("Method load_json must be implemented")

    def save_json(self):
        raise NotImplementedError("Method save_json must be implemented")

class LocalStorage(StorageBase):
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def load_json(self, file_name):
        file_path = os.path.join(self.storage_path, file_name)
        try:
            with open(file_path) as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File '{file_name}' not found at '{self.storage_path}'")
            return {}

    def save_json(self, file_name, json_object):
        file_path = os.path.join(self.storage_path, file_name)
        with open(file_path, 'w') as file:
            json.dump(json_object, file)

class GoogleCloudStorage(StorageBase):
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name

        from google.cloud import storage
        self._client = storage.Client()
        self._bucket = self._client.get_bucket(self.bucket_name)

    def load_json(self, file_name):
        blob = self._bucket.blob(file_name)
        with blob.open("r") as file:
            return json.load(file)

    def save_json(self, file_name, json_object):
        blob = self._bucket.blob(file_name)
        with blob.open("w") as file:
            json.dump(json_object, file)
