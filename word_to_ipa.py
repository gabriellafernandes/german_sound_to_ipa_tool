import epitran
from epitran.backoff import Backoff

# https://github.com/dmort27/epitran/tree/master
epi = epitran.Epitran('deu-Latn')
print(epi.transliterate(u'Deutsch'))

