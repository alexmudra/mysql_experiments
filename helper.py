import pandas

#read csv via panda module
def read_csv(path_to_csv):
    print(tuple(dict(item[1]) for item in tuple(pandas.read_csv(path_to_csv, sep=';', header=0, index_col = None).iterrows())))
    return tuple(dict(item[1]) for item in tuple(pandas.read_csv(path_to_csv, sep=';', header=0, index_col = None).iterrows()))
# '''
# tuple(dict( - це кортеж діктів
# sep='; - сепаратор яким розділяються колонки в csv-ішках
# header=0 -> хедер 0 не буде парсити 0й рядок в csv, н-д ITEM_NAME;PRICE. Пандас просто сприйме дані як заголовок
# index_col = None - параметр який визначає що жодна колонка не буде індексуватися
# .iterrows - ітератор
# '''

#insert data to db table
def form_insert_from_dict_tuple(table_name, dict_tuple: [dict])->str:
    return f"INSERT INTO {table_name}({', '.join(dict_tuple[0].keys())}) VALUES {', '.join([str(tuple(i.values())) for i in dict_tuple])}"

