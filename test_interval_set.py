import unittest
from interval_set import Interval

class IntervalTest(unittest.TestCase):

    def testOverlap1(self):
        """
        x------------x
              x----------x       
       
        x---------x 
                   x------x
        """
        
        interval = Interval(3,5) 
        interval2 =  Interval(2,4)
        self.assertEqual(Interval.OVERLAP_LEFT, interval._overlap(interval2))
        
        interval2 = Interval(1,3)
        self.assertEqual(Interval.OVERLAP_LEFT, interval._overlap(interval2))
        
        interval2 = Interval(1,2)
        self.assertEqual(Interval.NO_OVERLAP, interval._overlap(interval2))
        
        interval2 = Interval(6,8)
        self.assertEqual(Interval.NO_OVERLAP, interval._overlap(interval2))


    def testOverlap2(self):
        """
                 x------------x
           x--------x

                    x------------x
           x--------x

        """
          
        interval = Interval(3,5)
        interval2 = Interval(4,6)
        self.assertEqual(Interval.OVERLAP_RIGHT, interval._overlap(interval2))
        
        interval2 = Interval(5,6)
        self.assertEqual(Interval.OVERLAP_RIGHT, interval._overlap(interval2))
 
        interval2 = Interval(6,8)
        self.assertEqual(Interval.NO_OVERLAP, interval._overlap(interval2))
 
        interval2 = Interval(1,2)
        self.assertEqual(Interval.NO_OVERLAP, interval._overlap(interval2))
 

    def testOverlap3(self):
        """
             x-----x
           x-----------x 
        
        """ 

        interval = Interval(3,7)
        interval2 = Interval(4,6)
        self.assertEqual(Interval.OVERLAP_MIDDLE, interval._overlap(interval2))
        
        interval2 = Interval(3,6)
        self.assertEqual(Interval.OVERLAP_MIDDLE, interval._overlap(interval2)) 
    
        interval2 = Interval(1,2)
        self.assertEqual(Interval.NO_OVERLAP, interval._overlap(interval2))

        interval2 = Interval(8,9)
        self.assertEqual(Interval.NO_OVERLAP, interval._overlap(interval2))

        interval = Interval(1,5)
        interval2 = Interval(2,3)
        self.assertEqual(Interval.OVERLAP_MIDDLE, interval._overlap(interval2))

    
    def testOverlap4(self):
        """
           x-----------x 
             x-----x
        
        """ 
        interval = Interval(3,5)
        interval2 = Interval(3,7)
        self.assertEqual(Interval.OVERLAP_COVER, interval._overlap(interval2))
        

    def testMergeInterval(self):
        interval = Interval(3,5)
        interval2 = Interval(4,7)
        interval.merge(interval2)
        self.assertEqual(3, interval.get_start())
        self.assertEqual(7, interval.get_end())
        
        interval2 = Interval(1,3)
        interval.merge(interval2)
        self.assertEqual(1, interval.get_start())
        self.assertEqual(7, interval.get_end())
        
    def testSplit(self):       
        interval = Interval(1,5)
        interval2 = Interval(1,5)
        intervals = interval.split(interval2) 
        self.assertEqual(0, len(intervals))

        intervals = interval.split(Interval(4,6))
        self.assertEqual(1, len(intervals))
        new_interval = intervals[0]
        self.assertEqual(1, new_interval.get_start())
        self.assertEqual(4, new_interval.get_end())
        
        interval2 = Interval(2,3)    
        intervals = interval.split(interval2)
        self.assertEqual(2, len(intervals))


if __name__ == '__main__':
    unittest.main()
