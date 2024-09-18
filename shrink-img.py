# A python utility that shrinks images to a desired size.
# You can also specify the output format, defaults to JPEG.


def main():
    # Setup argparser
    import argparse

    desc = "Shrink images to a desired size and format."
    parser = argparse.ArgumentParser(description=desc)

    # Add size argument
    desc = "Desired size in bytes, use M, K to indicate Mega/Kilo(bytes)."
    parser.add_argument(
        "size",
        type=str,
        help=desc,
    )


if __name__ == "__main__":
    main()
