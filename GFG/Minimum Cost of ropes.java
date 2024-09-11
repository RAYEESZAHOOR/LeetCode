// Given an array arr containing the lengths of the different ropes, we need to connect these ropes to form one rope. The cost to connect two ropes is equal to sum of their lengths. The task is to connect the ropes with minimum cost. 


class Solution {
    // Function to return the minimum cost of connecting the ropes.
    public long minCost(long[] arr) {
        // code here
        long totalCost = 0;
        PriorityQueue<Long> pq = new PriorityQueue<>();

        // Add all rope lengths to the priority queue
        for (long length : arr) {
            pq.offer(length);
        }

        // Connect ropes until only one remains
        while (pq.size() > 1) {
            long cost = pq.poll() + pq.poll();
            totalCost += cost;
            pq.offer(cost);
        }

        return totalCost;
    }
}