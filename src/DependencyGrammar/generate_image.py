from spacy import displacy
import cairosvg
from io import BytesIO
from PIL import Image

def generate_dependency_tree_image(nlp, sentence):
    doc = nlp(sentence)
    # Generate a static image of the dependency tree in SVG format
    svg = displacy.render(doc, style="dep", jupyter=False)
    # Convert the SVG to a PNG image using cairosvg
    png_data = cairosvg.svg2png(bytestring=svg.encode("utf-8"))
    return png_data

def resize_image(png_data, width, height):
    # Load the image and resize it proportionally to fit within the specified width and height
    img = Image.open(BytesIO(png_data))
    img_width, img_height = img.size
    resize_ratio = min(width / img_width, height / img_height)
    new_width = int(img_width * resize_ratio)
    new_height = int(img_height * resize_ratio)
    img_resized = img.resize((new_width, new_height), Image.ANTIALIAS)
    return img_resized
