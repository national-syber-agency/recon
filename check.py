import json
import sys
import hashlib

def main():
    if len(sys.argv) != 2:
        print("Usage: python %s subdomain" % (__file__))
        print("e.g.: python %s something.ns.agency" % (__file__))
        exit(-1)
    subdomain = sys.argv[1]
    check_pwd(subdomain)


min_len = 50

base_domain = ".ns.agency"
seed = "estryuiobase_stringuytrdeswart4e5yugkjhbvfgcdre45y678iyuhkjgdryt5u6ti7yuhkjvgur67ioyulhkjvgdiyuhkj"

def loop_hash(payload):
    for i in range(900000):
        payload = hashlib.sha512(payload.encode('utf-8')).hexdigest()
    return payload


def check_pwd(fulldomain):
    with open('./output.json') as f:
        data = json.load(f)

    full_text = f'{fulldomain}{seed}'
    hashed = loop_hash(full_text)

    for category, hashes in data.items():
        if hashed in hashes:
            print(f"Valid subdomain in {category} category")
            print(hashed)
            exit(0)
    print("Subdomain not found")


if __name__ == "__main__":
    main()

