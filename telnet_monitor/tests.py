from django.test import TestCase
from django.urls import reverse


class ViewTester(TestCase):
    def test_resolve(self):
        response = self.client.get(
            reverse('telnet_monitor:api:resolve'), {
                'host': 'www.cga.gov.tw',
            })
        self.assertJSONEqual(
            response.content, {
                'status': 'success',
                'hostname': 'www.cga.gov.tw',
                'address': ['210.241.92.252']
            })

    def test_telnet(self):
        response = self.client.get(
            reverse('telnet_monitor:api:telnet'), {
                'host': 'www.cga.gov.tw',
                'port': '80'
            })
        self.assertJSONEqual(
            response.content, {
                'status': 'success',
                'hostname': 'www.cga.gov.tw',
                'port': 80,
                'result': 'alive',
            })

    def test_page(self):
        respone = self.client.get(reverse('telnet_monitor:index'))
        self.assertEqual(respone.status_code, 200)
