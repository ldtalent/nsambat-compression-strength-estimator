# concrete_strength
An online concrete compression strength estimator
# Parts
## The Model
This type of problem deals in continous variables and would require a regression model to solve it.
Multiple regression models exist of which two are selected namely: Linear Regression & Decision Tree Regression.
With prior knowledge of the highly non-linear nature of concrete compression strength Linear Regression is
selected against.
Decision Tree Regression is thus chosen as the model to be used.
### Train/Test Split
To evaluate model performance some of the data has to be split and not fit. This case chose to split 20% off for testing.
### Model Accuracy.
One metric to measure the accuracy is the r squared value of the model. Loosely Speaking, It is a measure of how well the model Fits to the data.
#### Model R2 value was approximately 80%.

### Model Persistence.
To deploy the model, it has to be saved or persisted. In this case the model was persisted with assistance of pickle to a  binary file namely: estimator.bin

### Relevant Files.
-Ensure all dependencies are installed from requirements.txt
-Utilize Trainer.ipynb to train the model.


## The Backend.
Flask framework was chosen to serve the content for its easy to setup and the project is small.

### Backend Endpoints
-Densities: These are required to estimate component mass in 1m cubed of concrete.
-concrete_strentgh: Required to measure concrete strength in MPa.
-Index: Required to load the frontend.

### Dependencies & Setup.
Python Backend dependencies are in requirements.txt
Ensure port 5000 is open.
Use flask run afer definining FLASK_APP="server.py" in your environment.

# The Frontend.
Vue framework was chosen for its easy to setup and can be used without a module bundler.
## UX
Range Sliders were chosen over other inputs that require keyboards. This is so because construction workers and administrators are often in environments keeping their hands busy, which would make typing hard.

### How it works.
The user interface accepts concrete mix ratios and returns concrete strength upon clicking the submit button.

## Methods.
-densities: Used to obtain density data from the backend.
-concrete strength: Used to obtain concrete strength.

## Dependencies.
All css and js dependencies are automatically loaded following inclusion of their cdns.

