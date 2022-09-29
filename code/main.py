import cover_blocks.start_block as start_block
from class_blocks.operator_block import connection_operator


def main():
    start_block.run_it()

    while True:
        connection_operator.run_it()


if __name__ == "__main__":
    main()
