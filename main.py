if __name__ == "__main__":
    # Write your solution here
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    data = pd.read_csv("menu.csv")

    # Create a figure and subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    # Histogram of Calories values
    axs[0, 0].hist(data['Calories'], bins=20, edgecolor='black')
    axs[0, 0].set_xlabel('Calories')
    axs[0, 0].set_ylabel('Frequency')
    axs[0, 0].set_title('Histogram of Calories')

    # Parallel Box Plot of Fat and Protein values
    data[['Total Fat', 'Protein']].boxplot(ax=axs[0, 1])
    axs[0, 1].set_ylabel('Grams')
    axs[0, 1].set_title('Parallel Box Plot of Fat and Protein')

    # Scatter Plot of Fat vs Calories
    axs[1, 0].scatter(data['Total Fat'], data['Calories'])
    axs[1, 0].set_xlabel('Fat (grams)')
    axs[1, 0].set_ylabel('Calories')
    axs[1, 0].set_title('Scatter Plot of Fat vs Calories')

    # Add a trendline to the Scatter Plot
    fit = np.polyfit(data['Total Fat'], data['Calories'], 1)
    x = np.linspace(data['Total Fat'].min(), data['Total Fat'].max(), 100)
    trendline = np.poly1d(fit)
    y = trendline(x)
    axs[1, 0].plot(x, y, color='red', linestyle='--')

    # Bar chart showing the average Calories of each Category
    category_avg_calories = data.groupby('Category')['Calories'].mean()
    category_avg_calories.plot(kind='bar', ax=axs[1, 1])
    axs[1, 1].set_xlabel('Category')
    axs[1, 1].set_ylabel('Average Calories')
    axs[1, 1].set_title('Average Calories of Each Category')

    # Adjust the spacing between subplots
    plt.tight_layout()

    # Display the combined chart
    plt.show()

    pass
