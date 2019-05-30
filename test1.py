import subprocess

def find_file(file):
	return subprocess.check_out("find.-name '%s'" % file, shell=True).splitlines()