import numpy as np
from lecture import complex_math

import numpy as np

def random_search(function, num_samples=1000, bounds=(-100, 100)):
    # Generate all random x, y pairs
    samples = np.random.randint(bounds[0], bounds[1], size=(num_samples, 2))

    best_x, best_y = None, None
    best_output = float('inf')

    for x, y in samples:
        value = function(x, y)

        if value < best_output:
            best_x, best_y, best_output = x, y, value

    return best_x, best_y, best_output

if __name__ == '__main__':
    x, y, v = random_search(function=complex_math)  # Find the best (x, y) that minimises the value of function(x, y)
    print(f"Best x: {x}")
    print(f"Best y: {y}")
    print(f"Best output: {v}")