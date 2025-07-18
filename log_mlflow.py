import dagshub
dagshub.init(repo_owner='ssubratkumar75', repo_name='ML_Project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)