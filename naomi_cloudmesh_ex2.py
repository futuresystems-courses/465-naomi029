import cloudmesh
from pprint import pprint

registeredCloud = cloudmesh.shell("cloud list")

if __name__ == '__main__':
	print registeredCloud
