import re
import sys
import itertools
from optparse import OptionParser


def format_word(word):
    word_pat = re.compile('[\W_]+')
    return word_pat.sub('', word.lower()).strip()


def word_pair_key(wordA, wordB, format=True):
    if format:
        return format_word(wordA) + '#' + format_word(wordB)
    else:
        return wordA + '#' + wordB


def cooccurrence(words, wordA, wordB):
    id = word_pair_key(wordA, wordB)
    return words.get_cooc(id)


def count_words(words, wordA):
    return words.get_word_cnt(wordA.lower().strip())


def cooccurrence_prob(words, A, B):
    countA = count_words(words, A)
    return round(float(cooccurrence(words, A, B)) / countA if countA != 0 else 0, 2)


class Words:

    def __init__(self, word_stream, k=1):
        set_k = k
        word_cnts = {}
        cooc = {}

        def format_words(uf_words):
            for word in uf_words:
                yield format_word(word)

        # words need to be formatted
        formatted_words_it = format_words(word_stream)
        # k streams for each direction and 1 in the middle
        total_it = 2*k+1
        word_its_ = itertools.tee(formatted_words_it, total_it)
        word_its = []

        for ws in itertools.izip(word_its_):
            for w in ws:
                word_its.append(w)

        # prep or offset the iterators
        # the kth is the "middle" stream.
        # offset first k ie stream no <k
        for n in range(0, k):
            cnt = k - n
            while cnt > 0:
                word_its[n].next()
                cnt = cnt - 1

        # pad the last k ie stream no >k
        for n in range(k+1, total_it):
                word_its[n] = itertools.chain([None]*(n-k), word_its[n])

        for words in itertools.izip_longest(*word_its):
            # kth word is the middle
            wordk = words[k]

            if wordk is not None:
                # update word counts
                if word_cnts.has_key(wordk):
                    word_cnts[wordk] += 1
                else:
                    word_cnts[wordk] = 1

                # update cooccurrence
                # get set of unique words in range k (but excluding k)
                uniq_ws = set(words[:k] + words[k+1:])
                for uw in uniq_ws:
                    if uw is not None:
                        id = word_pair_key(wordk, uw, format=False)
                        if cooc.has_key(id):
                            cooc[id] += 1
                        else:
                            cooc[id] = 1

        ### Important Magic ###
        # Assigns the local symbol table into self
        vars(self).update(locals())

    def get_word_cnt(self, word):
        return self.word_cnts[word] if self.word_cnts.has_key(word) else 0

    def get_cooc(self, key):
        return self.cooc[key] if self.cooc.has_key(key) else 0


#####################################################################################
# MAIN
def main():
    """Script Entry Point"""

    usage =  "\n\n%prog input.file k"
    parser = OptionParser(usage=usage)
    (opts, args) = parser.parse_args()

    input = args[0]
    k = int(args[1])

    # load_file(input, int(k))
    def readInput(inputfile):
        with open(inputfile, 'r') as f:
            for line in f.readlines():
                for word in line.split():
                    yield word
    input_words = Words(readInput(input), k)


    while True:
        line = sys.stdin.readline()
        words = line.split()
        # print "%.2f" % (prob(words[0].strip(), words[1].strip()))
        print "%.2f" % (cooccurrence_prob(input_words, words[0], words[1]))


###############################################################################
if __name__ == "__main__":
    main()
