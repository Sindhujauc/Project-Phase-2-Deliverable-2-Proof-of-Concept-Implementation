# Example test for Priority Queue
recommendation_queue = PriorityQueue()
recommendation_queue.insert("Smartphone", 90)  # Product with a relevance score of 90
recommendation_queue.insert("Laptop", 80)  # Product with a relevance score of 80

# Get top-1 recommended product
print(recommendation_queue.get_top_n(1))  # Expected output: ["Smartphone"]