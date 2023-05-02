ages = {"Claudia": 35, "Lisa": 52}
print(ages)
books = {"Stephen King": "Shinning", "Eric Ries": "The Lean Startup"}
print(books)
series = {"Netflix": "Dark", "Apple": "Severence", "HBO": "Game of Thrones"}
print (series)
dict_ages = dict({"Claudia": 35, "Lisa": 52})
print (dict_ages)
dict_books = dict({"Stephen King": "Shinning", "Eric Ries": "The Lean Startup"})
print(dict_books)
dict_series = dict({"Netflix": "Dark", "Apple": "Severence", "HBO": "Game of Thrones"})
print (dict_series)
dict_list = [ages, books, series]
print (dict_list)
dict_list_2 = [{"Claudia": 35, "Lisa": 52}, {"Stephen King": "Shinning", "Eric Ries": "The Lean Startup"}, {"Netflix": "Dark", "Apple": "Severence", "HBO": "Game of Thrones"}]
print (dict_list_2)
dict_list_3 = [dict({"Claudia": 35, "Lisa": 52}), dict({"Stephen King": "Shinning", "Eric Ries": "The Lean Startup"}), dict({"Netflix": "Dark", "Apple": "Severence", "HBO": "Game of Thrones"})]
print (dict_list_3)
dict_list_4 = []
dict_list_4.append(ages)
dict_list_4.append(books)
dict_list_4.append(series)
print (dict_list_4)
