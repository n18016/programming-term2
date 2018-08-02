arasi = {
    "Aiba":35,
    "Matsumoto":34,
    "Ninomiya":35,
    "Oono":37,
    "Sakurai":36
}

li = sorted(
    arasi.items(),
    key=lambda x: x[1],
    reverse=True)
for name, seniority in li:
    print(name, seniority)
