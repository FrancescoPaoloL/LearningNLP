from load_model import load_nlp_model
from generate_image import generate_dependency_tree_image
from display_image import display_dependency_tree_image

def draw_dependency_tree(sentence, model_name="en_core_web_sm"):
    nlp = load_nlp_model(model_name)
    png_data = generate_dependency_tree_image(nlp, sentence)
    display_dependency_tree_image(png_data)
