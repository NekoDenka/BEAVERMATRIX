import http.server
 
PORT = 8080
server_address = ("", PORT)

server = http.server.HTTPServer
handler = http.server.SimpleHTTPRequestHandler
#handler = http.server.CGIHTTPRequestHandler
#handler.cgi_directories = ["/"]
print("Serveur actif sur le port :", PORT)

httpd = server(server_address, handler)
httpd.serve_forever()
test = server.handle()
print(str(test))
