"""
DIGM 131 - Assignment 2: Procedural Pattern Generator
======================================================

OBJECTIVE:
    Use loops and conditionals to generate a repeating pattern of 3D objects
    in Maya. You will practice nested loops, conditional logic, and
    mathematical positioning.

REQUIREMENTS:
    1. Use a nested loop (a loop inside a loop) to create a grid or pattern
       of objects.
    2. Include at least one conditional (if/elif/else) that changes an
       object's properties (type, size, color, or position offset) based
       on its row, column, or index.
    3. Generate at least 25 objects total (e.g., a 5x5 grid).
    4. Comment every major block of code explaining your logic.

GRADING CRITERIA:
    - [25%] Nested loop correctly generates a grid/pattern of objects.
    - [25%] Conditional logic visibly changes object properties based on
            position or index.
    - [20%] At least 25 objects are generated.
    - [15%] Code is well-commented with clear explanations.
    - [15%] Pattern is visually interesting and intentional.

TIPS:
    - A 5x5 grid gives you 25 objects. A 6x6 grid gives you 36.
    - Use the loop variables (row, col) to calculate X and Z positions.
    - The modulo operator (%) is great for alternating patterns:
          if col % 2 == 0:    # every other column
    - You can vary: primitive type, height, width, position offset, etc.

COMMENT HABITS (practice these throughout the course):
    - Add a comment before each logical section explaining its purpose.
    - Use inline comments sparingly and only when the code is not obvious.
    - Keep comments up to date -- if you change the code, update the comment.
"""

import maya.cmds as cmds

# Clear the scene.
cmds.file(new=True, force=True)

def generate_pattern():
    # --- Configuration variables ---
    # These lines of code are giving names to how long and wide the pattern will be
    number_rows = 6  
    number_columns = 6 
    spacing = 3.0 

    # I used number_rows to match the name I created above
    for rows in range(number_rows):
        # This makes sure all of the coordinates made have an object placed for them
        for columns in range(number_columns):
            
            # Makes sure the objects are placed in a grid
            x_pos = columns * spacing
            z_pos = rows * spacing

            # One of the variables used to make the pattern
            # I use rows and columns variables I made to make checker pattern
            if  (rows + columns) % 2 == 0:
                geometry = cmds.polyCube(name=f"bloop_{rows}_{columns}")[0]
                cmds.scale(2, 1, 2, geometry)
            else:
                # Is the oposite for the variable above
                geometry = cmds.polySphere(name=f"beep_{rows}_{columns}")[0]
                cmds.scale(1, 1, 1, geometry)

            # needed to move and create all the objects
            cmds.move(x_pos, 0, z_pos, geometry)

# ---------------------------------------------------------------------------
# Run the generator
# ---------------------------------------------------------------------------
generate_pattern()

# Frame everything in the viewport.
cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")
