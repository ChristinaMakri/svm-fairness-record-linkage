import string
import random
import pandas as pd

def random_alteration(s):
    """Applies a random character modification to a string."""
    if not isinstance(s, str) or len(s) == 0:
        return s
    r = random.randrange(len(s))
    random_selection = random.randint(1, 3)
    if random_selection == 1:
        return s[:r] + s[r+1:]
    elif random_selection == 2:
        return s[:r] + random.choice(string.ascii_uppercase) + s[r+1:]
    else:
        return s[:r+1] + random.choice(string.ascii_uppercase) + s[r+1:]

def create_altered_dataset(input_path, output_path):
    df = pd.read_csv(input_path)
    altered = {'NAME': [], 'SURNAME': []}
    for i in df.index:
        altered['NAME'].append(random_alteration(df.loc[i, "NAME"]))
        altered['SURNAME'].append(random_alteration(df.loc[i, "SURNAME"]))
    df_altered = pd.DataFrame(altered)
    df_altered.to_csv(output_path, index=False)

# Example usage:
# create_altered_dataset('data/original.csv', 'data/altered.csv')
