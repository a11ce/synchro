from http.server import BaseHTTPRequestHandler, HTTPServer
from playsound import playsound
import pause
import time




class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client

        #print(message)
        self.wfile.write(bytes( str(message), "utf8"))
        return

def run():
  print('starting server...')
  server_address = ('192.168.1.123', 8081)
  print('running server...')
  global message
  message = time.time()+5
  print(message)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)

  httpd.handle_request()
  pause.until(message)
  print("now")
  playsound('jesus.mp3', block = True)


run()
