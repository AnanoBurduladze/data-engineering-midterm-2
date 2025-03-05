import pandas as pd

def process_csv(input_file, output_file):

    df = pd.read_csv(input_file)


    df = df[df['value'] > 30]


    result = df.groupby('category', as_index=False)['value'].mean()


    result.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")

if __name__ == "__main__":
    input_file = "data.csv"
    output_file = "processed_data.csv"
    process_csv(input_file, output_file)
