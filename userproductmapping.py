# Define a Hash Table for User-Product Mapping
class UserProductMapping:
    def _init_(self):
        self.data = {}

    def add_interaction(self, user_id, product_id):
        if user_id not in self.data:
            self.data[user_id] = set()
        self.data[user_id].add(product_id)

    def get_interactions(self, user_id):
        return self.data.get(user_id, set())