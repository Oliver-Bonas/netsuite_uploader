import sys
import os
print(sys.executable)

AIRFLOW_REPO = "airflow_pipelines"

def link_me_up():
    """
    Make sure both repos are in the same directory!!!!
    ./airflow_pipelines
    ./netsuite_uploader
    """
    sys.path.append(os.path.join(
        os.getcwd(),
        "..",
        "..",
        AIRFLOW_REPO,
        "dags"
    ))
    sys.path.append(os.path.join(
        os.getcwd(),
        ".."
    ))

    from config.environment import ENVIRONMENT

    ENVIRONMENT.set_development()