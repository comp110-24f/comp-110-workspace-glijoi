"""examples of dictionary syntax with Ice Cream Shop order tallies"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evaluates to number of entries
print(len(ice_cream))  # prints 3

# add key-value entry
ice_cream["mint"] = 3

# access entries by key
print(ice_cream["chocolate"])  # prints 12

# test if pbj is key in i_c
has_pbj: bool = "pbj" in ice_cream

# remove
ice_cream.pop("strawberry")  # returns value being deleted: returns 4

# for loop
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor} has {tally} orders")
