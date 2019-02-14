import argparse


parser = argparse.ArgumentParser(description='Powiedz: Witam serdecznie pana --name.')
parser.add_argument('--name', type=str, help='Twoje imie proszę pana!')
parser.add_argument('--powitanie', type=str, help='Powitanie!')

args = parser.parse_args()

print (args.powitanie + args.name)
