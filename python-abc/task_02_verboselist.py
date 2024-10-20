#!/usr/bin/python3
class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list")

    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        print(f"Removed {item} from the list")
        super().remove(item)

    def pop(self, index=-1):
        print(f"Popped {index} from the list.")
        super().pop(index)


if __name__ == "__main__":
    type_list = VerboseList([1, 2, 3])
    print(type_list)
    type_list.append(4)
    type_list.extend([5, 6, 7])
    print(type_list)
    type_list.remove(7)
    print(type_list)
    type_list.pop()
    print(type_list)
    type_list.pop(2)
    print(type_list)
