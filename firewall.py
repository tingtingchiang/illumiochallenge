import csv
import ipaddress

class Firewall():
	def __init__(self, csv_file):
		self.rules = self.__process_csv(csv_file);

	def __process_csv(self, csv_file):
		rules = {}
		with open(csv_file, newline='') as csvfile:
			csv_reader = csv.reader(csvfile)
			for row in csv_reader:
				# row = direction, protocol, port, IP address
				key = (row[0],row[1])
				port = [int(port) for port in row[2].split('-')]
				ipaddr = [int(ipaddress.ip_address(addr)) for addr in row[3].split('-')]
				if key in rules:
					rules[key].append((ipaddr,port))
				else:
					rules[key] = [(ipaddr,port)]
		return rules

	def __validate(self, x, target):
		return target[0] <= x <= target[1] if len(target) == 2 else target[0] == x

	def accept_packet(self, direction,protocol, port, ip_address):
		ip_address = int(ipaddress.ip_address(ip_address))

		if (direction,protocol) not in self.rules:
			return False

		for valid_ip, valid_port in self.rules.get((direction,protocol)):
			if self.__validate(ip_address, valid_ip) and self.__validate(port, valid_port):
				return True
		return False

# class RangeTree():
# 	def __init__(self, data = 2147483647):
# 		self.left = None
# 		self.right = None
# 		self.data = data
# 		self.is_leaf = True

# 	def insert(self, ipaddr, port):
# 		