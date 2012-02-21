from global_constants import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",3496)) # replace "" with socket.gethostname() to make public
s.listen(0)

sock_array = []

MAX_PLAYERS = 2
while True:
	if len(sock_array) < MAX_PLAYERS:
		sock_array.append(s.accept()[0])
		print sock_array
