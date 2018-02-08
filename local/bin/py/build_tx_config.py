from optparse import OptionParser


def build_tx_config(options):
    print('Would build config here..')
    print(options)
    # At this point its already merged to master...
    # diff files against master last successful tag/build
    # git diff-tree --no-commit-id --name-only -r 820a2f09
    # ignore translated files that may have changed e.g FR files


def main():
    parser = OptionParser(usage="usage: %prog [options] link_type")
    parser.add_option("-p", "--project_slug", help="tx project slug", default="")
    parser.add_option("-b", "--branch_name", help="branch name to prepend", default="")
    (options, args) = parser.parse_args()

    build_tx_config(options)

if __name__ == "__main__":
    main()
