Polynomial Regression for Car Price Prediction

This project implements a Polynomial Regression model to predict the price of used cars based on their age.

🛠️ Project Details

Dataset:

Car ages (in years) vs. their prices (in $1000).

Older cars generally have lower prices, but the relationship is non-linear.

Preprocessing:

Data reshaped for model compatibility.

Polynomial features generated with degree 2.

Model:

Linear Regression trained on the expanded polynomial features.

Libraries Used:

NumPy

Matplotlib

scikit-learn

📈 Workflow

Create polynomial features from the input data.

Train the regression model on these features.

Predict the price of a 5-year-old car.

Plot the original data and the fitted polynomial curve.

🚀 How to Run

Clone the repository:

git clone https://github.com/OsamaAt/your-repo-name.git
cd your-repo-name

Install required libraries:

pip install numpy matplotlib scikit-learn

Run the script:

python polynomial_regression_car_price.py

🧪 Results

The model successfully captures the non-linear relationship between car age and price.

Smooth polynomial curve fitting the data points.

✍️ Author

OsamaAt
