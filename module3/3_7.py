# Вам дано описание пирамиды из кубиков в формате XML.
# Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
# Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
# Пример:
# <cube color="blue">
#   <cube color="red">
#     <cube color="green">
#     </cube>
#   </cube>
#   <cube color="red">
#   </cube>
# </cube>
# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML
# документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2.
# Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.
# Ценность цвета равна сумме ценностей всех кубиков этого цвета.
# Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

from xml.etree.ElementTree import XMLParser


class MaxDepth:                     # The target object of the parser
    maxDepth = 0
    res = {}
    depth = 0

    def start(self, tag, attrib):   # Called for each opening tag.
        self.depth += 1
        if attrib["color"] not in self.res:
            self.res[attrib["color"]] = self.depth
        else:
            self.res[attrib["color"]] += self.depth

    def end(self, tag):             # Called for each closing tag.
        self.depth -= 1

    def data(self, data):
        pass            # We do not need to do anything with data.

    def close(self):    # Called when all data has been parsed.
        return self.res


target = MaxDepth()
parser = XMLParser(target=target)
exampleXml = input()

parser.feed(exampleXml)
rgb = parser.close()
print(rgb["red"], rgb["green"], rgb["blue"])
