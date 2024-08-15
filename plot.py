import numpy as np
import matplotlib.pyplot as plt
import csv

def load_data_from_csv(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            n, value = map(float, row)
            data.append((n, value))
    return zip(*data)

def load_degree_distribution(filename):
    degree_distribution = {}
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            degree, count = map(int, row)
            degree_distribution[degree] = count
    return degree_distribution
def plot_diameter_and_clustering(num_nodes_list, diameters_ba, clustering_coefficients_ba,
                                 diameters_er, clustering_coefficients_er):
    log_num_nodes = np.log(num_nodes_list)

    plt.figure(figsize=(14, 10))

    # Plot Diameter for BA Graph
    plt.subplot(2, 2, 1)
    plt.scatter(num_nodes_list, diameters_ba, label='BA Graph')
    plt.xscale('log')
    plt.xlabel('# of Nodes (n)')
    plt.ylabel('Average Diameter')
    plt.title('BA Graph: Average Diameter vs. Number of Nodes')
    slope, intercept = np.polyfit(log_num_nodes, diameters_ba, 1)
    plt.plot(num_nodes_list, slope * log_num_nodes + intercept, color='red', linewidth=2, label = f'Slope of Best Fit: {slope:.3f}')
    plt.legend()

    # Plot Diameter for ER Graph
    plt.subplot(2, 2, 2)
    plt.scatter(num_nodes_list, diameters_er, label='ER Graph')
    plt.xscale('log')
    plt.xlabel('Number of nodes (n)')
    plt.ylabel('Average Diameter')
    plt.title('ER Graph: Average Diameter vs. Number of Nodes')
    slope, intercept = np.polyfit(log_num_nodes, diameters_er, 1)
    plt.plot(num_nodes_list, slope * log_num_nodes + intercept, color='red', linewidth=2, label = f'Slope of Best Fit: {slope:.3f}')
    plt.legend()

    # Plot Clustering Coefficient for BA Graph
    plt.subplot(2, 2, 3)
    plt.scatter(num_nodes_list, clustering_coefficients_ba, label='BA Graph')
    plt.xscale('log')
    plt.xlabel('Number of nodes (n)')
    plt.ylabel('Average Clustering Coefficient')
    plt.title('Average Clustering Coefficient vs. Number of Nodes (BA Graph)')
    slope, intercept = np.polyfit(log_num_nodes, clustering_coefficients_ba, 1)
    # plt.plot(num_nodes_list, slope * log_num_nodes + intercept, color='red', linestyle='dashed', linewidth=2)
    plt.legend()

    # Plot Clustering Coefficient for ER Graph
    plt.subplot(2, 2, 4)
    plt.scatter(num_nodes_list, clustering_coefficients_er, label='ER Graph')
    plt.xscale('log')
    plt.xlabel('Number of nodes (n)')
    plt.ylabel('Average Clustering Coefficient')
    plt.title('Average Clustering Coefficient vs. Number of Nodes (ER Graph)')
    slope, intercept = np.polyfit(log_num_nodes, clustering_coefficients_er, 1)
    # plt.plot(num_nodes_list, slope * log_num_nodes + intercept, color='red', linestyle='dashed', linewidth=2)
    plt.legend()

    plt.tight_layout()
    plt.show()

def plot_degree_distribution(degree_distribution, n, graph_type):
    degrees = list(degree_distribution.keys())
    counts = list(degree_distribution.values())
    

    plt.figure(figsize=(14, 6))

    # Lin-Lin Scale
    plt.subplot(1, 2, 1)
    plt.bar(degrees, counts, width=0.8)
    plt.xlabel('Degree')
    plt.ylabel('Count')
    plt.title(f'{graph_type} Graph: Degree Distribution (n={n}) - Lin-Lin Scale')

    if graph_type == 'BA':
        plt.xlim(0, 80)

    # Log-Log Scale
    plt.subplot(1, 2, 2)
    plt.scatter(degrees, counts)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Degree')
    plt.ylabel('Count')
    plt.title(f'Degree Distribution (n={n}, {graph_type}) - Log-Log Scale')

    # Fit a line to the log-log data using degrees between 5 and 100
    if graph_type == 'BA' and n == 100000:
        filtered_degrees = [d for d in degrees if 5 <= d <= 140]
    else:
        filtered_degrees = [d for d in degrees if 5 <= d <= 100]
    filtered_counts = [counts[degrees.index(d)] for d in filtered_degrees]

    log_degrees = np.log(filtered_degrees)
    log_counts = np.log(filtered_counts)
    slope, intercept = np.polyfit(log_degrees, log_counts, 1)
   
    if graph_type == 'BA':
        plt.plot(filtered_degrees, np.exp(slope * log_degrees + intercept), color='red', linewidth=2, label=f'Slope of Best Fit: {slope:.2f})')
        plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    num_nodes_list_ba, average_diameters_ba = load_data_from_csv("diameters_ba.csv")
    _, average_clustering_coefficients_ba = load_data_from_csv("clustering_coefficients_ba.csv")
    num_nodes_list_er, average_diameters_er = load_data_from_csv("diameters_er.csv")
    _, average_clustering_coefficients_er = load_data_from_csv("clustering_coefficients_er.csv")

    plot_diameter_and_clustering(num_nodes_list_ba, average_diameters_ba, average_clustering_coefficients_ba,
                                 average_diameters_er, average_clustering_coefficients_er)

    # Plot degree distributions
    # for n in [64, 128, 256, 512, 1024, 1500, 2048, 3000, 4096, 6000, 8192, 16284, 16284 * 2]:
    for n in [1000, 10000, 100000]:
        # degree_distribution_ba = load_degree_distribution(f"degree_distribution_ba_{n}.csv")
        # plot_degree_distribution(degree_distribution_ba, n, "BA")

        degree_distribution_er = load_degree_distribution(f"degree_distribution_er_{n}.csv")
        plot_degree_distribution(degree_distribution_er, n, "ER")

if __name__ == "__main__":
    main()


