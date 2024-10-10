import pandas as pd


def find_earthquakes(magnitude, df):
    """Find all earthquakes of a certain magnitude."""
    return df[df['mag'] == magnitude]['place']


def main():
    # Load the earthquake data from the CSV file
    df = pd.read_csv('earthquakes.csv')

    # Ask the user for the desired earthquake magnitude
    magnitude = float(input("What magnitude earthquake are you looking for? "))

    # Find the earthquakes with the desired magnitude
    matching_quakes = find_earthquakes(magnitude, df)

    # Print the locations of the matching earthquakes
    if not matching_quakes.empty:
        print(f"Earthquakes of magnitude {magnitude} occurred at the following locations:")
        for location in matching_quakes:
            print(location)
    else:
        print(f"No earthquakes of magnitude {magnitude} were found.")


if __name__ == "__main__":
    main()
