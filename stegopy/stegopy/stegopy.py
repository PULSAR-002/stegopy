import argparse
from stegano import lsb

def hide(img2hide, message, newImg):
    try:
        secret = lsb.hide(img2hide, message)
        secret.save(newImg)
        print(f"[+] Message hidden and saved to: {newImg}")
    except Exception as e:
        print(f"[!] Error: {e}")

def decode(img2decode):
    try:
        msg = lsb.reveal(img2decode)
        print("[+] Decoded message:\n", msg)
    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Terminal-based Steganography tool by PULSAR")

    subparsers = parser.add_subparsers(dest='command', help='Subcommands: encode or decode')

    # Encode subcommand
    encode_parser = subparsers.add_parser('encode', help='Hide a message in an image')
    encode_parser.add_argument('--image', required=True, help='Path to the input image (.png or .bmp)')
    encode_parser.add_argument('--message', required=True, help='Secret message to hide')
    encode_parser.add_argument('--output', required=True, help='Path for the output image')

    # Decode subcommand
    decode_parser = subparsers.add_parser('decode', help='Reveal a hidden message from image')
    decode_parser.add_argument('--image', required=True, help='Path to the image containing hidden message')

    args = parser.parse_args()

    if args.command == 'encode':
        hide(args.image, args.message, args.output)
    elif args.command == 'decode':
        decode(args.image)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
