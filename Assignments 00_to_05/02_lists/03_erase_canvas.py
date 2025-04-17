import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 03_erase_canvas

def main():
    GRID_SIZE = 10
    CELL_SIZE = 40
    ERASER_SIZE = 2  # Not used yet but can be extended

    # Create a figure and axis for plotting
    fig, ax = plt.subplots(figsize=(GRID_SIZE, GRID_SIZE))

    # Create a grid of blue rectangles
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            ax.add_patch(patches.Rectangle(
                (i * CELL_SIZE, j * CELL_SIZE),
                CELL_SIZE, CELL_SIZE,
                linewidth=1,
                edgecolor='black',
                facecolor='blue'
            ))

    # Function to simulate the eraser
    def erase_cells(event):
        x, y = event.xdata, event.ydata

        if x is None or y is None:
            return

        col = int(x // CELL_SIZE)
        row = int(y // CELL_SIZE)

        ax.add_patch(patches.Rectangle(
            (col * CELL_SIZE, row * CELL_SIZE),
            CELL_SIZE, CELL_SIZE,
            linewidth=1,
            edgecolor='black',
            facecolor='white'
        ))
        plt.draw()

    # Connect the click event to the erase function
    fig.canvas.mpl_connect('button_press_event', erase_cells)

    # Set limits and show the grid
    ax.set_xlim(0, GRID_SIZE * CELL_SIZE)
    ax.set_ylim(0, GRID_SIZE * CELL_SIZE)
    ax.set_aspect('equal')
    ax.invert_yaxis()  # Optional: Makes top-left (0,0)
    plt.show()

if __name__ == "__main__":
    main()



