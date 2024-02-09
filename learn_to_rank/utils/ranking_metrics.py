import numpy as np
class RankingMetrics:

    def __init__():
        pass
    
    @staticmethod
    def average_precision_at_k(actual_index, sorted_index, click_flag, k):
        """
        Calculate mean average precision at k (MAP@k).

        Parameters:
            actual_index (list): List of actual indices of products
            sorted_index (list): List of sorted indices of products based on the model output.
            click_flag (list): List of boolean flags indicating whether each product was clicked or not.
            k (int): Number of recommendations to consider.

        Returns:
            float: Mean average precision at k.
            list: List of precision at k.
        """
        # Initialize variables to track relevant documents and precision
        relevant_docs = 0
        precision_at_k = []

        # Iterate over the top k recommended products
        for i, index in enumerate(sorted_index[:k]):
            # Check if the product at this position is relevant (clicked)
            if click_flag[actual_index.index(index)]:
                # Increment relevant documents count
                relevant_docs += 1
                # Calculate precision at this position
                precision_at_k.append(relevant_docs / (i + 1))

        # Calculate mean average precision at k
        if relevant_docs == 0:
            return 0.0

        mean_precision = round(np.mean(precision_at_k),2)

        return mean_precision, precision_at_k
