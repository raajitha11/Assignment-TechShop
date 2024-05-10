from dao.BaseDB import BaseDB


class EntityDB(BaseDB):
    def __init__(self, table_name):
        super().__init__()
        # self.table_name = table_name

    def get_entity_details(self, sql_query):
        # sql_query = f"SELECT * FROM {self.table_name} WHERE {self.get_entity_id_column()} = %s"
        entity_data = self.execute_query(sql_query)
        if entity_data:
            print(f"{self.get_entity_name()} Details:", entity_data)
        else:
            print(f"{self.get_entity_name()} not found.")