class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
        

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        category_list =[]
        for items in self.inventory:
            if items.category == category:
                category_list.append(items)
        return category_list