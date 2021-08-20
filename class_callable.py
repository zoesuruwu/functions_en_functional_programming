# Class 1
def sequence_class(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list
    return cls


seq = sequence_class(immutable=True)
t = seq("Timbuku")
print(type(t))
print(t)

# Class 2
def sequence_class(immutable):
    return tuple if immutable else list


seq = sequence_class(immutable=False)
t = seq("Nairobi")
print(type(t))
print(t)
