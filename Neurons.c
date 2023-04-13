#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct neuron {
    double *weights;  // pointer to array of weights
    double bias;      // neuron bias
    int num_inputs;   // number of inputs
} Neuron;

double sigmoid(double x) {
    return 1 / (1 + exp(-x));
}

double activate(Neuron *neuron, double *inputs) {
    double activation = neuron->bias;
    for (int i = 0; i < neuron->num_inputs; i++) {
        activation += neuron->weights[i] * inputs[i];
    }
    return sigmoid(activation);
}

Neuron *create_neuron(int num_inputs) {
    Neuron *neuron = malloc(sizeof(Neuron));
    neuron->num_inputs = num_inputs;
    neuron->weights = malloc(num_inputs * sizeof(double));
    for (int i = 0; i < num_inputs; i++) {
        neuron->weights[i] = ((double) rand() / RAND_MAX) * 2 - 1; // initialize weights randomly between -1 and 1
    }
    neuron->bias = ((double) rand() / RAND_MAX) * 2 - 1; // initialize bias randomly between -1 and 1
    return neuron;
}

void destroy_neuron(Neuron *neuron) {
    free(neuron->weights);
    free(neuron);
}

int main() {

    // Create a neuron with 3 inputs
    Neuron *neuron = create_neuron(3);

    // Set the inputs.
    double inputs[3] = {1, 2, 3};

    // Activate the neuron.
    double output = activate(neuron, inputs);

    printf("output: %f\n", output);

    // Destroy the neuron.
    destroy_neuron(neuron);

    return 0;
}
