import socket

hostnames = [
		"rutracker.org",
		"turkiye.gov.tr",
		"apa.az",
		"google.com",
		"linkedin.com",
		"irs.gov",
		"premierbet.co.ao",
		"rezka.ag",
		"china.com",
		"asos.com",
		"wikimedia.org"
    ]

my_file = open("ipv6-address-list.txt", "w")

for x in hostnames:
    # addressInfo = socket.getaddrinfo(x, 80, family=socket.AF_INET, proto=socket.IPPROTO_TCP)[0][-1][0]
    addressInfo = socket.getaddrinfo(x, 80, family=socket.AF_INET6, proto=socket.IPPROTO_TCP)[0][-1][0]
    print(x)
    print(addressInfo)
    if (x == hostnames[len(hostnames)-1]):
        my_file.write("\'" + addressInfo + "\'")
    else:
        my_file.write("\'" + addressInfo + "\'," + "\n")

my_file.close()