from constants import *
import pandas as pd

def get_id_dict(dataset: str) -> dict:
    '''
    We need to ensure axes are always aligned between different numpy arrays of comparions.
    This functions takes a dataset and returns a dictionary of subsets and example id's we can use for this.
    '''
    data = pd.read_json(f"{gdrive_path}/model_harvesting/prompts/{dataset}-theirs-compare.jsonl", orient="records", lines=True)

    id_dict = {}
    for article in sorted(data["article_id"].unique().tolist()):
        system_ids = data.loc[data["article_id"] == article, "system_id"].tolist()
        system_ids = sorted(list(set([x for pair in system_ids for x in pair])))
        id_dict[article] = system_ids

    return id_dict