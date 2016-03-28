import errno
import sys
import os
import StringIO


#@staticmethod
def error_text(errnumber):
    return '%s: %s' % (errno.errorcode[errnumber], os.strerror(errnumber))

# Print message and return to caller
# caller specifies "errnoflag" and "level"
#@staticmethod
def err_doit(errnoflag, level, fmt, *args):


    errno_save = errno  # value caller might want printed

    buf = StringIO.StringIO()
    if (len(args) <= 1):
        buf.write(fmt)
    else:
        buf.write(fmt % args)

    n = len(args);

    if (errnoflag):
        printstr = error_text(errno_save.ENODEV)
        printstr = buf.getvalue() + printstr

    printstr += '\n'

    sys.stderr.write(printstr)
'''

    if (daemon_proc) {
        syslog(level, buf);
    } else {
        fflush(stdout);     // in case stdout and stderr are the same
        fputs(buf, stderr);
        fflush(stderr);
    }
'''




'''
// Fatal error related to system call
// print message and terminate
'''
def err_sys(fmt, *args):

    err_doit(1, 0, fmt, args)
    exit(1)




