import pandas as pd
import numpy as np
import recordlinkage as rl

def compute_similarity(original_path, altered_path, output_path):
    df1 = pd.read_csv(original_path)
    df2 = pd.read_csv(altered_path)

    indexer = rl.index.Full()
    pairs = indexer.index(df1, df2)

    comp = rl.Compare()
    comp.string('NAME', 'NAME', method='jarowinkler', label='name_sim')
    comp.string('SURNAME', 'SURNAME', method='jarowinkler', label='surname_sim')

    features = comp.compute(pairs, df1, df2)
    features.to_csv(output_path)

# Example usage:
# compute_similarity('data/original.csv', 'data/altered.csv', 'data/features.csv')
