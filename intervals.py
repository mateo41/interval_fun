from interval_set import IntervalSet
 
interval_set = IntervalSet()
interval_set.add(1,5)
interval_set.pprint()
interval_set.remove(2,3)
interval_set.pprint()
interval_set.add(6,8)
interval_set.pprint()
interval_set.remove(4,7)
interval_set.pprint()
interval_set.pprint()
interval_set.add(1,10)
interval_set.pprint()
interval_set.remove(4,7)
interval_set.pprint()

