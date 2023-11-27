import httplib2

url = "http://codeabbey-games.atwebpages.com/say-100.php"
method = "POST"
data = "token: e5CJlcN6WrESFmYPuZfmnDcy"

http = httplib2.Http()

resp, content = http.request(url, method, data)
secret_number = int(content.decode('utf-8').strip().split()[1])

data = f"{data}\nanswer: {100-secret_number}"
resp, content = http.request(url, method, data)
end = content.decode('utf-8').strip()
print(end)

