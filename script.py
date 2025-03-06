import ipaddress

def cidr_to_p2p(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                # Strip whitespace and skip empty lines
                cidr = line.strip()
                if not cidr:
                    continue

                # Convert CIDR to network object
                network = ipaddress.ip_network(cidr)

                # Get first and last IP of the range
                first_ip = str(network[0])
                last_ip = str(network[-1])

                # Write in P2P format (naming all ranges as China)
                outfile.write(f"China:{first_ip}-{last_ip}\n")

        print("Conversion completed successfully!")

    except FileNotFoundError:
        print("Input file not found!")
    except ValueError as e:
        print(f"Invalid CIDR notation found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_file = "cn_ip_list.txt"    # Your input file with CIDR notation
    output_file = "cn_ip_blocklist.txt"    # Output file in P2P format
    cidr_to_p2p(input_file, output_file)
