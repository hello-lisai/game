import http.server
import socketserver

# 设置 HTTP 服务器的端口号
PORT = 8000

# 创建 HTTP 请求处理程序
Handler = http.server.SimpleHTTPRequestHandler

# 创建 HTTP 服务器
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
