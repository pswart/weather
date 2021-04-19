# Provides via web server weather info that it obtains from a weather service

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import requests
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    _weather_url = "https://goweather.herokuapp.com/weather/{Cape Town}"
    _weather_json = ""
    def get_weather(self):
      c = requests.get(self._weather_url).content
      s = c.decode()
      self._weather_json = json.loads(s)

    def do_GET(self):
        self.get_weather()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Cape Town weather</title></head>", "utf-16"))
        self.wfile.write(bytes("<body>", "utf-16"))
        self.wfile.write(bytes("<p>Today\'s weather for Cape Town that I got from <u>%s</u></p>" % self._weather_url, "utf-16"))
        self.wfile.write(bytes("<p>Description: %s" % self._weather_json["description"], "utf-16"))
        self.wfile.write(bytes("<p>Temperature: %s" % self._weather_json["temperature"], "utf-16"))
        self.wfile.write(bytes("<p>Wind: %s" % self._weather_json["wind"], "utf-16"))
        self.wfile.write(bytes("</body></html>", "utf-16"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
