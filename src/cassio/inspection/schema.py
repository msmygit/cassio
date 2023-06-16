from typing import List, Any, Dict, Callable


def _table_primary_key_columns(session, keyspace, table_name) -> List[str]:
    table = session.cluster.metadata.keyspaces[keyspace].tables[table_name]
    return [
        col.name for col in table.partition_key
    ] + [
        col.name for col in table.clustering_key
    ]
