import math

from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=16)

# format data
input_data = parse_data(puzzle.input_data, is_lines=True)

############################
payload = ''.join([(bin(int(c, 16))[2:]).zfill(4) for c in input_data[0]])

def packet_header(head):
    ver = ''.join(payload[head:head+3])
    tid = ''.join(payload[head+3:head+6])
    return int(ver, 2), int(tid, 2)


def process_packet(head, depth):
    ver, tid = packet_header(head)
    head += 6

    if tid == 4:
        val, head = process_literal(head)
        print(f"{' ' * depth}LITERAL = {val}")
        return val, head
    else:
        lti = payload[head]
        head += 1

        values = []
        if lti == '0':
            print(f"{' ' * depth}OPERATOR {''.join(payload[head:head+15])}")
            total_len = int(''.join(payload[head:head+15]), 2)
            head += 15
            packet_end = head + total_len
            print(f"{' ' * depth}OPERATOR {total_len=}")

            while head < packet_end:
                val, head = process_packet(head, depth+1)
                values.append(val)
        else:
            num_packets = int(''.join(payload[head:head+11]), 2)
            head += 11
            print(f"{' ' * depth}OPERATOR {num_packets=}")

            values = []
            for i in range(num_packets):
                val, head = process_packet(head, depth+1)
                values.append(val)


        match tid:
            case 0:
                return sum(values), head
            case 1:
                return math.prod(values), head
            case 2:
                return min(values), head
            case 3:
                return max(values), head
            case 5:
                return 1 if values[0] > values[1] else 0, head
            case 6:
                return 1 if values[0] < values[1] else 0, head
            case 7:
                return 1 if values[0] == values[1] else 0, head


def process_literal(head):
    val = ''
    while payload[head] == '1':
        val += payload[head+1:head+5]
        head += 5

    val += payload[head+1:head+5]
    head += 5

    print(head, int(val, 2))
    return int(val, 2), head


answer, _ = process_packet(0, 0)
############################
print(answer)

# submit answer
puzzle.answer_b = answer
