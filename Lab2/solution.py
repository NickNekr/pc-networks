import sys
import socket
from ping3 import ping
import click

class MTUChecker:
    def __init__(self, dest_ip, min_mtu=500, max_mtu=3000):
        self.dest_ip = dest_ip
        self.min_mtu = min_mtu
        self.max_mtu = max_mtu

    def check_host(self):
        try:
            socket.gethostbyname(self.dest_ip)
            return True
        except socket.error:
            return False

    def find_mtu(self):
        min_mtu = self.min_mtu - 1
        max_mtu = self.max_mtu

        while min_mtu + 1 < max_mtu:
            current_mtu = (min_mtu + max_mtu) // 2

            reply = ping(self.dest_ip, size=current_mtu-28, timeout=2)

            if reply:
                min_mtu = current_mtu
            else:
                max_mtu = current_mtu

        if min_mtu == self.min_mtu - 1:
            print(f"Error: Bad min/max mtu values.")
            sys.exit(1)


        return min_mtu

@click.command()
@click.argument('host', type=str, required=True)
@click.option('--min_mtu', type=click.IntRange(0, 1000000), default=500, help='Minimum MTU value to start with (default: 500)')
@click.option('--max_mtu', type=click.IntRange(0, 1000000), default=3000, help='Maximum MTU value to start with (default: 3000)')
def main(host, min_mtu, max_mtu):
    checker = MTUChecker(host, min_mtu, max_mtu)

    if not checker.check_host():
        print(f"Error: Destination {host} is unreachable.")
        sys.exit(1)

    try:
        mtu = checker.find_mtu()
        print(f"Optimal MTU for {host} is {mtu}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
   