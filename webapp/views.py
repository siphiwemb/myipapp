from rest_framework.views import APIView
from rest_framework.response import Response
from .myip_actions import MyIpActions


class MyIPView(APIView):
    MIA = MyIpActions()

    def get(self, request):
        """Get request actions."""

        ip = self.MIA.get_ip_addr_from_request(request)
        prev_ip = self.MIA.get_ip_addr_from_db(ip)
        self.MIA.save_ip_addr(ip) # save the ip address.

        # Generate the response text.
        if prev_ip is None:
            user_ip_dict = {"ip_addr": ip}
        else:
            user_ip_dict = prev_ip
        
        res = self.MIA.generate_reponse_text(user_ip_dict)

        return Response(res, status=200)