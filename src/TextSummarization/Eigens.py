import numpy as np
import matplotlib.pyplot as plt

def plot_matrix_and_eigenvectors(matrix, eigenvectors):
    fig, ax = plt.subplots()

    # Plot the initial matrix as a heatmap
    cax = ax.matshow(matrix, cmap='viridis')

    # Plot the eigenvectors
    colors = ['r', 'b']
    for i, vector in enumerate(eigenvectors.T):
        origin = np.zeros_like(vector)
        ax.quiver(*origin, *vector, angles='xy', scale_units='xy', scale=1, color=colors[i], label=f'Eigenvector {i + 1}')

    # Set labels and title
    plt.xticks(range(len(matrix)))
    plt.yticks(range(len(matrix)))
    plt.xlabel('Column Index')
    plt.ylabel('Row Index')
    plt.title('Matrix and Eigenvectors')

    # Add legend
    plt.legend()

    # Add colorbar for the heatmap
    cbar = fig.colorbar(cax)
    cbar.set_label('Matrix Element Value')

    plt.show()


def main():
    # Define the matrix
    A = np.array([[3, 1], [1, 2]])

    # Find eigenvalues and eigenvectors
    # by using the np.linalg.eig() function
    eigenvalues, eigenvectors = np.linalg.eig(A)

    print("Initial Matrix A:")
    print(A)
    print("\nEigenvalues:")
    print(eigenvalues)
    print("\nEigenvectors:")
    print(eigenvectors)

    plot_matrix_and_eigenvectors(A, eigenvectors)

if __name__ == "__main__":
    main()

