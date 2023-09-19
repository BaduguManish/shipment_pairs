# Define shipment data
shipments = [
    ['US', 'US', 8],
    ['US', 'IN', 14],
    ['US', 'CA', 4],
    ['US', 'MX', 7],
    ['US', 'VE', 13],
    ['IN', 'US', 3],
    ['IN', 'IN', 13],
    ['IN', 'CA', 18],
    ['IN', 'MX', 16],
    ['IN', 'VE', 3],
    ['CA', 'US', 8],
    ['CA', 'IN', 20],
    ['CA', 'CA', 16],
    ['CA', 'MX', 3],
    ['CA', 'VE', 2],
    ['MX', 'US', 12],
    ['MX', 'IN', 20],
    ['MX', 'CA', 3],
    ['MX', 'MX', 3],
    ['MX', 'VE', 8],
    ['VE', 'US', 3],
    ['VE', 'IN', 7],
    ['VE', 'CA', 5],
    ['VE', 'MX', 15],
    ['VE', 'VE', 13],
]

def remove_intra_shipments(data):
    """Remove shipments where the origin and destination are the same country."""
    export_only = []
    for shipment in data:
        if shipment[0] != shipment[1]:
            export_only.append(shipment)
    return export_only

def combine_shipment_pairs(data):
    """Combine shipment quantities for unique country pairs, sorted by quantity."""
    shipment_pairs = []
    data = sorted(data, key=lambda x: x[2], reverse=True)
    for i in range(len(data) - 1):
        current_shipment = data[i]
        next_shipment = data[i + 1]
        if current_shipment[0] == next_shipment[0]:
            # Same origin, so add quantities
            shipment_pairs.append(
                [current_shipment[0], current_shipment[1], current_shipment[2] + next_shipment[2], next_shipment[2]]
            )
        else:
            # Different origins, create a new pair
            shipment_pairs.append([current_shipment[0], current_shipment[1], current_shipment[2], 0])
            shipment_pairs.append([next_shipment[0], next_shipment[1], 0, next_shipment[2]])
    return shipment_pairs

if __name__ == '__main__':
    # Part 1: Remove intra shipments
    export_only_shipments = remove_intra_shipments(shipments)
    print('#' * 80, ' ' * 30 + 'Intra Removed', '#' * 80, sep='\n')
    print(export_only_shipments)

    # Part 2: Combine shipment pairs
    combined_shipment_pairs = combine_shipment_pairs(shipments)
    print('\n', '#' * 80, ' ' * 30 + 'Pairs collected', '#' * 80, sep='\n')
    print(combined_shipment_pairs)
