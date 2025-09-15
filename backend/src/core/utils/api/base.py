import requests
from requests import Response
from src.core.utils.exceptions.errors import (
    ApiServiceCodeError,
    AuthUnauthorizedError,
    RouteNotFoundError,
)


class BaseAPI:
    def _get(self, url, params=None, headers={}):
        response = requests.get(url, params=params, headers=headers)
        return self._parse(response)

    def _post(self, url, data=None, params=None, headers={}):
        response = requests.post(url, json=data, params=params, headers=headers)
        return self._parse(response)

    def _put(self, url, data=None, headers={}):
        response = requests.put(url, json=data, headers=headers)
        return self._parse(response)

    def _patch(self, url, data=None, headers={}):
        response = requests.patch(url, json=data, headers=headers)
        return self._parse(response)

    def _delete(self, url, params=None, headers={}):
        response = requests.delete(url, params=params, headers=headers)
        return self._parse(response)

    def _parse(self, response: Response):
        if response.status_code == 400:
            message = response.text if response.text else "Bad Request"
            raise ApiServiceCodeError(message)

        if response.status_code == 401:
            raise AuthUnauthorizedError(
                "The informed token is invalid. Check your signature !!!"
            )

        elif response.status_code == 404:
            raise RouteNotFoundError(f"Route '{response.url}' not found !!!")

        elif response.status_code == 408:
            raise TimeoutError("Timeout during the request!!!")

        elif response.status_code == 500:
            raise Exception(
                f"Unknown error occured durring the process of the request. Response: {response.text}"
            )

        return response
