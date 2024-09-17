from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class RequestHandler(BaseHTTPRequestHandler):
    def serve_index(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        with open('index.html') as fp:
            self.wfile.write(fp.read().encode('utf-8'))

    def serve_table(self):
        email = self.path.split('?')[-1]
        try:
            table = [line.split(",") for line in open(f"db/{email}.csv").readlines()]
        except FileNotFoundError:
            self.serve_404()
            return

        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        
        html = "<table border='1'>"
        html += "<thead><tr>" + "".join(f"<th>{e}</th>" for e in table[0]) + "<tr><thead>"
        html += "<tbody>" + "".join([
            "<tr>"+"".join([f"<td>{e}</td>" for e in row])+"</tr>"
            for row in table[1:]
        ]) + "</tbody>"
        html += "</table>"
        
        html = f"""
        <html>
        <head>
            <title>CSV Table</title>
        </head>
        <body>
            <h1>Data ^_^</h1>
            {html}
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

    def serve_404(self):
        self.send_response(404)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Not Found')

    def do_GET(self):
        if self.path == '/':
            self.serve_index()
        elif "/table" in self.path:
            self.serve_table()
        else:
            self.serve_404() 

server = HTTPServer(
    ('', 80), 
    RequestHandler
)
server.serve_forever()
