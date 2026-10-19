from resvg import render, usvg
from affine import Affine


def renderSVGtoPNG(svgFile, fontfamily="Space Mono", outputFile="output.png"):
    with open(svgFile, "r") as f:
        svg = f.read()

    options = usvg.Options.default()
    options.load_system_fonts()
    options.font_family = fontfamily

    tree = usvg.Tree.from_str(svg, options)
    data = render(tree, tuple(Affine.identity())[0:6])

    with open(outputFile, "wb") as out:
        out.write(bytes(data))
