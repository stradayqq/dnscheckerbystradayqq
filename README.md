# dnscheck

A utility for checking a domain's DNS records (A, AAAA, MX, TXT, NS) with automatic whois/RDAP lookup for every found A address.

## Installation

Requires `python3` and `pipx`.

If pipx is not installed:
```bash
sudo apt install pipx
```

Clone the repository and install:
```bash
git clone <repo-url>
cd dnschecherbystradayqq
pipx install .
```

On first install, pipx may ask you to update PATH:
```bash
pipx ensurepath
```
After that, **open a new terminal** (or re-login) — just running `source ~/.bashrc` may not pick up the change.

## Usage

```bash
dnscheck
```

The script will ask for a domain and print:
- all found DNS records (A, AAAA, MX, TXT, NS)
- for every A address — whois/RDAP data: ASN, ASN description, network name, country

## Updating

If the repository has been updated:
```bash
cd dnschecherbystradayqq
git pull
pipx install . --force
```

## Dependencies

- [dnspython](https://pypi.org/project/dnspython/)
- [ipwhois](https://pypi.org/project/ipwhois/)

Installed automatically via pipx, no need to install separately.
