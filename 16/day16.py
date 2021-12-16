from struct import pack
from bitstring import BitArray
import binascii

def parse_packet(data):
  # parse single packet, return excess data
  packet_version = data[0:3].uint
  packet_type = data[3:6].uint
  literal = BitArray()
  idx = 6
  subpackets = []
  packet_count = 0
  if packet_type == 4:
    completed = False
    while (completed == False):
      #print(data[idx])
      if data[idx] is False:
        completed = True
      #print(idx,idx+1,idx+5)
      #print(data[idx+1:idx+5].bin)
      literal.append(data[idx+1:idx+5])
      idx += 5
    #print(literal.uint)
  else:
    # bit indicates length if false, number of subpackets if true
    if data[idx]:
      packet_count = data[idx+1:idx+12].uint
      idx += 12
    else:
      subdata_length = data[idx+1:idx+16].uint
      idx += 16
      subpackets = data[idx:idx+subdata_length]
      idx += subdata_length
  packet = {
    'version': packet_version,
    'type': packet_type,
    'value': literal.uint if literal else 0,
    'sub_packets': subpackets,
    'packet_count': packet_count
  }
  return packet, data[idx:]

def decode_packets(data, count=0):
  completed = False
  version_sum = 0
  values = []
  loop = 0
  while (completed == False):
    packet, data = parse_packet(data)
    version_sum += packet['version']
    if packet['type'] != 4:
      if packet['sub_packets']:
        #print(packet['sub_packets'])
        sub_sum, sub_values, subdata = decode_packets(packet['sub_packets'])
        version_sum += sub_sum
      elif packet['packet_count'] > 0:
        sub_sum, sub_values, subdata = decode_packets(data, packet['packet_count'])
        data = subdata
        version_sum += sub_sum
      if packet['type'] == 0:
        values.append(sum(sub_values))
      elif packet['type'] == 1:
        mult = 1
        for x in sub_values:
          mult = x * mult
        values.append(mult)
      elif packet['type'] == 2:
        values.append(min(sub_values))
      elif packet['type'] == 3:
        values.append(max(sub_values))
      elif packet['type'] == 5:
        values.append(1 if sub_values[0] > sub_values[1] else 0)
      elif packet['type'] == 6:
        values.append(1 if sub_values[0] < sub_values[1] else 0)
      elif packet['type'] == 7:
        values.append(1 if sub_values[0] == sub_values[1] else 0)
    else:
      values.append(packet['value'])
    if len(data) <= 6:
      completed = True
    loop += 1
    if count > 0:
      if loop >= count:
        completed = True
  return version_sum, values, data

if __name__ == "__main__":
  test = False
  if test:
    test_packet = BitArray('0xD2FE28')
    print(test_packet.bin)
    packet, data = parse_packet(test_packet)

    print(packet,data)

    test_packet2 = BitArray('0x38006F45291200')
    packet2, data2 = parse_packet(test_packet2)
    print(packet2, data2)
    packet3, data3 = parse_packet(packet2['sub_packets'])
    print(packet3, data3)
    packet4, data4 = parse_packet(data3)
    print(packet4, data4)
  else:
    with open('input.txt') as f:
      data = '0x' + f.readline()
    packets = BitArray(data)
    version_sums = decode_packets(packets)
    print(version_sums)