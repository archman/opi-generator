import os
import toml


def get_attr_conf():
    """ Return a dict of the attribute map from BOY to BOB.

    Read default config from '/etc/opigen/attr.toml', if failed,
    read from '<package-directory>/config/attr.toml'.

    If 'attr.toml' exists in current working directory, read it
    to override the default config, otherwise, override with
    '~/.opigen/attr.toml' if available.
    """
    if os.path.isfile("/etc/opigen/attr.toml"):
        deployed_conf = toml.load("/etc/opigen/attr.toml")
    else:
        basedir = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(basedir, "attr.toml")
        deployed_conf = toml.load(path)
    # check if user-defined config exists
    _cwd_confpath = os.path.abspath("./attr.toml")
    if os.path.isfile(_cwd_confpath):
        _confpath = _cwd_confpath
    else:
        _user_confpath = os.path.expanduser("~/.opigen/attr.toml")
        if os.path.isfile(_user_confpath):
            _confpath = _user_confpath
        else:
            return deployed_conf
    # override
    _user_conf = toml.load(_confpath)
    for k, v in _user_conf.items():
        _d = deployed_conf.setdefault(k, {})
        for _k, _v in v.items():
            _d[_k] = _v
    return deployed_conf
