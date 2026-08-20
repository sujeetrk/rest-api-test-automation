import logging

import requests

from utils.logger import get_logger


logger = get_logger(__name__)


class APIClient:

    def get(self, url):
        logger.info(f"GET request: {url}")

        response = requests.get(url)

        logger.info(
            f"GET response: {response.status_code} "
            f"| Time: {response.elapsed.total_seconds():.3f}s"
        )

        return response

    def post(self, url, data=None):
        logger.info(f"POST request: {url}")

        response = requests.post(url, json=data)

        logger.info(
            f"POST response: {response.status_code} "
            f"| Time: {response.elapsed.total_seconds():.3f}s"
        )

        return response

    def put(self, url, data=None):
        logger.info(f"PUT request: {url}")

        response = requests.put(url, json=data)

        logger.info(
            f"PUT response: {response.status_code} "
            f"| Time: {response.elapsed.total_seconds():.3f}s"
        )

        return response

    def patch(self, url, data=None):
        logger.info(f"PATCH request: {url}")

        response = requests.patch(url, json=data)

        logger.info(
            f"PATCH response: {response.status_code} "
            f"| Time: {response.elapsed.total_seconds():.3f}s"
        )

        return response

    def delete(self, url):
        logger.info(f"DELETE request: {url}")

        response = requests.delete(url)

        logger.info(
            f"DELETE response: {response.status_code} "
            f"| Time: {response.elapsed.total_seconds():.3f}s"
        )

        return response