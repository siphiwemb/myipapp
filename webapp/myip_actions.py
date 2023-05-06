from .models import UserIp
from django.utils import timezone
from datetime import datetime
import pytz

class MyIpActions():

    def get_ip_addr_from_request(self, request):
        """Gets the ip address from the request Meta data."""

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('HTTP_X_REAL_IP')
        
        return ip

    
    def save_ip_addr(self, ip: str):
        """Saves the ip address into the database."""

        ip_obj = UserIp.objects.filter(ip_addr=ip)

        if ip_obj.exists():
            UserIp.objects.filter(ip_addr=ip).update(timestamp=timezone.now())
        else:
            UserIp.objects.create(ip_addr=ip)
        return True


    def get_ip_addr_from_db(self, ip: str):
        """Gets and returns ip address details from the db if found."""

        user_ip_items = UserIp.objects.filter(ip_addr=ip).order_by('-timestamp').values()

        if len(user_ip_items) > 0:
            return {"ip_addr": user_ip_items[0]["ip_addr"], "timestamp": user_ip_items[0]["timestamp"]}
        else:
            return None
    

    def generate_reponse_text(self, user_ip_dict: dict):
        """Generates the response text to be returned to the user."""

        if "timestamp" in user_ip_dict:
            dt = user_ip_dict["timestamp"]
            eastern_tz = pytz.timezone('US/Eastern')
            dt = dt.astimezone(eastern_tz)
            human_readable_str = dt.strftime('%a %b %d %H:%M:%S %Z %Y')

            return f"""Your client's IP address is: {user_ip_dict["ip_addr"]}. Your previous/last request was on {human_readable_str}."""
        else:
            return f"""Your client's IP address is: {user_ip_dict["ip_addr"]}. This is the first message received from your client."""
