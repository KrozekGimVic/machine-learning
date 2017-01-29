from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse
import json
import skynet

class Server(BaseHTTPRequestHandler):
    sk = skynet.Skynet(image_size=30)
    save_on = 0

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

            Server.sk.load_data_from_string(label, image)
            Server.sk.train(E=1, mbs=1, learning_rate=1e-8)
            Server.save_on += 1
            if Server.save_on >= 10:
                Server.sk.save_engine_matrix()
                Server.save_on = 0
        except:
            self.wfile.write('Wrong json data.\n'.encode('utf-8'))

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, Server)
    httpd.serve_forever()

run()
