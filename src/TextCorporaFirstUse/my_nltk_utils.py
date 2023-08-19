import nltk
import yaml

def load_resources_from_yaml(yaml_file):
    with open(yaml_file, 'r') as file:
        resources = yaml.safe_load(file)
    return resources

def ensure_nltk_downloads(yaml_file):
    resources = load_resources_from_yaml(yaml_file)

    for resource in resources:
        resource_path = resource['resource_path']
        resource_name = resource['resource_name']
        #description = resource['description']

        if not nltk.data.find(resource_path):
            nltk.download(resource_name)

