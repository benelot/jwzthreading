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


def get_thread_length(ctr, depth=0):
    base_list = get_thread_indices(ctr)
    return len(base_list)


def get_thread_indices(ctr):
    base_list = []
    return get_thread_indices_sub(ctr, base_list, 0)


def get_thread_indices_sub(ctr, base_list, depth=0):
    if ctr['message'] is not None:
        message_id = ctr['message'].message_id
        base_list.append(message_id)

    for child in ctr.children:
        get_thread_indices_sub(child, base_list, depth + 1)

    return base_list


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

    # print('Output...')
    # for container in threads:
    #     print_container(container)

    thread_length = {}

    for container in threads:
        length = get_thread_length(container)
        if length + 1 not in thread_length:
            thread_length[length + 1] = 1
        else:
            thread_length[length + 1] += 1

    print("\n\nThread lengths:")
    for i in sorted(thread_length):
        print("Length:" + str(i + 1) + "   #:" + str(thread_length[i]))

    idx_list = []
    for container in threads:
        thread_idx_list = get_thread_indices(container)
        idx_list.append(thread_idx_list)

    print("Total number of threads: ", len(idx_list))


if __name__ == "__main__":
    main()
