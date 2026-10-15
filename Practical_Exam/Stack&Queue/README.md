# Food-Delivery Queue and Cancelled-Order Stack

## AIM
To implement a food-delivery system using a FIFO Queue for active orders and a LIFO Stack for cancelled orders.

## DESCRIPTION
New food orders are processed in arrival order using a Queue (FIFO). Cancelled orders are stored in a Stack (LIFO), so the most recently cancelled order is restored first.

## ALGORITHM
1. Create an empty Queue for active orders.
2. Create an empty Stack for cancelled orders.
3. Add new orders to the Queue.
4. Display active orders.
5. Process the first order using dequeue.
6. Cancel orders and push them onto the Stack.
7. Display cancelled orders.
8. Restore the latest cancelled order using pop.
9. Add the restored order to the active Queue.
10. Display the final Queue and Stack.

## SAMPLE OUTPUT
```text
Active orders: ['O101', 'O102', 'O103']
Processed order: O101
Cancelled orders: ['O102', 'O103']
Restored order: O103
Current active orders: ['O103']
Current cancelled stack: ['O102']
```

## ANALYSIS
- Queue follows FIFO (First In, First Out).
- Stack follows LIFO (Last In, First Out).
- Time Complexity: O(1) per enqueue, dequeue, push, and pop operation.
- Space Complexity: O(N), where N is the number of orders.

## INFERENCE
Combining a Queue and Stack efficiently manages active food orders and cancelled-order recovery.
