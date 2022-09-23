# Databricks notebook source
# MAGIC %run ./dbclient_wrapper

# COMMAND ----------

dbclient.get('/jobs/list', version='2.1')

# COMMAND ----------

job_json = {
    "name": "Notebook_Execution",
    "tags": {
                "purpose": "api_test"
            },
    "tasks": [
        {
            "task_key": "Notebook_Execution",
            "description": "Job created via API",
            "job_cluster_key": "wagnersilveira_jobcluster",
            "notebook_task": {
                "notebook_path": "/Users/wagner.silveira@databricks.com/example",
                "source": "WORKSPACE",
                "base_parameters": {
                    "param": "John Doe"
                }
            },
            "timeout_seconds": 86400,
            "max_retries": 3,
            "min_retry_interval_millis": 2000,
            "retry_on_timeout": False
        }
    ],
    "job_clusters": [
        {
            "job_cluster_key": "wagnersilveira_jobcluster",
            "tags": {
                "purpose": "api_test"
            },
            "new_cluster": {
                "num_workers": 1,
                "spark_version": "10.4.x-scala2.12",
                "node_type_id": "m4.large",
                "driver_node_type_id": "m4.large",
                "aws_attributes": {
                    "first_on_demand": 1,
                    "availability": "SPOT_WITH_FALLBACK",
                    "zone_id": "auto",
                    "spot_bid_price_percent": 100,
                    "ebs_volume_type": "GENERAL_PURPOSE_SSD",
                    "ebs_volume_count": 3,
                    "ebs_volume_size": 100
                },
            },
        }
    ],
    "email_notifications": {
        "on_start": [
            "wagner.silveira@databricks.com"
        ],
        "on_success": [
            "wagner.silveira@databricks.com"
        ],
        "on_failure": [
            "wagner.silveira@databricks.com"
        ],
        "no_alert_for_skipped_runs": False
    },
    "timeout_seconds": 86400,
    "format": "SINGLE_TASK",
    "access_control_list": [
        {
            "group_name": "admins",
            "permission_level": "CAN_MANAGE"
        }
    ]
}

# COMMAND ----------

dbclient.post("/jobs/create", json_params=job_json, version="2.1")
