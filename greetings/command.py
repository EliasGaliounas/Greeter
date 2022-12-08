# %%
print("executing command.py, __name__ is", __name__)

from argparse import ArgumentParser
from greetings.greeter import greet


def process():
    parser = ArgumentParser(description="Generate appropriate greetings")
    parser.add_argument("personal")
    parser.add_argument("family")
    args = parser.parse_args()
    print(greet(args.personal, args.family))


if __name__ == "__main__":
    process()