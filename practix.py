items_tags = {"milo":150,"milk":250,"sweet":50,"diaper":5000,"soap":200}
print(items_tags)

products = ["singlet","boxer","slippers","spagheti","candle"]
items = dict.fromkeys(products,1000)
print(items)

items_2 = {"liquid_soap":300}

items_tags.update(items_2)
print(items_tags)

merged_dict = items_tags|items
print(merged_dict)

dict_1 = {"name":"Nuel","country":"Ghana","height":5.7,
          "age":25,"phone no":[89699943,894636636]}
access = dict_1["phone no"][1]
print(f"Accesed_second_no:{access}")

dict_1["height"] = 6.7
print(dict_1)

university = {
    "English Language":{"teacher":"Rita","students":30,"means of teaching":"online"},
    "Maths":{'teacher':"John","students":50,"means of teaching":"online"},
    "Programming":{"teacher":"Nuel","students":30,"means of teaching":"online"}
}
means_of_teaching_prog = university["Programming"]["means of teaching"]
print(means_of_teaching_prog)

print("students" in university["Maths"])

print(dict_1.get("email", "no email found"))

n = [6,2,5,7,1,9,3]
n.sort()
n.reverse()
print(f"Descending order:{n}")

m = (4,2,7,9,3)
reverse_1 = m[::-1]
print(f"reversed:{reverse_1}")

dict_2 = dict()
dict_2["rice"] = 1000
dict_2["beans"] = 500
dict_2["garri"] = 300
print(dict_2)

