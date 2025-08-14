shopping_dict = {
    'warzywniak': ['marchewka', 'burak', 'rukola'],
    'piekarnia': ['bułka', 'chleb', 'pączek'],
    'spozywczy': ['kasza', 'maka']
}
i = 0
for key, values in shopping_dict.items():
    key_1=key.capitalize()
    new_values=[value.capitalize() for value in values ]
    print(f"ide so {key_1} i kupuje tam{new_values}")
    s = len(new_values)
i = s+i
print(f"W sumie kupuje {i} produktów.")