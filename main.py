def replace_list_element(list_elements, index, text):
    list_elements[index] = text
    return list_elements


book_titles = ["Гарри Поттер и Тайная комната", "Гарри Поттер и Тайная комната",
               "Гарри Поттер и узник Азкабана", "Гарри Поттер и Кубок огня",
               "Гарри Поттер и Принц-полукровка"]
replace_list_element(book_titles, 0, "Гарри Поттер и Философский камень")
replace_list_element(book_titles, -1, "Гарри Поттер и Орден Феникса")
print(book_titles)