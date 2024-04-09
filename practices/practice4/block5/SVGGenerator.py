# Реализовать прототип библиотеки для рисования в формате SVG.

Color = 'red' or 'green' or 'blue' or 'black'

class SVGLine:
    def __init__(self, x1: float, y1: float, x2: float, y2: float, stroke: Color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.stroke = stroke

    def generate_svg(self) -> str:
        return (f'<line x1="{self.x1}" y1="{self.y1}" x2="{self.x2}" '
                f'y2="{self.y2}" stroke="{self.stroke}" />\n')


class SVGCircle:
    def __init__(self, cx: float, cy: float, r: float, fill: Color):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.fill = fill

    def generate_svg(self) -> str:
        return (f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.r}" '
                f'fill="{self.fill}" />\n')


class SVG:
    def __init__(self):
        self.elements = []

    def line(self, x1: float, y1: float, x2: float, y2: float, stroke: Color) -> None:
        self.elements.append(SVGLine(x1, y1, x2, y2, stroke))

    def circle(self, cx: float, cy: float, r: float, fill: Color) -> None:
        self.elements.append(SVGCircle(cx, cy, r, fill))

    def save(self, filename: str, width: float, height: float) -> None:
        markup = (f'<svg version="1.1" width="{width}" height="{height}" '
                  f'xmlns="http://www.w3.org/2000/svg">\n')

        for element in self.elements:
            markup += element.generate_svg()

        markup += '</svg>\n'

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(markup)


def main():
    svg = SVG()

    svg.line(10, 10, 60, 10, 'black')
    svg.line(60, 10, 60, 60, 'black')
    svg.line(60, 60, 10, 60, 'black')
    svg.line(10, 60, 10, 10, 'black')

    svg.circle(10, 10, 5, 'red')
    svg.circle(60, 10, 5, 'red')
    svg.circle(60, 60, 5, 'red')
    svg.circle(10, 60, 5, 'red')

    svg.save('pic.svg', 100, 100)


if __name__ == '__main__':
    main()
