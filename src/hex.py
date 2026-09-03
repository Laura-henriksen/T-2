import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        # Implement the encoding here
        y = []
        for chr in x:
            hxnbr = f"{ord(chr):02x}"
            y.append(hxnbr)
        z = ''.join(y)
        print(z)
        #encoding = ""
        #print(encoding)

    case "decode":
        # Implement the decoding here
        y = []
        lst = []
        decode = []
        for i in range(0, len(x), 2):
            y.append(x[i:i+2])
        for nbr in y:
            lst.append(int(nbr, base = 16))
        for nmbr in lst:
            decode.append(chr(nmbr))
        decoding = ''.join(decode)
        print(decoding)
