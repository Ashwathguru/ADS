import heap
import PQ
import Airport

print("MAX HEAP IMPLEMENTATION ")
h=heap.MaxHeap([1,2,3,4,5])
h._buildheap()
h.printlist()
print("EXTRACTING MAX")
print(h.extract_max())
h.printlist()
print("Ascending Order")
h.maxHeap_sort()
h.printlist()
h.heap_add(6)
h.printlist()



print("Priority Queue")
print("Please Insert [ID,Priority,Arrival Time,Execution time,Deadline]")
l=[1,1,1,1,5]
pq=PQ.priorityQueue(l)

pq.heap_add([1,2,1,5,10])
pq.heap_add([2,3,1,5,11])
pq.heap_add([3,3,3,6,12])
pq.descOrder()
print(pq.data)
WT, tat = pq.waitingTime()
l2 = pq.chkDeadline(tat)
print(l2)



print("AIRPORT")
l1 = [20180808011100, 1, 'Landing']
air = Airport.Min_Heap(l1)
print("Please Insert in Format [Time Stamp,Flight No.,Takeoff/Landing]")
air.heap_add([20181208101100, 2, 'Takeoff'])
air.heap_add([20181208101130, 3, 'Landing'])
air.heap_add([20181208100030, 4, 'Takeoff'])
print(air.data)
ans= air.extracting_min()
print(ans)
print("Flight No.: ",ans[1])
print("Event:",ans[2])
print("Time: ",ans[0])