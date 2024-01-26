import re

def extract_domain(email):
    match = re.search('@([A-Za-z0-9.]+)', email)
    return match.group(1) if match else None

def main():
    k = int(input("Enter the number of emails: "))
    unique_domains = set()

    for _ in range(k):
        email = input("Enter an email: ").strip()
        domain = extract_domain(email)

        if domain:
            unique_domains.add(domain)

    for domain in sorted(unique_domains):
        print(domain)

if __name__ == "__main__":
    main()
