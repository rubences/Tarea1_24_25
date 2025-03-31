class Entity:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def __str__(self):
        return f"Entity at ({self.x}, {self.y}) with image {self.image}"

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        # Placeholder for drawing logic
        print(f"Drawing entity at ({self.x}, {self.y}) with image {self.image}")

    def update(self):
        # Placeholder for update logic
        print(f"Updating entity at ({self.x}, {self.y}) with image {self.image}")

    def get_position(self):
        return self.x, self.y
    
    def set_position(self, x, y):
        self.x = x
        self.y = y
    
    def get_image(self):
        return self.image
    
    def set_image(self, image):
        self.image = image

    def collide(self, other):
        # Placeholder for collision detection logic
        return self.x == other.x and self.y == other.y
    
    


    
