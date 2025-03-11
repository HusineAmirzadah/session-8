import heapq

exchange = {
    'Binance': {'Coinbase': 200, 'Kraken': 45, 'FTX': 35, 'Gemini': 180},
    'Coinbase': {'Binance': 190, 'Kraken': 40, 'FTX': 30, 'Gemini': 170},
    'Kraken': {'Binance': 90, 'Coinbase': 85, 'FTX': 95, 'Gemini': 40},
    'FTX': {'Binance': 80, 'Coinbase': 75, 'Kraken': 90, 'Gemini': 110},
    'Gemini': {'Binance': 175, 'Coinbase': 165, 'Kraken': 55, 'FTX': 105}
}

def get_lowest_fees(graph, start):
    """
    Find lowest fee routes to an exchange.

    Args:
        graph (dict): An adjacency list of neighboring exchanges with their fees.
        start (str): The starting exchange name.

    Returns:
        dict: Exchange names and the lowest fees to reach them from the starting exchange.
    """
    distances = {node: float('inf') for node in graph}

    # TODO: implement dijkstras
    
    return distances


src, dest = "Gemini", "Coinbase"
distances = get_lowest_fees(exchange, src)
print(f"Fee from {src} to {dest}: {distances[dest]}")

