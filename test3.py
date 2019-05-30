import hashlib
import hmac
import struct
 
_REQUEST_HMAC_KEY = "C0rrectHorseBatteryStaple!"
 
def create_authenticated_request(payload):
    # Test: "Hello" should produce 0005b8382134ef6f58ea28b8ede4b27bf76e19c4e4a648656c6c6f
    encoded_size = struct.pack(">H", len(payload))
    mac = hmac.new(_REQUEST_HMAC_KEY, payload, hashlib.sha1).digest()
    return encoded_size + mac + payload
 
def verify_and_get_authenticated_payload_from_request(req):
    (size,) = struct.unpack(">H", req[0 : 2])
    expected_mac = req[2 : 22]
    actual_mac = hmac.new(_REQUEST_HMAC_KEY, req[22 : 22 + size], hashlib.sha1).digest()
    if not hmac.compare_digest(actual_mac, expected_mac):
        raise ValueError("Request does not authenticate")
    return req[22:]
 