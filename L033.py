import pandas as pd
import matplotlib.pyplot as plt

data = {
    "name": ["Ali", "Sara", "Usman", "Hina", "Omar", "Ayesha", "Bilal", "Zara", "Hamza", "Noor"],
    "hours": [1, 2, 2, 3, 4, 4, 5, 6, 7, 8],
    "marks": [35, 48, 52, 58, 61, 66, 70, 78, 85, 92]
}
df = pd.DataFrame(data)
plt.hist(df["marks"], bins=5)
plt.title("Mark of 10 students")
plt.xlabel("Marks")
plt.ylabel("No. of Students")
plt.savefig("Marks_hist.png")
plt.show()
# To check the equal round exactly
import numpy as np
print(np.histogram(df["marks"], bins=5))

# Histogram 
plt.scatter(df["hours"], df["marks"])
plt.title("Study hours vs Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.savefig("hours_marks_scatter.png")
plt.show()