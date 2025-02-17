#!/usr/bin/env python3

import math
import random
import time


# Create a Class called "Location".
# Each location object will have an x and y variable denoting a location in 2D space.
class Location:
    def __init__(self, x, y):
        # Save the input arguments as object variables
        self.x = x
        self.y = y


# Create a Class called "WeightedAverage"
# This Class provides a method for processing a list of Locations
class WeightedAverager:
    def __init__(self, origin, landmarks):

        # Save the input arguments as object variables
        self.origin = origin
        self.landmarks = landmarks

        # Define parameters
        threshold = 10.0  # outliers beyond this distance should be ignored

        # Call the averaging function
        answer = self.weighted_average(threshold)

        # Print the answer to console
        print("answer: " + str(answer))

    def weighted_average(self, threshold):
        # Generate random weights
        weights = [random.random() for _ in self.landmarks]

        # Calculate distances first to determine which landmarks to include
        distances = []
        valid_indices = []

        print("Calculating distances:")
        for i, landmark in enumerate(self.landmarks):
            # Calculate Euclidean distance
            dx = landmark.x - self.origin.x
            dy = landmark.y - self.origin.y
            distance = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
            distances.append(distance)

            # Print and check if within threshold
            if distance <= threshold:
                valid_indices.append(i)
                status = "included"
            else:
                status = "excluded (> threshold)"
            print(f"Location ({landmark.x}, {landmark.y}): distance = {distance:.2f}, {status}")

        if not valid_indices:
            print("No landmarks within threshold distance!")
            return 0.0

        # Normalize weights for only the valid landmarks
        valid_weights = [weights[i] for i in valid_indices]
        weight_sum = sum(valid_weights)
        normalized_weights = [w / weight_sum for w in valid_weights]

        # Calculate weighted average using only valid landmarks
        weighted_total = 0.0
        print("\nCalculating weighted average with valid landmarks:")
        for i, weight in zip(valid_indices, normalized_weights):
            weighted_total += distances[i] * weight
            print(f"Using distance {distances[i]:.2f} with weight {weight:.3f}")

        return weighted_total


if __name__ == '__main__':

    # Setup the data
    origin = Location(5.0, 5.0)
    landmarks = [Location(6.0, 7.0), Location(5.1, 4.9), Location(15.0, 20.0), Location(8.0, 0.0), Location(-3.0, 2.0),
                 Location(-10.0, -10.0), Location(5.0, 5.0), Location(0.0, 0.0)]

    try:
        # Run continuously at 2 Hz
        while True:
            print("\n--- New Calculation ---")
            # Create and run the WeightedAverager object
            weighted_averager = WeightedAverager(origin, landmarks)

            # Sleep for 0.5 seconds (2 Hz)
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nProgram terminated by user")