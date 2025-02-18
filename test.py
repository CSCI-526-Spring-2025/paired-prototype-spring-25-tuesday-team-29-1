from PIL import Image, ImageDraw
import random

def create_maze(width, height):
    maze = [[1] * width for _ in range(height)]
    start_x, start_y = random.randrange(0, width, 2), random.randrange(0, height, 2)
    maze[start_y][start_x] = 0
    stack = [(start_x, start_y)]

    while stack:
        x, y = stack[-1]
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)

        moved = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                maze[y + dy//2][x + dx//2] = 0
                stack.append((nx, ny))
                moved = True
                break

        if not moved:
            stack.pop()
    return maze

def draw_maze_png(maze, cell_size=10, wall_color=(0, 0, 0), background_color=(0, 0, 0, 0), filename="maze.png", wall_thickness=2):

    height = len(maze)
    width = len(maze[0])
    image_width = width * cell_size
    image_height = height * cell_size

    img = Image.new('RGBA', (image_width, image_height), background_color)
    draw = ImageDraw.Draw(img)

    for y in range(height):
        for x in range(width):
            if maze[y][x] == 1:
                if y == 0 or maze[y-1][x] == 0:
                    x1, y1 = x * cell_size, y * cell_size
                    x2, y2 = (x + 1) * cell_size, y * cell_size + wall_thickness
                    draw.rectangle([(x1, y1), (x2, y2)], fill=wall_color)
                if y == height - 1 or maze[y+1][x] == 0:
                    x1, y1 = x * cell_size, (y + 1) * cell_size - wall_thickness
                    x2, y2 = (x + 1) * cell_size, (y + 1) * cell_size
                    draw.rectangle([(x1, y1), (x2, y2)], fill=wall_color)

                if x == 0 or maze[y][x-1] == 0:
                    x1, y1 = x * cell_size, y * cell_size
                    x2, y2 = x * cell_size + wall_thickness, (y + 1) * cell_size
                    draw.rectangle([(x1, y1), (x2, y2)], fill=wall_color)

                if x == width - 1 or maze[y][x+1] == 0:
                    x1, y1 = (x + 1) * cell_size - wall_thickness, y * cell_size
                    x2, y2 = (x + 1) * cell_size, (y + 1) * cell_size
                    draw.rectangle([(x1, y1), (x2, y2)], fill=wall_color)

    img.save(filename, "PNG")
    print(f"Maze saved as {filename}")

if __name__ == "__main__":
    maze_width = 20
    maze_height = 10
    cell_size = 30
    wall_color = (255, 255, 255)
    transparent_background = (0, 0, 0, 0)
    wall_thickness = 3

    maze_grid = create_maze(maze_width, maze_height)
    draw_maze_png(maze_grid, cell_size, wall_color, transparent_background, "simple_maze_connected_walls.png", wall_thickness)