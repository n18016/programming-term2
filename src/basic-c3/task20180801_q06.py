arasi = {
    "Aiba":175,
    "Matsumoto":172,
    "Ninomiya":168,
    "Oono":166,
    "Sakurai":171
}

li = sorted(
    arasi.items(),
    key=lambda x: x[1])
for name, seniority in li:
    print(name, seniority)
