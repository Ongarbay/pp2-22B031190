from configparser import ConfigParser


def configuration(filename="db.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        parametres = parser.items(section)
        for parameter in parametres:
            db[parameter[0]] = parameter[1]
    else:
        raise Exception(
            "Section {0} not found in the {1} file".format(section, filename))
    return db
