from typing import List
from dataclasses import dataclass
import copy


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
    subpackets: List[object] = None


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
            # Call recursively to get the subpackets
            p.subpackets = []
            for _ in range(p.num_subpackets):
                p_sub, pos = pass_a_packet(b, pos)
                p.subpackets.append(p_sub)
        else:
            # 15-bits give combined length of subpackets
            p.subpacket_bits = int(b[pos : pos + 15], 2)
            pos += 15
            # Call recursively to get the subpackets
            p.subpackets = []
            pos_current = copy.deepcopy(pos)
            while pos < pos_current + p.subpacket_bits:
                p_sub, pos = pass_a_packet(b, pos)
                p.subpackets.append(p_sub)

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

    return all_packets, pos


def do_calcs(packet_tree, calc_types):

    print('Doing calcs')
    print('packet_tree', packet_tree)

    type = calc_types[packet_tree.type_id]
    arguments = []
    for sp in packet_tree.subpackets:
        if sp.literal_value:
            arguments.append(sp.literal_value)
        else:
            arguments.append(do_calcs(sp, calc_types))

    result = None
    if type == 'less':
        if arguments[0] < arguments[1]:
            result = 1
        else:
            result = 0
    elif type == 'greater':
        if arguments[0] > arguments[1]:
            result = 1
        else:
            result = 0
    elif type == 'equal':
        if arguments[0] == arguments[1]:
            result = 1
        else:
            result = 0
    elif type == 'sum':
        print('summing', arguments)
        result = sum(arguments)
    elif type == 'prod':
        if len(arguments) == 1:
            result = arguments[0]
        else:
            result=1
            for a in arguments:
                result *= a
    elif type == 'min':
        result = min(arguments)
    elif type == 'max':
        result = max(arguments)

    return result


if __name__ == '__main__':
    data = read_data('day_16.txt')

    test_literal = 'D2FE28'
    test_operator_1 = '38006F45291200'
    test_operator_2 = 'EE00D40C823060'

    test_transmission_1 = '8A004A801A8002F478'
    test_transmission_2 = '620080001611562C8802118E34'
    test_transmission_3 = 'C0015000016115A2E0802F182340'
    test_transmission_4 = 'A0016C880162017C3686B18A3D4780'

    test_result_1 = 'C200B40A82'
    test_result_2 = '04005AC33890'
    test_result_3 = '880086C3E88112'
    test_result_4 = 'CE00C43D881120'
    test_result_5 = 'D8005AC2A8F0'
    test_result_6 = 'F600BC2D8F'
    test_result_7 = '9C005AC2F8F0'
    test_result_8 = '9C0141080250320F1802104A08'

    binary_string = convert_hex_to_binary(data)
    print('Binary string:', binary_string)

    packet_tree, pos = pass_a_packet(binary_string, pos=0)
    print(packet_tree)

    # Get calc type
    calc_types = {
        0: 'sum',
        1: 'prod',
        2: 'min',
        3: 'max',
        4: 'literal',
        5: 'greater',
        6: 'less',
        7: 'equal'
    }

    result = do_calcs(packet_tree, calc_types)
    print('Result', result)




