from aocd import models
from src.utils import parse_data

# create puzzle
puzzle = models.Puzzle(year=2021, day=16)

# format data
input_data = parse_data(puzzle.input_data, is_lines=True)

############################
payload = ''.join([(bin(int(c, 16))[2:]).zfill(4) for c in input_data[0]])
print(payload)
exit()

versions = []


def packet_header(head):
    ver = ''.join(payload[head:head+3])
    tid = ''.join(payload[head+3:head+6])
    return int(ver, 2), int(tid, 2)


def process_packet(head):
    ver, tid = packet_header(head)
    versions.append(ver)
    head += 6

    if tid == 4:
        val, head = process_literal(head)
        return head
    else:
        lti = payload[head]
        head += 1

        if lti == '0':
            total_len = int(''.join(payload[head:head+15]), 2)
            head += 15
            packet_end = head + total_len

            while head < packet_end:
                head = process_packet(head)

            return head
        else:
            num_packets = int(''.join(payload[head:head+11]), 2)
            head += 11

            for i in range(num_packets):
                head = process_packet(head)

            return head


def process_literal(head):
    val = ''
    while payload[head] == '1':
        val += payload[head+1:head+5]
        head += 5

    val += payload[head+1:head+5]
    head += 5

    return int(val, 2), head


p_head = 0
process_packet(0)

answer = sum(versions)
############################

# submit answer
puzzle.answer_a = answer
