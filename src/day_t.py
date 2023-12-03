class DayT(unittest.TestCase):
    """A short description of the storyline

    """
    
    def test_part_one(self):
        """
        In this example, the test values are 
            
    
        Adding these together produces .
        """

        TEST = """
"""

        TEST_CANDIDATES = []
        TEST_SUM = None
        
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
