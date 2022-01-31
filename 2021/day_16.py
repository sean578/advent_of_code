from typing import List
from dataclasses import dataclass


def read_data(filename):
    return open(filename).readline().strip()


# Hold a packet (or subpacket) Doesn't yet link to what the subpackets are...
@dataclass
class Packet:
    version: int = None
    type_id: int = None
    literal_value: int = None
    length_type_id: int = None
    subpacket_bits: int = None
    num_subpackets: int = None


def convert_hex_to_binary(hex_string):
    hex_string = '0x' + hex_string
    binary_length = (len(hex_string)-2)*4
    number, pad, rjust, size, kind = int(hex_string, 16), '0', '>', binary_length, 'b'
    return f'{number:{pad}{rjust}{size}{kind}}'


def pass_a_packet(b, pos):
    p = Packet()
    # Get version
    p.version = int(b[pos: pos + 3], 2)
    pos += 3
    # Get type_id
    p.type_id = int(b[pos: pos + 3], 2)
    pos += 3

    # If literal number, get the data:
    if p.type_id == 4:
        not_last_byte = True
        literal_as_list = []
        while not_last_byte:
            not_last_byte = int(b[pos], 2)
            pos += 1
            literal_as_list.extend(b[pos:pos + 4])
            pos += 4
        p.literal_value = int(''.join(literal_as_list), 2)
    # If operator, get the data
    else:
        # Get Length ID type
        p.length_type_id = int(b[pos: pos + 1], 2)
        pos += 1
        if p.length_type_id:
            # 11-bits give number of subpackets
            p.num_subpackets = int(b[pos : pos + 11], 2)
            pos += 11
        else:
            # 15-bits give combined length of subpackets
            p.subpacket_bits = int(b[pos : pos + 15], 2)
            pos += 15

    # TODO: If operator packet then need to link future packets to this one
    return p, pos


def sum_of_versions(all_packets):
    sum_of_versions = 0
    for packet in all_packets:
        sum_of_versions += packet.version
    return sum_of_versions


def pass_packets(b, all_packets):
    pos = 0
    while pos + 10 < len(b):
        packet, pos = pass_a_packet(b, pos)
        all_packets.append(packet)
        # print(packet)

    return all_packets, pos


if __name__ == '__main__':
    data = read_data('day_16.txt')

    test_literal = 'D2FE28'
    test_operator_1 = '38006F45291200'
    test_operator_2 = 'EE00D40C823060'

    test_transmission_1 = '8A004A801A8002F478'
    test_transmission_2 = '620080001611562C8802118E34'
    test_transmission_3 = 'C0015000016115A2E0802F182340'
    test_transmission_4 = 'A0016C880162017C3686B18A3D4780'

    # Each packet has:
    # Header:
    #   Version, type ID

    # IDs:
    #   4: Literal
    #   !4: Operator

    # Literal packet:
    #   3 bits version
    #   3 bits packet type = 4
    #   n*5 bit packets giving number. Xyyy X=0 implies last group.

    # Operator packet high level:
    #   Length type ID = 0 -> 15 bits give combined length of all sub-packets
    #   Length type ID = 1 -> 11 bits give number of sub-packets
    #   Each packet is >= 11 bits (then can be some more zeros at the end)

    binary_string = convert_hex_to_binary(data)
    print('Binary string:', binary_string)
    all_packets = []
    all_packets, pos = pass_packets(binary_string, all_packets)
    for packet in all_packets:
        print(packet)

    print('Answer part 1:', sum_of_versions(all_packets))