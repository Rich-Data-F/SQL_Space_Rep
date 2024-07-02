import os
import logging
import duckdb
import pandas as pd
import streamlit as st

# Define the rows
data={"Temperature":[23, 23, 21], "date":['12Jun2023', '13Jun2027', '13JUL2023']}
#row_1 = ['column_title_1', 'column_title_2', 'column_title_3']
#row_2 = [3, 4, 5]
#row_3 = [2, 5, 3]
#row_4 = [2, 5, 3]
#nb_rows = 4
#
## Initialize an empty list to store rows
#rows = []
#
## Use a for loop to dynamically append rows to the list
#for i in range(1, nb_rows + 1):
#    current_row = globals()[f'row_{i}']
## Use exec to get the value of the variable
##    exec(f'current_row = {row_var_name}')
##    current_row=f'row_{i}'
#    st.write(f"{current_row}")
#    st.write(f"nom de la row:{current_row}")
#    rows.append(current_row)
#
#rows_df=pd.DataFrame(rows, columns=rows[0])
data_df=pd.DataFrame(data)
st.dataframe(data_df)

sql_query_text=st.text_area(label='Proposez le texte de votre query')
st.write(f"texte de la query SQL: {sql_query_text}")
result=duckdb.query(sql_query_text).df()
st.dataframe(result)


# Create the DataFrame from the list of rows
# data = pd.DataFrame(rows[1:], columns=rows[0])


# import streamlit as st
# from datetime import date, timedelta


# if "data" not in os.listdir():
#   print("creating folder data")
#   logging.error(os.listdir())
#   logging.error("creating folder data")
#   os.mkdir("data")

# if "exercises_sql_tables.duckdb" not in os.listdir("data"):
#   exec(open("init_db.py").read())
#   # subprocess.run(["python", "init_db.py"])

#on = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

#def check_users_solution(user_query: str) -> None:
#   """
#   Checks that user SQL query is correct by:
#   1: checking the columns
#   2: checking the values
#   :param user_query: a string containing the query inserted by the user
#   """
#   result = con.execute(user_query).df()
#   st.dataframe(result)
#   try:
#       result = result[solution_df.columns]
#       st.dataframe(result.compare(solution_df))
#       if result.compare(solution_df).shape == (0, 0):
#           st.write("Correct !")
#           st.balloons()
#   except KeyError as e:
#       st.write("Some columns are missing")
#   n_lines_difference = result.shape[0] - solution_df.shape[0]
#   if n_lines_difference != 0:
#       st.write(
#           f"result has a {n_lines_difference} lines difference with the solution_df"
#       )
#
#
#with st.sidebar:
#   available_themes_df = con.execute("SELECT DISTINCT theme FROM memory_state").df()
#   theme = st.selectbox(
#       "What would you like to review?",
#       available_themes_df["theme"].unique(),
#       index=None,
#       placeholder="Select a theme...",
#   )
#   if theme:
#       st.write(f"You selected {theme}")
#       select_exercise_query = f"SELECT * FROM memory_state WHERE theme = '{theme}'"
#   else:
#       select_exercise_query = f"SELECT * FROM memory_state"
#
#   exercise = (
#       con.execute(select_exercise_query)
#       .df()
#       .sort_values("last_reviewed")
#       .reset_index(drop=True)
#   )
#   st.write(exercise)
#   exercise_name = exercise.loc[0, "exercise_name"]
#   with open(f"answers/{exercise_name}.sql", "r") as f:
#       answer = f.read()
#
#   solution_df = con.execute(answer).df()
#
#st.header("enter your code:")
#form = st.form("my_form")
#query = form.text_area(label="votre code SQL ici", key="user_input")
#form.form_submit_button("Submit")
#
#df query:
#   check_users_solution(query)
#
#for n_days in [2, 7, 21]:
#   if st.button(f"Revoir dans {n_days} jours"):
#       next_review = date.today() + timedelta(days=n_days)
#       con.execute(
#           f"UPDATE memory_state SET last_reviewed = '{next_review}' WHERE exercise_name = '{exercise_name}'"
#       )
#       st.rerun()
#
#if st.button("Reset"):
#   con.execute(f"UPDATE memory_state SET last_reviewed = '1970-01-01'")
#   st.rerun()
#
#
#tab2, tab3 = st.tabs(["Tables", "Solution"])
#with tab2:
#   exercise_tables = exercise.loc[0, "tables"]
#   for table in exercise_tables:
#       st.write(f"table: {table}")
#       df_table = con.execute(f"SELECT * FROM {table}").df()
#       st.dataframe(df_table)
#
# with tab3:
#   st.write(answer)