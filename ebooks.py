import random
import re
import textwrap
from english import Stopwords
from text.blob import TextBlob, Sentence

from tokenizer import WordTokenizer

class EbooksQuotes(object):

    def __init__(
        self, keywords=None, probability=0.001,
        minimum_quote_size=8, maximum_quote_size=140,
        wrap_at=30, truncate_chance=1.0/4):
        keywords = keywords or []
        self.keywords = [x.lower() for x in keywords]
        self.probability = probability
        self.minimum_quote_size = minimum_quote_size
        self.maximum_quote_size = maximum_quote_size
        self.wrap_at = wrap_at
        self.truncate_chance = truncate_chance
        self._blobs = {}

    SEVERAL_CAPITALIZED_WORDS = re.compile("(([A-Z][a-zA-Z]+,? ){2,}[A-Z][a-zA-Z]+[!?.]?)")

    # Ways of further tweaking a quote.
    def one_sentence_from(self, quote):
        """Reduce the given quote to a single sentence.
        
        The choice is biased against the first sentence, which is less likely
        to be the start of a real in-text sentence.
        """
        blob = TextBlob(quote)
        try:
            sentences = blob.sentences
        except Exception, e:
            # TextBlob can't parse this. Just return the whole string
            return quote
        if len(sentences) > 1 and len(sentences[-1]) < 10:
            # Don't choose a very short sentence if it's at the end of a chunk.
            sentences = sentences[:-1]
        s = random.choice(sentences)
        if s == sentences[0]:
            s = random.choice(sentences)
            if s == sentences[0]:
                s = random.choice(sentences)

        return s

    def remove_ending_punctuation(self, string):
        # Notably absent: dash and colon, which make a quote
        # funnier.
        if string.count('"') == 1:
            string = string.replace('"', "")
        string = string.replace("_", "")
        while string and string[-1] in ',; ':
            string = string[:-1]
        return string

    def truncate_at_stopword(self, string):
        # Truncate a string at the last stopword not preceded by
        # another stopword.
        # print "%s =>" % string

        if type(string) == Sentence:
            words = string.words
        else:
            try:
                words = TextBlob(string).sentences
            except Exception, e:
                # TextBlob can't parse this. Just return the whole string
                return string

        reversed_words = list(reversed(words[2:]))
        for i, w in enumerate(reversed_words):
            if (w in Stopwords.MYSQL_STOPWORDS                
                and i != len(reversed_words)-1 and
                not reversed_words[i+1] in Stopwords.MYSQL_STOPWORDS):
                # print "Stopword %s (previous) %s" % (w, reversed_words[i+1])
                r = re.compile(r".*\b(%s)\b" % w)
                string = unicode(string)
                m = r.search(string)
                if m is not None:
                    string = string[:m.span(1)[0]]
                # print "=> %s" % string
                # print "---"
                break
        return string


    def quotes_in(self, paragraph):
        para = textwrap.wrap(paragraph, self.wrap_at)
        if len(para) == 0:
            return

        probability = self.probability
        if para[0][0].upper() == para[0][0]:
            # We greatly prefer lines that start with capital letters.
            probability *= 5
        else:
            probability /= 4

        gathering = False
        in_progress = None
        for i in range(len(para)):
            line = para[i]
            if gathering:
                # We are currently putting together a quote.
                done = False
                if (random.random() < self.truncate_chance 
                    and len(in_progress) >= self.minimum_quote_size):
                    # Yield a truncated quote.
                    done = True
                else:
                    potential = in_progress + ' ' + line.strip()
                    if len(potential) >= self.maximum_quote_size:
                        # That would be too long. We're done.
                        done = True
                    else:
                        in_progress = potential

                if done:
                    quote = in_progress
                    in_progress = None
                    gathering = done = False

                    # Miscellaneous tweaks to increase the chance that
                    # the quote will be funny.
                    if random.random() < 0.6:
                        quote = self.one_sentence_from(quote)

                    if random.random() < 0.4:
                        quote = self.truncate_at_stopword(quote)

                    # Quotes that end with two consecutive stopwords
                    # are not funny. It would be best to parse every
                    # single quote and make sure it doesn't end with
                    # two consecutive stopwords. But in practice it's
                    # much faster to just check for the biggest
                    # offenders, which all end in 'the', and then trim
                    # the 'the'.
                    low = quote.lower()
                    for stopwords in ('of the', 'in the', 'and the',
                                      'in the', 'on the', 'for the'):
                        if low.endswith(stopwords):
                            quote = quote[:len(" the")-1]
                            break

                    quote = unicode(quote)
                    quote = self.remove_ending_punctuation(quote)

                    if (len(quote) >= self.minimum_quote_size
                        and len(quote) <= self.maximum_quote_size):
                        yield quote
            else:
                # We are not currently gathering a quote. Should we
                # be?
                r = random.random()
                if random.random() < probability * 50:
                    # Run the regular expression and see if it matches.
                    m = self.SEVERAL_CAPITALIZED_WORDS.search(line)
                    if m is not None:
                        phrase = m.groups()[0]
                        if "Gutenberg" in phrase or "Proofreader" in phrase:
                            # Part of the meta, not part of text.
                            continue
                        # Tag the text to see if it's a proper noun.
                        blob = TextBlob(phrase)
                        tags = blob.tags
                        proper_nouns = [x for x, tag in tags if tag.startswith('NNP')]
                        if len(proper_nouns) < len(tags) / 3.0:
                            # We're good.
                            yield phrase

                matches = self._line_matches(line)
                if matches or random.random() < probability:
                    gathering = True
                    if matches:
                        # A keyword match! Start gathering a quote either
                        # at this line or some earlier line.
                        maximum_backtrack = (
                            self.maximum_quote_size / self.wrap_at) - 1
                        backtrack = random.randint(0, maximum_backtrack)
                        start_at = max(0, i - backtrack)
                        in_progress = " ".join(
                            [x.strip() for x in para[start_at:i+1]])
                    else:
                        in_progress = line.strip()
                    

    def _line_matches(self, line):
        l = line.lower()
        for keyword in self.keywords:
            if keyword in l:
                return True
        return False

