import zeep

def get_ns_number(api, word):
    """
    USAGE

    print(get_ns_number(api, "Customer"))
    print(get_ns_number(api, "CustomerSearch"))
    print(get_ns_number(api, "InventoryItem"))
    print(get_ns_number(api, "InventoryItemSearch"))
    print(get_ns_number(api, "SalesOrder"))
    """
    for i in range(100):
        try:
            t = api.client.get_type(f"ns{i}:{word}")
            print(f"{word} = api.client.get_type(\"ns{i}:{word}\")")
            break

        except zeep.exceptions.LookupError:
            print("failed for ns", i)
