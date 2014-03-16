import sys
inPy3k = sys.version_info[0] == 3

if not inPy3k:
    import ConfigParser
    from ConfigParser import SafeConfigParser
    import StringIO
    maxint = sys.maxint
    string_types = basestring
else:
    import configparser as ConfigParser
    from configparser import ConfigParser as SafeConfigParser
    import io as StringIO
    maxint = sys.maxsize
    string_types = (str, bytes)
