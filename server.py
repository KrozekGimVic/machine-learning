from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse
import json

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write('Not implemented yet.\n'.encode('utf-8'))

    def do_POST(self):
        self._set_headers()
        if self.path != '/upload_image':
            self.wfile.write('Wrong url.\n'.encode('utf-8'))
            return

        try:
            content_len = int(self.headers['content-length'])
            data = self.rfile.read(content_len)
            data_dict = json.loads(data)

            label = data_dict['label']
            image = data_dict['image']


        except:
            self.wfile.write('Wrong json data.\n'.encode('utf-8'))

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, Server)
    httpd.serve_forever()

run()
