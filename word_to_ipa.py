import epitran
import pandas as pd

# https://github.com/dmort27/epitran/tree/master
# usage example
epi = epitran.Epitran('deu-Latn')
print(epi.transliterate(u'Deutsch'))


# Add column in dataset for IPA pronunciation, iterating through the dataset to apply epi
def ipa_generation():
    df = pd.read_csv('german_words_dataset.csv')

    # Create new column with IPA pronunciation for singular version of the word
    # This is done so far to avoid handling words with no plural
    df['IPA'] = '' 
    for index, row in df.iterrows():
        df.at[index, 'IPA'] = epi.transliterate(row['German_Singular'])

    df.to_csv('german_words_dataset.csv', index=True)


ipa_generation()