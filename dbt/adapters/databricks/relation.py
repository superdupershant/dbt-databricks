from dataclasses import dataclass

from dbt.adapters.base.relation import Policy
from dbt.adapters.spark.relation import SparkRelation


@dataclass
class DatabricksIncludePolicy(Policy):
    database: bool = True
    schema: bool = True
    identifier: bool = True


@dataclass(frozen=True, eq=False, repr=False)
class DatabricksRelation(SparkRelation):
    include_policy: DatabricksIncludePolicy = DatabricksIncludePolicy()

    def __post_init__(self) -> None:
        return

    def rander(self):
        return super(SparkRelation, self).render()
