from DnsClient import DnsClient
from PackageTypeEnums import package_type

main_root_server = '192.33.4.12'
reserved_root_server = '8.8.8.8'
port = 53
address = 'quora.com'
req_type = package_type.A
dns_client = DnsClient('TCP', True)
try:
    print(dns_client.get_ip(address, main_root_server, req_type=req_type, port=port))
except (ValueError, TimeoutError) as e:
    print(dns_client.get_ip(address, reserved_root_server, req_type=req_type, port=port))
