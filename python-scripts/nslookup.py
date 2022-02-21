import socket

# Performs IPv6 DNS-lookup on a given list of hostnames and logs the resulting IPv6-addresses to a file
filename = "ipv6-address-list-full.txt"

#hostnames = [
		#"rutracker.org",
		#"turkiye.gov.tr",
		#"apa.az",
		#"google.com",
		#"linkedin.com",
		#"irs.gov",
		#"premierbet.co.ao",
		#"rezka.ag",
		#"china.com",
		#"asos.com",
		#"wikimedia.org"
    #]

hostnames = [
		"google.com",
		"youtube.com",
		"qq.com",
		"facebook.com",
		"yahoo.com",
		"wikipedia.org",
		"live.com",
		"microsoft.com",
		"office.com",
		"netflix.com",
		"instagram.com",
		"google.com.hk",
		"canva.com",
		"force.com",
		"alipay.com",
		"bing.com",
		"apple.com",
		"linkedin.com",
		"adobe.com",
		"chaturbate.com",
		"okezone.com",
		"yy.com",
		"getadblock.com",
		"yandex.ru",
		"whatsapp.com",
		"godaddy.com",
		"mail.ru",
		"google.com.br",
		"medium.com",
		"spotify.com",
		"google.co.in",
		"google.cn",
		"blogger.com",
		"google.de",
		"aliyun.com",
		"google.co.jp",
		"pikiran-rakyat.com",
		"telegram.org",
		"babytree.com",
		"dropbox.com",
		"espn.com",
		"google.fr",
		"zendesk.com",
		"rednet.cn",
		"google.es",
		"ilovepdf.com",
		"notion.so",
		"cnn.com",
		"kumparan.com",
		"salesforce.com",
		"xhamster.com",
		"google.ru",
		"t.me",
		"bbc.com",
		"indiatimes.com",
		"nih.gov",
		"calendly.com",
		"padlet.com",
		"google.it",
		"bscscan.com",
		"google.com.tw",
		"onlinesbi.com",
		"zerodha.com",
		"speedtest.net",
		"bet9ja.com",
		"hdfcbank.com",
		"fedex.com",
		"theguardian.com",
		"pixabay.com",
		"etherscan.io",
		"investing.com",
		"icicibank.com",
		"pancakeswap.finance",
		"google.com.sg",
		"state.gov",
		"bbc.co.uk",
		"google.co.uk",
		"healthline.com",
		"ikea.com",
		"cnnic.cn",
		"researchgate.net",
		"documentforce.com",
		"google.com.tr",
		"suara.com",
		"google.com.mx",
		"cnet.com",
		"albawabhnews.com",
		"hotstar.com",
		"skype.com",
		"google.ca",
		"investopedia.com",
		"poocoin.app",
		"foxnews.com",
		"manoramaonline.com",
		"remove.bg",
		"youm7.com",
		"uol.com.br",
		"tudou.com",
		"espncricinfo.com",
		"blackboard.com",
		"geeksforgeeks.org",
		"taboola.com",
		"google.co.th",
		"hp.com",
		"google.com.ar",
		"webex.com",
		"y2mate.com",
		"ca.gov",
		"google.com.sa",
		"secureserver.net",
		"mozilla.org",
		"disneyplus.com",
		"spankbang.com",
		"google.com.eg",
		"wikimedia.org",
		"yandex.com",
		"ndtv.com",
		"dailymail.co.uk",
		"moneycontrol.com",
		"aol.com",
		"asos.com",
		"china.com",
		"canada.ca",
		"thesaurus.com",
		"redd.it",
		"namu.wiki",
		"patreon.com",
		"flickr.com",
		"att.com",
		"plantvsundead.com",
		"rezka.ag",
		"google.co.kr",
		"cj.com",
		"metropoles.com",
		"wazirx.com",
		"xfinity.com",
		"rt.com",
		"premierbet.co.ao",
		"alwafd.news",
		"google.pl",
		"irs.gov",
		"shein.com",
		"google.co.id",
		"typeform.com",
		"tableau.com",
		"orange.fr",
		"smartsheet.com",
		"patch.com",
		"jpnn.com",
		"coinpayu.com",
		"smallseotools.com",
		"google.ro",
		"quillbot.com",
		"inquirer.net",
		"naukri.com",
		"hindustantimes.com",
		"bukalapak.com",
		"dextools.io",
		"ensonhaber.com",
		"thepiratebay.org",
		"teachable.com",
		"seekingalpha.com",
		"codepen.io",
		"axieinfinity.com",
		"news18.com",
		"apa.az",
		"google.gr",
		"turkiye.gov.tr",
		"googlevideo.com",
		"alodokter.com",
		"google.az",
		"dcard.tw",
		"ladbible.com",
		"mathrubhumi.com",
		"ai.marketing",
		"cnnindonesia.com",
		"wsj.com",
		"rutracker.org",
		"usps.com",
		"boc.cn",
		"rctiplus.com",
		"ebay-kleinanzeigen.de",
		"google.com.ua",
		"udemy.com",
		"elementor.com"
]

with open(filename, "w") as my_file:
	for host in hostnames:
		addressInfo = socket.getaddrinfo(host, 80, family=socket.AF_INET6, proto=socket.IPPROTO_TCP)[0][-1][0]
		print(host)
		print(addressInfo)
		if (host == hostnames[len(hostnames)-1]):
			my_file.write("\'" + addressInfo + "\'")
		else:
			my_file.write("\'" + addressInfo + "\'," + "\n")