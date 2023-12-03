import os
import re
import unittest

WORD_DIGIT_DICT = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}

class DayOne(unittest.TestCase):
    """The Elves need your help to restore snow production by amending calibration numbers

    """
    
    def test_part_one(self):
        """
        In this example, the calibration values of these four lines are 
            12, 38, 15, and 77. 
    
        Adding these together produces 142.
        """

        TEST = """1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet"""

        TEST_CANDIDATES = [12,38,15,77]
        TEST_SUM = 142
        
        self.assertEqual(find_candidates(TEST),TEST_CANDIDATES)
        self.assertEqual(sum_candidates(TEST_CANDIDATES),TEST_SUM)
    

    def test_part_two(self):
        """
        In this example, the calibration values are 
            29, 83, 13, 24, 42, 14, and 76. 
        
        Adding these together produces 281.
        """
        PATH = '/workspaces/adventofcode-2023/data/'
        FILENAME = 'inputs.txt'

        test = """two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen"""

        
        test_candidates = [29, 83, 13, 24, 42, 14, 76]
        test_sum = 281
        
        self.assertEqual(find_candidates(test,True),test_candidates)
        self.assertEqual(sum_candidates(test_candidates),test_sum)

    def test_part_two_edge_cases(self):

        """
        In this example, the calibration values are 
            29, 83, 13, 24, 42, 14, and 76. 
        
        Adding these together produces 281.
        """

        test = """eighthree
        sevenine
        two1ninesix"""

        test_candidates = [83, 79, 26]
        test_sum = 188
        
        self.assertEqual(find_candidates(test,True),test_candidates)
        self.assertEqual(sum_candidates(test_candidates),test_sum)

    def test_part_one_gold_star(self):
        """
        What is the sum of all of the calibration values?
        """

        PATH = '/workspaces/adventofcode-2023/data/'
        FILENAME = '1_inputs.txt'
        TRANSLATE = False

        GOLD_STAR = 55607


        self.assertEqual(day1(PATH,FILENAME,TRANSLATE),GOLD_STAR)

    def test_part_two_gold_star(self):
        """
        What is the sum of all of the calibration values?
        """

        PATH = '/workspaces/adventofcode-2023/data/'
        FILENAME = '1_inputs.txt'
        TRANSLATE = True


        GOLD_STAR = 55309


        self.assertNotEqual(day1(PATH,FILENAME,TRANSLATE),GOLD_STAR)

def load_inputs(path,filename):
    file_path = os.path.join(path, filename)

    with open(file_path, "r") as file:
        file_contents = file.read()

    return file_contents

def split_lines(input):
    return input.split('\n')

def find_digits(val):
    d = [v for v in val if v.isdigit()]
    return d

def extract_first_and_last_digits(list_of_digits):
    return list_of_digits[0],list_of_digits[-1]

def stringify_and_concat(first,last):
    return str(first) + str(last)

def translate_number_to_digit(adict, text):
    regex = re.compile("|".join(map(re.escape, adict.keys(  ))))
    return regex.sub(lambda match: adict[match.group(0)], text)

def parse_inputs(input,translate=False):
    inputs_clean = split_lines(input)

    if translate == True:
        parsed = []
        for i in inputs_clean:
            parsed.append(translate_number_to_digit(WORD_DIGIT_DICT,i))
        
        return parsed    

    return inputs_clean

def find_candidates(input,translate=False):
    inputs_clean = parse_inputs(input,translate)
    candidates = []
    for i in inputs_clean:
        nums = find_digits(i)
        first, last = extract_first_and_last_digits(nums)
        first_last = stringify_and_concat(first,last)
        candidates.append(int(first_last))
    
    return candidates

def sum_candidates(candidates):
    return sum(candidates)

def day1(path,filename,translate=False):
    inputs = load_inputs(path,filename)
    candidates = find_candidates(inputs,translate)
    return sum_candidates(candidates)

if __name__ == "__main__":
    unittest.main(argv=[''],verbosity=3)