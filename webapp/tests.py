from django.test import TestCase
from .myip_actions import MyIpActions
import datetime



# Create your tests here.
class MyIpTest(TestCase):

    MIA = MyIpActions()
    ip = '127.0.0.1'

    def setUp(self):
        pass

    def test_myip_view(self):

        # 1. Test get_ip_addr_from_db method

        # 1.1 if ip does not exist
        get_ip_obj = self.MIA.get_ip_addr_from_db(self.ip)
        self.assertIsNone(get_ip_obj)

        # 2. Test save_ip_addr method
        saved_ip = self.MIA.save_ip_addr(self.ip)
        self.assertTrue(saved_ip, True)

        # 1.2 if ip exists
        get_ip_obj = self.MIA.get_ip_addr_from_db(self.ip)
        self.assertIn("ip_addr", get_ip_obj)

        # 3. Test generate_reponse_text
        
        # 3.1 if ip does not exists
        ip_obj = {"ip_addr": self.ip}
        resp_text = self.MIA.generate_reponse_text(ip_obj)
        expected_text = f"""Your client's IP address is: {self.ip}. This is the first message received from your client."""
        self.assertEqual(resp_text, expected_text)

        # 3.2 if ip does exists
        time_now = datetime.datetime.now()
        ip_obj = {"ip_addr": self.ip, "timestamp": str(time_now)}
        resp_text = self.MIA.generate_reponse_text(ip_obj)
        expected_text = f"""Your client's IP address is: {self.ip}. Your previous/last request was on {time_now}."""
        self.assertEqual(resp_text, expected_text)

        # 4 Test the get request
        
        # 4.1 if ip does not exist
        response = self.client.get('/api/myip/', follow=True)
        self.assertContains(response, "This is the first message received from your client.")

        # 4.2 if ip exists
        response = self.client.get('/api/myip/', follow=True)
        self.assertContains(response, "Your previous/last request was on")

