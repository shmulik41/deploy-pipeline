from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from service1!")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), HelloHandler)
    print("Starting service1 on port 8080...")
    server.serve_forever()

