def get_value_from_nested_object(data, key):
    keys = key.split('/')
    value = data

    try:
        for k in keys:
            value = value[k]
        return value
    except (KeyError, TypeError):
        return None

# Example Inputs
object1 = {"a": {"b": {"c": "d"}}}
key1 = "a/b/c"

object2 = {"x": {"y": {"z": "a"}}}
key2 = "x/y/z"

value1 = get_value_from_nested_object(object1, key1)
value2 = get_value_from_nested_object(object2, key2)

print("Value for key 'a/b/c':", value1)  # Output: Value for key 'a/b/c': d
print("Value for key 'x/y/z':", value2)  # Output: Value for key 'x/y/z': a
