import argparse

parser = argparse.ArgumentParser(description='My calculator cli')
parser.add_argument('--add',type=init, nargs=2)

args = parser.parse_args()

print(args.add)