import argparse


parser = argparse.ArgumentParser(description='Powiedz: Witam serdecznie pana --name.')
parser.add_argument('--name', type=str, help='Twoje imie proszę pana!')


args = parser.parse_args()

print ('witam serdecznie pana' + args.name)
