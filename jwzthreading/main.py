from jwzthreading import Message, thread

def print_container(ctr, depth=0, debug=0):
    """Print summary of Thread to stdout."""
    if 'message' in ctr:
        if debug:
            message = repr(ctr) + ' ' + repr(ctr['message'] and ctr['message'].subject)
        else:
            message = str(ctr['message'] and ctr['message'].subject)
    else:
        message = str(ctr)

    print(''.join(['> ' * depth, message]))

    for child in ctr.children:
        print_container(child, depth + 1, debug)

def main():
    import mailbox
    import sys

    msglist = []

    print('Reading input file...')
    mbox = mailbox.mbox(sys.argv[1])
    for message in mbox:
        try:
            parsed_msg = Message(message)
        except ValueError:
            continue
        msglist.append(parsed_msg)

    print('Threading...')
    threads = thread(msglist)

    print('Output...')
    for container in threads:
        print_container(container)


if __name__ == "__main__":
    main()
