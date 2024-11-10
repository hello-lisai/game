import http.server
import socketserver
import os
import webbrowser

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    
    # 打开当前目录下的 index.html 文件
    index_path = os.path.join(os.getcwd(), "index.html")
    if os.path.exists(index_path):
        webbrowser.open(f"http://localhost:{PORT}/index.html")
    
    httpd.serve_forever()
