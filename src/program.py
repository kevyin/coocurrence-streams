import os
import re
import sys
import time
import traceback
import subprocess
import os.path
from optparse import OptionParser

def cooccurrence(words, wordA, wordB, K=3):
    pass

def count_words(words, wordA):
    return words.get_cnt(wordA.lower())


def cooccurrence_prob(words, A, B, k):
    return cooccurrence(words, A, B, k) / count_words(words, A)


class Words:

    def __init__(self, mywords):
        words = []
        word_cnts = {}
        words = mywords
        for word in words:
            pattern = re.compile('[\W_]+')
            word = pattern.sub('', word.lower())
            if word_cnts.has_key(word):
                word_cnts[word] += 1
            else:
                word_cnts[word] = 1

        ### Important Magic ###
        # Assigns the local symbol table into self
        vars(self).update(locals())

    def get_cnt(self, word):
        return self.word_cnts[word] if self.word_cnts.has_key(word) else 0



#####################################################################################
# MAIN
def main():
    """Script Entry Point"""

    usage =  "\n\n%prog [options] "
    parser = OptionParser(usage=usage)
    parser.add_option("-w", "--workingDir",
                      dest="working_dir", default="./",
                      help="Working directory")
    parser.add_option("-j", "--cores",
                      dest="cores", default="32",
                      help="Number of cores to use")
    #parser.add_option("", "--extra-options",
    #dest="extra_options", default="",
    #help="Extra options to bcl2fastq")
    parser.add_option("", "--sge",
                      action="store_true", dest="sge",
                      help="submit as grid engine job")
    (opts, args) = parser.parse_args()

    output_dir = args[0]
    in_files = " ".join([os.path.abspath(p) for p in args[1:]])
    working_dir = os.path.abspath(opts.working_dir)
    print "Working dir: " + working_dir
    #print "Output dir: " + in_dir
    print "Output dir: " + output_dir
    print "input files: " + in_files

    runinfo = { "output_dir" : output_dir,
                "in_files" : in_files,
                #"extra_options" : opts.extra_options,
                "cores" : opts.cores }


###############################################################################
if __name__ == "__main__":
    main()
