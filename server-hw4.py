# Anh Hoang
from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import mimetypes

#It handles HTTP GET requests and serves HTML and JSON files based on the requested resource.
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve HTML or JSON content based on the requested resource
        content_type, _ = mimetypes.guess_type(self.path)
        # get file path
        file_path = self.path[1:]
        # check content type
        #If the content type is text/html, the server attempts to open and read the file.
        if content_type == "text/html":
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    self.send_response(200, "FILE READ SUCCESSFULLY")
                    self.send_header('Content-Type', content_type)
                    self.end_headers()
                    self.wfile.write(content.encode())
            except FileNotFoundError:
                self.send_error(404, f"FILE NOT FOUND: {file_path}")
                self.send_header('Content-Type', content_type)
        #If the content type is application/json, the server attempts to open and read the file as JSON.
        elif content_type == "application/json":
            try:
                with open(file_path, 'r') as file:
                    content = json.load(file)
                    self.send_response(200, "FILE READ SUCCESSFULLY")
                    self.send_header('Content-Type', content_type)
                    self.end_headers()
                    self.wfile.write(json.dumps(content).encode())
            except FileNotFoundError:
                self.send_error(404, f"FILE NOT FOUND: {file_path}")
                self.send_header('Content-Type', content_type)
        else:
            # Handle unsupported content type
            self.send_error(404, "FILE TYPE NOT SUPPORTED")
            self.send_header('Content-Type', content_type)

        # Server setup


port = 8070
server_address = ('', port)
httpd = HTTPServer(server_address, MyHandler)

print(f"Serving on port {port}")
httpd.serve_forever()
