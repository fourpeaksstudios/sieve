#!/usr/bin/env python3

import inkex

import svgpathtools


def isclosedac(p):
    return abs(p.start-p.end) < 1e-6


class Sieve(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)

        self.OptionParser.add_option(
            '-a', '--area', action='store', type='float', dest='area',
            help='Remove paths with an area smaller than this value'
        )

    def effect(self):
        self.options.area = self.unittouu(str(self.options.area) + 'px')
        if self.options.area == 0:
            return

        for path in self.document.xpath("//svg:path", namespaces=inkex.NSS):
            parsed_path = svgpathtools.parse_path(path.attrib["d"])

            if not isclosedac(parsed_path):
                continue

            area = parsed_path.area()

            if area < self.options.area:
                path.getparent().remove(path)


if __name__ == '__main__':
    e = Sieve()
    e.affect()
