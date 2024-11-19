### What is a Matrix?

A matrix is a rectangular array of numbers arranged in rows and columns. For example, a 3x3 matrix looks like this:

$$
\begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix}
$$

### Basic Operations

1. **Addition**: Matrices of the same size can be added together by adding corresponding elements.
2. **Multiplication**: Matrices can be multiplied if the number of columns in the first matrix equals the number of rows in the second matrix.

### Usage in Games

Matrices are extensively used in game development, especially in 3D graphics. Here are a few key applications:

#### 1. Transformations

Matrices are used to perform transformations such as translation, rotation, and scaling on objects in a game.

- **Translation**: Moving an object from one place to another.
- **Rotation**: Rotating an object around an axis.
- **Scaling**: Changing the size of an object.

For example, a translation matrix for moving an object by \( (x, y, z) \) units is:

$$
\begin{bmatrix}
1 & 0 & 0 & x \\
0 & 1 & 0 & y \\
0 & 0 & 1 & z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

#### 2. Camera View

Matrices are used to control the camera view in a game. The view matrix transforms coordinates from world space to camera space.

#### 3. Projection

Projection matrices convert 3D coordinates to 2D coordinates for rendering on the screen. For example, a perspective projection matrix looks like this:

$$
\begin{bmatrix}
\frac{1}{\tan(\frac{fov}{2})} & 0 & 0 & 0 \\
0 & \frac{1}{\tan(\frac{fov}{2})} & 0 & 0 \\
0 & 0 & \frac{far + near}{near - far} & \frac{2 \cdot far \cdot near}{near - far} \\
0 & 0 & -1 & 0
\end{bmatrix}
$$

### Example in Game Development

Imagine you have a character in a game that needs to move, rotate, and scale. You can use matrices to achieve this:

1. **Translation Matrix**: Move the character to a new position.
2. **Rotation Matrix**: Rotate the character around an axis.
3. **Scaling Matrix**: Change the size of the character.

By multiplying these matrices together, you can combine all these transformations into a single matrix that can be applied to the character.

### Code Example

Here's a simple example in C++:

```cpp
#include <iostream>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>

int main() {
    glm::mat4 model = glm::mat4(1.0f); // Identity matrix

    // Translation
    model = glm::translate(model, glm::vec3(1.0f, 2.0f, 3.0f));

    // Rotation
    model = glm::rotate(model, glm::radians(45.0f), glm::vec3(0.0f, 1.0f, 0.0f));

    // Scaling
    model = glm::scale(model, glm::vec3(0.5f, 0.5f, 0.5f));

    std::cout << "Model Matrix: " << glm::to_string(model) << std::endl;

    return 0;
}
```

Zdroj: konverzace s Copilotem, 15. 11. 2024
(1) Matrices and Vectors in Game Development - DEV Community. <https://dev.to/fkkarakurt/matrices-and-vectors-in-game-development-67h>.
(2) Cheat Sheet: Adding Math Notation To Markdown - upyesp. <https://www.upyesp.org/posts/makrdown-vscode-math-notation/>.
(3) Matrix Algebra and Game Programming - GameLudere. <https://www.gameludere.com/2019/12/21/matrix-algebra-and-game-programming/>.
