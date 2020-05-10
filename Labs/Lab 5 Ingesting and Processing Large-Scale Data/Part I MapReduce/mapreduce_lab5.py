'''
Lab 5 (Part I): Batch Processing Data with MapReduce

What's the most used word in 5-star customer reviews on Amazon?

We can answer this question using the mrjob package to investigate customer
reviews available as a part of Amazon's public S3 customer reviews dataset.

For this demo, we'll use a small sample of this 100m+ review dataset that
Amazon provides (s3://amazon-reviews-pds/tsv/sample_us.tsv).

In order to run the code below, be sure to `pip install mrjob` if you have not 
done so already.
'''

from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

class MRMostUsedWord(MRJob):

    def mapper_get_words(self, _, row):
        '''
        If a review's star rating is 5, yield all of the words in the review
        '''
        data = row.split('\t')
        if data[7] == '5':
            for word in WORD_RE.findall(data[13]):
                yield (word.lower(), 1)

    def combiner_count_words(self, word, counts):
        '''
        Sum all of the words available so far
        '''
        yield (word, sum(counts))

    def reducer_count_words(self, word, counts):
        '''
        Arrive at a total count for each word in the 5 star reviews
        '''
        yield None, (sum(counts), word)

    # discard the key; it is just None
    def reducer_find_max_word(self, _, word_count_pairs):
        '''
        Yield the word that occurs the most in the 5 star reviews
        '''
        yield max(word_count_pairs)

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   combiner=self.combiner_count_words,
                   reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_find_max_word)
        ]

if __name__ == '__main__':
    MRMostUsedWord.run()
