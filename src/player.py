class Player():
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.inventory = dict()
        self.selected_item = None
        
        
    #call on item pickup    
    def add_item_to_inventory(item):
        self.inventory["item"] =self.inventory["item"] + 1
    
    #call on item drop/use
    def remove_item_to_inventory(item):
        self.inventory["item"] =self.inventory["item"] - 1
    
    #call on player move    
    def update_player_pos(x,y):
        self.x_pos = x
        self.y_pos = y
    
    #call on itemswitch
    def set_selected_item(item):
        if self.inventory["item"]>0:
            self.selected_item = item
        else:
            print("item is not in the players inventory")
            raise 
    