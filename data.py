import numpy as np
import csv
from graph import Graph
from graph_algorithms import get_diameter, get_clustering_coefficient, get_degree_distribution
from barabasi_albert_graph import barabasi_albert_graph
from erdos_renyi_graph import erdos_renyi_graph
import os
def analyze_graphs(num_nodes_list, d, num_graphs=20):
    average_diameters_ba = []
    average_clustering_coefficients_ba = []
    average_diameters_er = []
    average_clustering_coefficients_er = []

    for n in num_nodes_list:
        diameters_ba = []
        clustering_coefficients_ba = []
        diameters_er = []
        clustering_coefficients_er = []

        for _ in range(num_graphs):
            # BA Graph
            graph_ba = barabasi_albert_graph(n, d)
            diameters_ba.append(get_diameter(graph_ba))
            clustering_coefficients_ba.append(get_clustering_coefficient(graph_ba))
            
            # ER Graph
            graph_er = erdos_renyi_graph(n)  # p is calculated inside the function
            diameters_er.append(get_diameter(graph_er))
            clustering_coefficients_er.append(get_clustering_coefficient(graph_er))

            # Save degree distribution for BA
            # degree_distribution_ba = get_degree_distribution(graph_ba)
            # save_degree_distribution(f"degree_distribution_ba_{n}.csv", degree_distribution_ba)
            
            # Save degree distribution for ER
            # degree_distribution_er = get_degree_distribution(graph_er)
            # save_degree_distribution(f"degree_distribution_er_{n}.csv", degree_distribution_er)

        average_diameters_ba.append(np.mean(diameters_ba))
        average_clustering_coefficients_ba.append(np.mean(clustering_coefficients_ba))
        average_diameters_er.append(np.mean(diameters_er))
        average_clustering_coefficients_er.append(np.mean(clustering_coefficients_er))

    return (average_diameters_ba, average_clustering_coefficients_ba,
            average_diameters_er, average_clustering_coefficients_er)

def save_data_to_csv(filename, data):
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["n", "value"])
        for n, value in data:
            writer.writerow([n, value])

def save_degree_distribution(filename, degree_distribution):
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["degree", "count"])
        for degree, count in degree_distribution.items():
            writer.writerow([degree, count])
def main():
    num_nodes_list = [64, 128, 256, 512, 1024, 1500, 2048, 3000, 4096, 6000, 8192, 16284, 16284 * 2]
    # num_nodes_list = [1000, 10000, 100000]
    # num_nodes_list = [ 16284 * 2]
    # num_nodes_list = [64, 128, 256, 512, 1024, 1500, 2048, 3000, 4096, 6000, 8192, 16284, 16284 * 2]
    d = 5
    
    
    (average_diameters_ba, average_clustering_coefficients_ba,
     average_diameters_er, average_clustering_coefficients_er) = analyze_graphs(num_nodes_list, d)

    save_data_to_csv("diameters_ba.csv", zip(num_nodes_list, average_diameters_ba))
    save_data_to_csv("clustering_coefficients_ba.csv", zip(num_nodes_list, average_clustering_coefficients_ba))
    save_data_to_csv("diameters_er.csv", zip(num_nodes_list, average_diameters_er))
    save_data_to_csv("clustering_coefficients_er.csv", zip(num_nodes_list, average_clustering_coefficients_er))

    

if __name__ == "__main__":
    main()
