import nltk
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

def download_nltk_resources():
    nltk.download("punkt")
    nltk.download("stopwords")

def preprocess_text(text):
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return " ".join(filtered_tokens)

def svd(M, k=None, epsilon_factor=1e-6):
    """
    Compute the Singular Value Decomposition of a matrix M.

    Parameters:
    - M: Input matrix
    - k: Number of singular values to compute (default is min(rows, columns))
    - epsilon_factor: Small regularization term factor based on the scale of singular values

    Returns:
    - U: Left singular vectors
    - S: Singular values
    - Vt: Right singular vectors (transposed)
    """
    M = np.array(M, dtype=float)
    rows, cols = M.shape

    # If k is not specified, use the smaller of the matrix dimensions
    k = k or min(rows, cols)

    # Compute M^T * M and M * M^T
    MTM = M.T @ M
    MMT = M @ M.T

    # Eigenvalue decomposition of M^T * M
    eigenvalues_MTM, V_MTM = np.linalg.eigh(MTM)

    # Sort eigenvalues in descending order
    sorted_indices = np.argsort(eigenvalues_MTM)[::-1]
    eigenvalues_MTM = eigenvalues_MTM[sorted_indices]
    V_MTM = V_MTM[:, sorted_indices]

    # Calculate singular values using absolute values of eigenvalues
    singular_values = np.sqrt(np.abs(eigenvalues_MTM))

    # epsilon is a small positive number that is added to the diagonal 
    # the purpose of adding epsilon is to improve the stability and 
    # accuracy of the computation.
    epsilon = epsilon_factor * np.max(singular_values)
    
    # so:
    #   let M be the original matrix, ϵ be the regularization term, and I be the identity matrix
    #   the modified matrix is calculated as:
    #       M_reg = M + ϵ⋅I
    M_reg = M + epsilon * np.identity(min(rows, cols))

    U = M_reg @ V_MTM / singular_values

    # Keep only the first k singular values/vectors
    U = U[:, :k]
    singular_values = singular_values[:k]
    Vt = V_MTM[:, :k].T

    return U, singular_values, Vt

def extractive_summarization(text, num_sentences=3):
    sentences = sent_tokenize(text)
    
    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sentences)
    
    # Apply Singular Value Decomposition (SVD)
    U, S, Vt = svd(X.toarray())
    
    # Select top-ranked sentences based on the first component of the SVD
    top_sentence_indices = U[:, 0].argsort()[-num_sentences:][::-1]
    
    # Generate summary
    summary = [sentences[i] for i in sorted(top_sentence_indices)]
    return "\n".join(summary)

