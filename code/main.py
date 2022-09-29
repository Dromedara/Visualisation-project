import start_block
from operator_block import connection_operator


def main():
    start_block.run_it()

    while True:
        connection_operator.run_it()


if __name__ == "__main__":
    main()
