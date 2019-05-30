from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading
 
class _LoginHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        _UserAuthenticator.auth(self)
        self.end_headers()
        self.wfile.write("Welcome, %s\n" % _UserAuthenticator.user)
 
 
class _UserAuthenticator(object):
    @staticmethod
    def auth(req):
        auth_header = req.headers["Authorization"]
        (user, auth_token) = auth_header.split(":")
        # Assume sensible code here which ensures the user is authorized, by
        # checking the auth token is still valid and matches the user
        # ...
 
        # Authorized!
        _UserAuthenticator.user = user
 
 
class _ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
 
if __name__ == '__main__':
    server = _ThreadedHTTPServer(('0.0.0.0', 8080), _LoginHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
 
 