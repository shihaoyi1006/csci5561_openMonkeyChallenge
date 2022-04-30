import json
import numpy as np
from unicodedata import category

def get_single_json(file, species, bbox, landmarks):
    new_json = {"file":file,
                "species":species,
                "bbox":bbox,
                "landmarks":landmarks}
    return new_json


def main():
    filepath = "./test_prediction.json"
    export_new_path = "./test_new_monkey.json"
    export_old_path = "./test_old_monkey.json"
    export_ape_path = "./test_ape.json"
    export_new = {}
    export_old = {}
    export_ape = {}
    export_new["data"] = []
    export_old["data"] = []
    export_ape["data"] = []
    with open(filepath, 'r') as fp:
	    information = json.load(fp)
    len_data = len(information["data"])
    for index in range(len_data):
        file = information["data"][index]["file"]
        
        species = information["data"][index]["species"]
        bbox = information["data"][index]["bbox"]
        landmarks = information["data"][index]["landmarks"]
        #visibility = information["data"][index]["visibility"]
        
        if species == "Emperor_tamarin" or species == "Golden_lion_tamarin" or species == "Tufted_capuchin" or species == "Common_marmoset" or species == "Cotton-top_tamarin" or species == "Squirrel_monkey" or species == "":
            new_json = get_single_json(file, species, bbox, landmarks)
            export_new["data"].append(new_json)
        if species == "Chacma_baboon" or species == "Crab-eating_macaque" or species == "Hamadryas_baboon" or species=="Japanese_macaque" or species == "Lion-tailed_macaque" or species == "Mandrill" or species == "Olive_baboon" or species == "Proboscis_monkey" or species == "Rhesus_macaque" or species == "Vervet_monkey" or species == "Formosan_rock_macaque" or species == "Dusky_leaf_monkey" or species == "Golden_snub-nosed_monkey" or species == "Barbary_macaque":
            new_json = get_single_json(file, species, bbox, landmarks)
            export_old["data"].append(new_json)
        if species == "Gibbon" or species == "Siamang" or species == "Bonobo" or species == "Orangutan" or species =="Chimpanzee" or species == "Gorilla":
            new_json = get_single_json(file, species, bbox, landmarks)
            export_ape["data"].append(new_json)
        
        
    with open(export_new_path, 'w') as fp:
	    json.dump(export_new, fp, indent=4)
    with open(export_old_path, 'w') as fp:
	    json.dump(export_old, fp, indent=4)
    with open(export_ape_path, 'w') as fp:
	    json.dump(export_ape, fp, indent=4)
        
    
    
    
    
    
    
if __name__ == '__main__':
    main()