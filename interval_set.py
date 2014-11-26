
class Interval:
    NO_OVERLAP = 0
    OVERLAP_LEFT = 1 
    OVERLAP_RIGHT = 2
    OVERLAP_COVER = 3
    OVERLAP_MIDDLE = 4

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_start(self):
        return self.start
  
    def get_end(self):
        return self.end 
    
    def overlap(self, interval):
        return self._overlap(interval) > 0
    
    def _overlap(self, interval):
        """
        There are 4 cases to consider for overlap intervals.
 
        1.  x--------x
                 x--------x
     
        2.       x------------x
            x--------x
    
        3.  x------------x
               x------x
    
        4.      x-----x
             x-----------x

        Return true if the intervals overlap, otherwise return false
        """
        overlap = self.NO_OVERLAP

        if interval.get_start() <= self.start and self.start <= interval.get_end():
            overlap = self.OVERLAP_LEFT
       
        if interval.get_end() >= self.end and interval.get_start() <= self.end: 
            overlap = self.OVERLAP_RIGHT
      
        if interval.get_start() <= self.start and  interval.get_end() >= self.end:
            overlap =  self.OVERLAP_COVER
 
        interval_size = interval.get_end() - interval.get_start()
        size = self.end - self.start

        if interval.get_start() >= self.start and interval.get_end() <= self.end and interval_size < size: 
            overlap = self.OVERLAP_MIDDLE 

        return overlap

    def merge(self, interval):
        assert(self.overlap(interval))
        self.start = min(self.start, interval.get_start())
        self.end = max(self.end, interval.get_end())

   
    def split(self, interval):
        """
        Return a list with 0, 1 or 2 intervals. The current interval object is not modified, 
        but should be discarded.
        """
        assert(self.overlap(interval))
        overlap_type = self._overlap(interval)        
        if overlap_type == self.OVERLAP_LEFT: 
            return [Interval(interval.get_end(),self.end)] 

        if overlap_type == self.OVERLAP_RIGHT: 
            return [Interval(self.start,interval.get_start())] 
        
        if overlap_type == self.OVERLAP_MIDDLE: 
            return [Interval(self.start,interval.get_start()), 
                    Interval(interval.get_end(),self.end)] 
        
        if overlap_type == self.OVERLAP_COVER: 
            return []
     
    def to_string(self):  
        return "(" + ",".join((str(self.start), str(self.end))) + ")"

class IntervalSet:
      
      def __init__(self):
          self.intervals = {}

      def add(self, start, end): 
          keys = self.intervals.keys() 
          keys.sort()
          interval = Interval(start, end)
          
          for key in keys:
              if interval.overlap(self.intervals[key]):              
                 interval.merge(self.intervals[key]) 
                 self.intervals.pop(key)
          
          self.intervals[interval.get_start()] = interval
              

      def remove(self, start, end):
          keys = self.intervals.keys() 
          keys.sort()
          interval = Interval(start, end)
         
          for key in keys: 
              if interval.overlap(self.intervals[key]):
                  split_interval = self.intervals.pop(key)
                  split_intervals = split_interval.split(interval) 
                  for new_interval in split_intervals: 
                      self.intervals[new_interval.get_start()] = new_interval
    
      def pprint(self):
          keys = self.intervals.keys()
          keys.sort()
          intervals = [] 
          for key in keys:
              intervals.append(self.intervals[key].to_string())
          intervals_string = "[" + ",".join(intervals) + "]" 
          print intervals
