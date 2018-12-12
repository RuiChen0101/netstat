def get_fd(connect):
    return str(connect[0])

def get_family(connect):
    return srt(connect[1])

def get_type(connect):
    return srt(connect[2])

def get_local_address(connect):
    if len(connect[3])==0:
        return '*'
    else:
        return str(connect[3][0])

def get_local_port(connect):
    if len(connect[3])==0:
        return '*'
    else:
        return str(connect[3][1])

def get_remote_address(connect):
    if len(connect[4])==0:
        return '*'
    else:
        return str(connect[4][0])

def get_remote_port(connect):
    if len(connect[4])==0:
        return '*'
    else:
        return str(connect[4][1])

def get_status(connect):
    return connect[5]

def get_pid(connect):
    return connect[6]
