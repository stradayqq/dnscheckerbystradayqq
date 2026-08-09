import dns.resolver

def check_dns_records(domain):
    record_types = ['A', 'AAAA', 'MX', 'TXT', 'NS']
    
    print(f"Results of DNS check for domain: {domain}\n")
    
    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            print(f"[{rtype} records]:")
            for rdata in answers:
                print(f"  - {rdata.to_text()}")
        except dns.resolver.NoAnswer:
            print(f"[{rtype} records]: not found")
        except dns.resolver.NXDOMAIN:
            print(f"Error: Domain {domain} does not exist.")
            break
        except Exception as e:
            print(f"[{rtype} records]: Error ({e})")
        print("-" * 30)

if __name__ == "__main__":
    target_domain = "freehost.com.ua"
    check_dns_records(target_domain)
