import csv

import joblib
import pandas as pd
import ast
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from Sardinas_Patterson import is_codage
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data = [line.strip()[1:-1].replace(' ', '').split(',') for line in lines]
    return data

def sequence_length(sequence):
    return len(sequence)

def count_ones(sequence):
    return sequence.count('1')

def count_zeros(sequence):
    return sequence.count('0')

def ratio_ones(sequence):
    return count_ones(sequence) / len(sequence) if len(sequence) > 0 else 0

def ratio_zeros(sequence):
    return count_zeros(sequence) / len(sequence) if len(sequence) > 0 else 0

def subsequence_frequency(sequence, subseq):
    return sequence.count(subseq)

def average_length(binary_strings):
    lengths = [len(s) for s in binary_strings]
    total_length = sum(lengths)
    average = total_length / len(binary_strings) if binary_strings else 0
    return average

def count_words(binary_strings):
    return len(binary_strings)

def entropy(sequence):
    from collections import Counter
    import math
    if not sequence:
        return 0
    counts = Counter(sequence)
    probabilities = [count / len(sequence) for count in counts.values()]
    entropy_value = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return entropy_value

def process_line(line):
    concatenated_sequence = ''.join(line)
    seq_properties = {
        "language": line,
        "length": sequence_length(concatenated_sequence),
        "count_words": count_words(line),
        "average_word_length": average_length(line),
        "count_ones": count_ones(concatenated_sequence),
        "count_zeros": count_zeros(concatenated_sequence),
        "ratio_ones": ratio_ones(concatenated_sequence),
        "ratio_zeros": ratio_zeros(concatenated_sequence),
        "frequency_11": subsequence_frequency(concatenated_sequence, "11"),
        "frequency_00": subsequence_frequency(concatenated_sequence, "00"),
        "entropy": entropy(concatenated_sequence),
        "valeur": 0
    }
    return seq_properties


def makeDataFrame(line):
    concatenated_sequence = ''.join(line)
    seq_properties = {
        "length": sequence_length(concatenated_sequence),
        "count_words": count_words(line),
        "average_word_length": average_length(line),
        "count_ones": count_ones(concatenated_sequence),
        "count_zeros": count_zeros(concatenated_sequence),
        "ratio_ones": ratio_ones(concatenated_sequence),
        "ratio_zeros": ratio_zeros(concatenated_sequence),
        "frequency_11": subsequence_frequency(concatenated_sequence, "11"),
        "frequency_00": subsequence_frequency(concatenated_sequence, "00"),
        "entropy": entropy(concatenated_sequence),
    }
    return seq_properties

def process_data(data):
    processed_data = []
    for line in data:
        line_properties = process_line(line)
        processed_data.append(line_properties)
    return processed_data

def write_to_csv(processed_data, output_file):
    headers = [
        "language", "length", "count_words", "average_word_length", "count_ones", "count_zeros", "ratio_ones",
        "ratio_zeros", "frequency_11", "frequency_00", "entropy", "valeur"
    ]
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for row in processed_data:
            writer.writerow(row)
            

def update_csv() :
    file_path = 'data.csv'
    df = pd.read_csv(file_path)
    df['valeur'] = df['language'].apply(lambda x: 1 if is_codage(ast.literal_eval(x)) else 0)
    df.to_csv(file_path, index=False)
    print("update okokok")
    
    
def train_ia():
    file_path = 'data.csv'
    df = pd.read_csv(file_path)
    x = df.drop(columns=['language', 'valeur'], axis=1)
    y = df['valeur']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=42)
    model = KNeighborsClassifier(n_neighbors=12)
    model.fit(x_train, y_train)
    joblib.dump(model, "model.joblib")
    score = model.score(x_test, y_test)
    print(f"Model Accuracy: {score}")