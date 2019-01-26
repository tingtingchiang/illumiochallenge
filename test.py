from firewall import Firewall
import time

TIME_REQ = 8

def common_cases():
	f = Firewall('test_input.csv')

	assert f.accept_packet("inbound", "tcp", 80, "192.168.1.2")
	assert f.accept_packet("inbound", "udp", 53, "192.168.2.1")
	assert not f.accept_packet("inbound", "tcp", 81, "192.168.1.2")
	assert not f.accept_packet("inbound", "udp", 24, "52.12.48.92")
	print('Base Cases Passed')

def edge_cases():
	f = Firewall('edge_case.csv')

	# test overlap in part of ip range does not affect port validity
	assert not f.accept_packet("inbound", "tcp", 89, "192.168.2.3")
	# test present ip range overlap does not affect port validity
	assert f.accept_packet("inbound", "tcp", 80, "192.168.1.9")
	# test port range is inclusive
	assert f.accept_packet("inbound", "tcp", 53, "192.168.1.2")
	assert f.accept_packet("inbound", "tcp", 79, "192.168.1.2")
	# test ip address range is inclusive
	assert f.accept_packet("inbound", "tcp", 80, "192.168.2.5")
	assert f.accept_packet("inbound", "tcp", 80, "192.168.1.1")
	# test out of ip range by one.
	assert not f.accept_packet("inbound", "tcp", 88, "192.168.2.0")
	# test packet is only tested against applicable rules
	assert not f.accept_packet("outbound", "tcp", 80, "192.168.2.0")


	print('Edge Cases Passed')

def large_set():
	f = Firewall('large_set.csv')
	start = time.time()

	# test overlap in part of ip range does not affect port validity
	for i in range(100):
		assert not f.accept_packet('inbound','tcp',1,'192.168.1.2')

	end = time.time()
	assert end-start<TIME_REQ
	print('Large Set Passed')


common_cases()
edge_cases()
large_set()