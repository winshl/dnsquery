
import dns.resolver
import time

def dns_query(domain, record_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ["8.8.8.8"]

    print(f"\nDNS Query: {domain}")
    print(f"Record Type: {record_type}")
    print("DNS Server: 8.8.8.8")

    start = time.time()

    try:
        answers = resolver.resolve(domain, record_type)
        end = time.time()

        print("\nQuery Results:")

        for answer in answers:
            print(answer)

        response_time = (end - start) * 1000

        print(f"\nResponse Time: {response_time:.2f} ms")
        print("Status: SUCCESS")

    except dns.resolver.NXDOMAIN:
        print("Error: Domain does not exist.")

    except dns.resolver.NoAnswer:
        print("Error: No records found.")

    except dns.exception.Timeout:
        print("Error: DNS request timed out.")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    domain = input("Enter domain name: ")
    record_type = input(
        "Record type (A, AAAA, MX, NS, TXT, CNAME): "
    ).upper()

    dns_query(domain, record_type)
