# Import any dependencies needed to execute sql queries
from employee_events.sql_execution import QueryMixin 
# Define a class called QueryBase
# that has no parent class
class QueryBase(QueryMixin):

    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = ""

    # Define a `names` method that receives
    # no passed arguments
    def names(self):
                
        # Return an empty list
        return []


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self, id: int):
          

        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        query = f"""
                    SELECT event_data, SUM(positive_events), SUM(negative_events)
                     FROM {self.name}
                     JOIN employee_events ON {self.name}.{self.name}_id = employee_events.{self.name}_id
                     WHERE {self.name}.{self.name}_id = {id}
                     GROUP BY event_date
                     ORDER BY event_date
                """
        return self.run_query_df(query)    
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    def notes(self, id: int):

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        query = f"""
                SELECT note_date, note
                    FROM notes
                    JOIN {self.name} ON {self.name}.{self.name}_id = notes.{self.name}_id
                    WHERE {self.name}.{self.name}_id = {id}
                """
        return self.run_query_df(query)

