from aocd.models import Puzzle
from collections import defaultdict, Counter

class Day2(unittest.TestCase):
    """A Cube Conundrum

    """
    
    def test_part_one(self):
        """
        In this example, the test values are 
            
    
        Adding these together produces .
        """

        TEST = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

        TEST_CANDIDATES = []
        TEST_SUM = 8
        
        self.assertEqual(func1(TEST),TEST_CANDIDATES)
        self.assertEqual(func2(TEST_CANDIDATES),TEST_SUM)
    

    def test_part_two(self):
        """
        In this example, the test values are 
            
    
        Adding these together produces .
        """

        TEST = """
"""

        TEST_CANDIDATES = []
        TEST_SUM = None
        
        self.assertEqual(func1(TEST,True),TEST_CANDIDATES)
        self.assertEqual(func2(TEST_CANDIDATES),TEST_SUM)

    def test_part_two_edge_cases(self):
        """
        In this example, the test values are 
            
    
        Adding these together produces .
        """

        TEST = """
"""

        TEST_CANDIDATES = []
        TEST_SUM = None
        
        self.assertEqual(func1(TEST,True),TEST_CANDIDATES)
        self.assertEqual(func2(TEST_CANDIDATES),TEST_SUM)


    def test_part_one_gold_star(self):
        """
        What is the final question?
        """

        PATH = '/workspaces/adventofcode-2023/data/'
        FILENAME = '1_inputs.txt'

        GOLD_STAR = None


        self.assertEqual(part1(PATH,FILENAME,TRANSLATE),GOLD_STAR)

    def test_part_two_gold_star(self):
        """
        What is the final question?
        """

        PATH = '/workspaces/adventofcode-2023/data/'
        FILENAME = '1_inputs.txt'

        GOLD_STAR = None


        self.assertNotEqual(part2(PATH,FILENAME,TRANSLATE),GOLD_STAR)

def split_lines(input):
    return input.split('\n')

def load_puzzle(day):
    puzzle = Puzzle(2023,day)
    inputs = split_lines(puzzle.input_data)
    return inputs

def parse(puzzle_input):
    inputs = split_lines(puzzle_input)

    selections = []
    for example in inputs:
        record = example.split(": ")
        game, cubes = record[0],record[1]
        sets_of_cubes = cubes.split("; ")
        selections = [s.split(', ') for s in sets_of_cubes]

    nums = []
    colors = []
    for s in selections:
        for i in s:
            cubes = i.split(' ')
            num, color = cubes[0], cubes[1]
            nums.append(float(num))
            colors.append(color)
    # return game and lzcn?
    return list(zip(colors, nums))
    
def color_stuff(s):    
    dd = defaultdict(float)
    for color,nums in s:
        dd[color] += nums
                
    return sorted(dd.items())

def difference(benchmark, game):
    benchmark = {k:v for k,v in benchmark}
    game = {k:v for k,v in game}

    diff = {k: benchmark[k] - game.get(k,0) for k in benchmark}

    return diff

def is_possible(diff):
    return not(any(value > 0 for value in diff.values()))

BENCHMARK = [('red', 12), ('green', 13), ('blue', 14)]
def part_1(data,benchmark):
    s = parse(data)
    g = color_stuff(s)
    b = difference(benchmark,g)
    return is_possible(b)

def part_2(data):
    pass

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution_1 = part_1(data)
    solution_2 = part_2(data)
    
    return solution_1, solution_2



