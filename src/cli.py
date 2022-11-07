from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(
        prog='Flatpak Notion Repackaged Installer',
        description='Builds and installs Notion Repackaged as a flatpak',
    )

    parser.add_argument("-i", "--install", action='store_true')

    return parser.parse_args()
