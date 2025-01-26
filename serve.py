from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        SimpleHTTPRequestHandler.end_headers(self)

port = 8000
print(f"Starting server at http://localhost:{port}")
print("Use Ctrl+C to stop the server")
HTTPServer(('localhost', port), CORSRequestHandler).serve_forever() 