from intcode_day_11 import IntCode


def test_parse_mode_opcode():
    intcode = IntCode(DEBUG=True)
    assert intcode.parse_mode_opcode(1) == (1, [0, 0, 0])
    assert intcode.parse_mode_opcode(101) == (1, [1, 0, 0])
    assert intcode.parse_mode_opcode(1001) == (1, [0, 1, 0])
    assert intcode.parse_mode_opcode(10001) == (1, [0, 0, 1])
    assert intcode.parse_mode_opcode(1101) == (1, [1, 1, 0])
    assert intcode.parse_mode_opcode(12001) == (1, [0, 2, 1])
    assert intcode.parse_mode_opcode(22201) == (1, [2, 2, 2])
