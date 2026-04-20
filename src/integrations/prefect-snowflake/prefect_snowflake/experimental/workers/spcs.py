# Backward-compatibility shim — the canonical module is now prefect_snowflake.workers.spcs
from snowflake.core import Root
from prefect_snowflake.workers.spcs import (
    SPCSServiceTemplateVariables,
    SPCSWorker,
    SPCSWorkerConfiguration,
    SPCSWorkerResult,
    _get_default_job_manifest_template,
    _is_transient_error,
)

__all__ = [
    "Root",
    "SPCSServiceTemplateVariables",
    "SPCSWorker",
    "SPCSWorkerConfiguration",
    "SPCSWorkerResult",
    "_get_default_job_manifest_template",
    "_is_transient_error",
]
