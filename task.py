def add_station(line, name: str, x: float, y: float, interchanges: list):
    line[name] = {"latitude": x, "longitude": y, "interchange_stations" : interchanges}
    return line

def remove_station(line, name:str):
    line.pop(name, None)
    return line

def add_interchange(line, name: str, interchange_name: str):
    line[name]["interchange_stations"].append(interchange_name)
    return line

def remove_interchange(line, name: str, interchange_name: str):
    line[name]["interchange_stations"].remove(interchange_name)
    return line

class LineBuilder(object):
    def __init__(self):
        pass

    def create_line(self):
        return dict()


class Network(object):
    def __init__(self, line_builder: LineBuilder):
        self._lines = []
        self.line_builder = line_builder

    def _get_lines(self):
        return self._lines

    def _add_line(self):
        return self._lines.append(line_builder.create_line())


def all_network_interchange_nodes(net):
    results = {}
    for line in net._get_lines():
        for station, features in line.items():
            if features["interchange_stations"]:
                results[station] = features["interchange_stations"]
    return results

line_builder = LineBuilder()
network = Network(line_builder)

network._add_line()
network._add_line()

add_station(network._get_lines()[0], "Арбатская", 56.0, 38.0, [])
add_station(network._get_lines()[1], "Библиотека им. Ленина", 56.0, 38.0, ["Арбатская"])

add_interchange(network._get_lines()[0], "Арбатская", "Библиотека им. Ленина")

print(all_network_interchange_nodes(network))