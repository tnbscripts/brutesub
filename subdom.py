#!.../Python3

import requests,sys

def usage():
	print(f"Well come.\nTypes: http or https\nUsage: {sys.argv[0]} <site.com> <type>\nOBS: Yes:site.com\nNo:www.site.com")
	exit()

if len(sys.argv) < 3:
	usage()

target = sys.argv[1]
type = sys.argv[2]

with open("subdomains.txt") as file:
	print(f"[*]initiating attack on: {target}\n")
	count = 0
	for i in file:
		limit = 200
		count += 1
		if count >= limit:
			print("[...]Processing[...]")
			count = 0
		sub = i.strip()
		url_type1 = f"http://{sub}.{target}"
		url_type2 = f"https://{sub}.{target}"
		try:
			if type == "http":
				r = requests.get(url_type1, timeout=8)
				if r.status_code == 200:
					print(f"[+]Subdomain Found: {url_type1}")
			elif type == "https":
				r = requests.get(url_type2, timeout=8)
				if r.status_code == 200:
					print(f"[+]Subdomain Found: {url_type2}")
		except:
			continue
