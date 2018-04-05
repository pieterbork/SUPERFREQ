import subprocess

def get_hackrf_info():
	p = subprocess.check_output("hackrf_info")
	if "No HackRF boards found" in p:
		return []
	else:
		words = ['version', 'number']
		hackrf = []
		for line in p.splitlines():
			if any(word in line.lower() for word in words):
				parts = line.split(": ")
				key = '_'.join(parts[0].lower().split())
				value = ' '.join(parts[1:])
				hackrf.append((key,value))
		return hackrf
	
