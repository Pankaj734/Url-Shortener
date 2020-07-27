
def short(id):
	basemap = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	base = len(basemap)

	surl = ""
	rem = id%base
	surl = surl + basemap[int(rem)]
	quo = int(id/base)

	while quo>0 :
		rem = quo%base
		surl = surl + basemap[int(rem)]
		quo = int(quo/base)

	return str(surl)
