import argparse

parser = argparse.ArgumentParser(prog="ping")

parser.add_argument("STRING")

parser = argparse.ArgumentParser(prog="ping", description="Ping command")
parser.add_argument("destination", help="dns name or ip address")
parser.add_argument(
    "-i",
    type=float,
    help="seconds between sending each packet",
)
parser.add_argument("-c", type=int, help="stop after <count> replies")
parser.add_argument("-D", action="store_true", help="print timestamps")
parser.add_argument("-a", action="store_true", help="use audible ping")
parser.add_argument("-A", action="store_true", help="use adaptive ping")
parser.add_argument("-B", action="store_true", help="sticky source address")
parser.add_argument(
    "-d",
    action="store_true",
    help="use SO_DEBUG socket option",
)
parser.add_argument("-f", action="store_true", help="flood ping")
parser.add_argument("-I", help="either interface name or address")
parser.add_argument(
    "-L",
    action="store_true",
    help="suppress loopback of multicast packets",
)
parser.add_argument(
    "-l",
    type=int,
    help="send <preload> number of packages while waiting replies",
)
parser.add_argument("-m", help="tag the packets going out")
parser.add_argument(
    "-M",
    choices=["do", "dont", "want"],
    help="define mtu discovery",
)
parser.add_argument(
    "-n",
    action="store_true",
    help="no dns name resolution",
)
parser.add_argument(
    "-O",
    action="store_true",
    help="report outstanding replies",
)
parser.add_argument("-p", help="contents of padding byte")
parser.add_argument("-q", action="store_true", help="quiet output")
parser.add_argument("-Q", help="use quality of service <tclass> bits")
parser.add_argument(
    "-s",
    type=int,
    help="use <size> as number of data bytes to be sent",
)
parser.add_argument(
    "-S",
    type=int,
    help="use <size> as SO_SNDBUF socket option value",
)
parser.add_argument("-t", help="define time to live")
parser.add_argument(
    "-U",
    action="store_true",
    help="print user-to-user latency",
)
parser.add_argument("-v", action="store_true", help="verbose output")
parser.add_argument("-V", action="version", version="%(prog)s version")
parser.add_argument(
    "-w",
    type=float,
    help="reply wait <deadline> in seconds",
)
parser.add_argument("-W", help="time to wait for response")

ipv4_group = parser.add_argument_group("IPv4 options")
ipv4_group.add_argument("-4", action="store_true", help="use IPv4")
ipv4_group.add_argument(
    "-b",
    action="store_true",
    help="allow pinging broadcast",
)
ipv4_group.add_argument(
    "-R",
    action="store_true",
    help="record route",
)
ipv4_group.add_argument(
    "-T",
    choices=["tsonly", "tsandaddr", "tsprespec"],
    help="define timestamp",
)

ipv6_group = parser.add_argument_group("IPv6 options")
ipv6_group.add_argument("-6", action="store_true", help="use IPv6")
ipv6_group.add_argument("-F", help="define flow label")
ipv6_group.add_argument(
    "-N",
    help="use icmp6 node info query, try <help> as argument",
)
