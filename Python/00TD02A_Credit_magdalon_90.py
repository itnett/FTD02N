python
from http.server import BaseHTTPRequestHandler, HTTPServer

class EnkelServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>Hei, verden!</h1></body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer(("localhost", 8080), EnkelServer)
    print("Server startet http://%s:%s" % ("localhost", 8080))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stoppet.")