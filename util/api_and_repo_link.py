import sys
import os
print(sys.executable)

AIRFLOW_REPO_FOLDER_NAME = "airflow_pipelines"

def link_me_up():
    """
    Make sure both repos are in the same directory!!!!
    ./airflow_pipelines
    ./netsuite_uploader
    """

    repo_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        AIRFLOW_REPO_FOLDER_NAME
    )
    sys.path.append(repo_path)

    from dags.config.environment import ENVIRONMENT



    another_repo = os.path.join(
        ENVIRONMENT.ROOT_FOLDER,
        "dags"
    )

    sys.path.append(another_repo)

    print("~" * len (another_repo))
    print(another_repo)
    print("~" * len (another_repo))
    print("now you just need to set_development()")