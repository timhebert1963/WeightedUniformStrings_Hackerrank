# Hackerrank - Weighted Uniform Strings
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem
import time

class SubWeights():
    def __init__(self, s):
        self.swl = len(s)  # sub_weight length

        self.alpha  = list(map(chr, range(97,123)))    # chr, range(97,123) generates alphabet.

        self.max_sub_weight = [0 for _ in range(26)]   # highest sub string weight will be assigned
                                                       # to respective index.

        self.previous = ''  # previous character in string s.

    def calculateSubWeights(self, s):
        for i in range(self.swl):

            char_index  = self.alpha.index(s[i])    # alphabet character index in array self.alpha.
            char_weight = char_index + 1            # alphabet character weight.

            if s[i] == self.previous:
                sub_weight += char_weight    # current sub string weight
            
            else:
                self.previous = s[i]
                sub_weight = char_weight     # current sub string weight

            if self.max_sub_weight[char_index] < sub_weight:
                self.max_sub_weight[char_index] = sub_weight    # assign max weight

    def findSubWeight(self, queries):
        ql = len(queries)
        result = ['No' for _ in range(ql)]    # initialize all result array indeces to 'No'

        # array queries index loop.
        for i in range(ql):
            q = queries[i]

            # array self.max_sub_weight index loop.
            for j in range(26):

                # j+1 is weight of alphabet character in array self.alpha.
                if q % (j+1) == 0 and q <= self.max_sub_weight[j]:
                    result[i] = 'Yes'
                    break

        return result

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):

    sw = SubWeights(s)
    sw.calculateSubWeights(s)
    return sw.findSubWeight(queries)

def getTime():
    return int(time.time())

def convertSeconds(s):
    return s // 60, s % 60  # minutes = s // 60, seconds = s % 60

def testResults(test, start_time, expected, result):
    
    end_time = getTime()                         # used to measure time to execute each test case.
    seconds = end_time - start_time              # total execution time in seconds.
    minutes, seconds = convertSeconds(seconds)   # execution time converted to minutes and seconds.

    if result == expected:
        status = 'PASS'    # test results match expected results
    else:
        status = 'FAIL'    # test results do not match expected results

    print("{:10s}   {:6s}    total time to execute == {:2d} minutes {:2d} seconds".format(test, status, minutes, seconds))

def main():

    ##########################################################################################
    #
    # 'sample 0' and 'sample 1' are from Hackerrank sample tests
    # 'Testcase 2' and 'Testcase 3' are actual test cases from Hackerrank
    #
    # 
    # TC2_35634_queries_weightedUniformStrings.py needs to be imported for demo purposes
    # TC3_21086_queries_weightedUniformStrings.py needs to be imported for demo purposes
    # elif test == 'Testcase 2':
    #     from TC2_35634_queries_weightedUniformStrings import string, queries, expected
    # elif test == 'Testcase 3':
    #     from TC3_21086_queries_weightedUniformStrings import string, queries, expected
    #
    ##########################################################################################
    test_case_list = ['sample 0', 'sample 1', 'Testcase 2', 'Testcase 3']

    # Test Results Legend
    print('\n')
    print("{:10s}   {}    {}".format('Test Case', 'Status', 'Execution Time'))

    for test in test_case_list:

        if test == 'sample 0':
            string   = 'abccddde'
            queries  = [1, 3, 12, 5, 9, 10]
            expected = ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'No']

        elif test == 'sample 1':
            string   = 'aaabbbbcccddd'
            queries  = [9, 7, 8, 12, 5]
            expected = ['Yes', 'No', 'Yes', 'Yes', 'No']

        elif test == 'Testcase 2':
            from TC2_35634_queries_weightedUniformStrings import string, queries, expected

        elif test == 'Testcase 3':
            from TC3_21086_queries_weightedUniformStrings import string, queries, expected

        start_time = getTime()  # used to measure time to execute each test case

        result = weightedUniformStrings(string, queries)  # execute test

        testResults(test, start_time, expected, result)  # display test results

if __name__ == '__main__':
    main()



