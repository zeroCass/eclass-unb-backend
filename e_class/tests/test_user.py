from rest_framework.reverse import reverse #type:ignore
from rest_framework import status #type:ignore
from rest_framework.test import APITestCase #type:ignore
from e_class.models import User

import logging
logger = logging.getLogger(__name__)

class UsersViewSetTestCase(APITestCase):
    def add_test_users(self):
        """
        Adds a test User into the database
        """
        logger.debug('Adding a new User into database')
        u = User(name='Casper', email='casper@gmail.com', password='casper', cpf='31231312322', userType=2)
        u.save()
        logger.debug('Successfully added test User into the database')

    def test_list_users(self):
        """
        Test to list all the Userss in the list
        """
        logger.debug('Starting test list User')

        self.add_test_users()

        url = 'https://unbiased-coder.com:8000%s'%reverse('users-list')
        logger.debug('Sending TEST data to url: %s'%url)
        response = self.client.get(url, format='json')
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d'%(json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        logger.debug('Testing result count')
        self.assertEqual(len(json), 1)