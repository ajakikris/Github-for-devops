from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = """
            <html>
            <head><title>Simple Python Webpage</title></head>
            <body>
                <h1>Welcome to My Python Webpage!</h1>
                <p>This page is served using Python's built-in HTTP server.</p>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
        else:
            super().do_GET()

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Serving on http://localhost:8000")