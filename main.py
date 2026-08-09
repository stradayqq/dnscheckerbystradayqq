from fileinput import close

import dns.resolver
from ipwhois import IPWhois

def check_dns_records(domain):
    record_types = ['A', 'AAAA', 'MX', 'TXT', 'NS']
    
    print(f"Results of DNS check for domain: {domain}\n")
    
    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            print(f"[{rtype} records]:")
            for rdata in answers:
                print(f"  - {rdata.to_text()}")
                if rtype == 'A':
                    print_whois(rdata.to_text())
        except dns.resolver.NoAnswer:
            print(f"[{rtype} records]: not found")
        except dns.resolver.NXDOMAIN:
            print(f"Error: Domain {domain} does not exist.")
            break
        except Exception as e:
            print(f"[{rtype} records]: Error ({e})")
        print("-" * 30)

def print_whois(ip):
    try:
        obj = IPWhois(ip)
        res = obj.lookup_rdap(depth=1)
        print(f"    whois for {ip}:")
        print(f"      asn: {res.get('asn')}")
        print(f"      asn_description: {res.get('asn_description')}")
        print(f"      network name: {res.get('network', {}).get('name')}")
        print(f"      country: {res.get('network', {}).get('country')}")
    except Exception as e:
        print(f"    whois for {ip}: Error ({e})")

if __name__ == "__main__":
    target_domain = input("Enter the domain to check: ")    
    check_dns_records(target_domain)
    answer = input("put your domain: ")
    check_dns_records(answer)
close
 