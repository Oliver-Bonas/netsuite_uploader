import pandas
import os
cols = ["department", "new_pgr", "new_sgr", "new_type", "new_type_detail"]

everything = pandas.read_csv('all_attributes_and_properties.csv')
"""
fashion_extras = pandas.read_csv('fashion_extras.csv', delimiter="@")

fashion_extras['SplitValues'] = fashion_extras['ExternalID'].str.split(':')



# Create new columns based on split values
for i in range(5):  # Assuming you want 5 new columns
    name = cols[i]
    fashion_extras[name] = fashion_extras['SplitValues'].apply(lambda x: x[i].strip() if len(x) > i else None)
"""

hierarchy = pandas.concat(
    [
        everything[cols + ["config", "refnr"]],
        #fashion_extras[cols]
    ]
)

# strip spaces, and convert to title case
hierarchy.department = hierarchy.department.str.strip().str.title()
hierarchy.new_pgr = hierarchy.new_pgr.str.strip().str.title()
hierarchy.new_sgr = hierarchy.new_sgr.str.strip().str.title()
hierarchy.new_type = hierarchy.new_type.str.strip().str.title()
hierarchy.new_type_detail = hierarchy.new_type_detail.str.strip().str.title()
hierarchy = hierarchy.drop_duplicates()


#folder = r"N:\IT Shared\SO Shared\ERP Data\Products\20231002_filled_templates"
#main_fashion_file = os.path.join(folder, "main_fashion.csv")

#main_fashion = pandas.read_csv(main_fashion_file)

#1/0


# Departments
# Product Group
# Sub Product Group
# OB Type
# Type Detail
levels = {
    0: "Departments",
    1: "Product Group",
    2: "Sub Product Group",
    3: "OB Type",
    4: "Type Detail"
}

VERSION = "Oliver Bonas Update 2023"
#VERSION = "test1"

external_ids_already_added = {""}

csv_dict_rows = []

for pos, node in hierarchy.iterrows():
    config = node.pop("config")
    refnr = node.pop("refnr")
    vals = node.values


    parent_chain = vals[~pandas.isna(vals)].tolist()
    hierarchy.loc[hierarchy.index == pos, "merch_node_corrected"] = " : ".join(parent_chain)
    # remove trailing white space
    #parent_chain = [n.strip() for n in parent_chain]

    #parent_chain = ["test_" + n + "_test" for n in parent_chain]

    for i in range(len(parent_chain)):
        # parent is empty for fashion
        externalid = " : ".join(parent_chain[:i+1])
        parentid = " : ".join(parent_chain[:i])

        if externalid in external_ids_already_added:
            continue

        if parentid not in external_ids_already_added:
            raise Exception(f"parentid {parentid} not in external_ids_already_added")

        external_ids_already_added.add(externalid)


        csv_dict_rows.append({
            "ExternalID": externalid,
            "Name": parent_chain[i],
            "Description": "",
            "Version": VERSION,
            "level": levels[i],
            "Parentnode": parentid,
            "Is include": "TRUE",
        })

df = pandas.DataFrame(csv_dict_rows)
df = df.sort_values(by="ExternalID")

"""
without = pandas.read_csv("merch_hierarchy_cleaned.csv")
count = 0
for v in fashion_extras.ExternalID.values:
    if v.title().replace("  ", " ").replace("  ", " ").replace("  ", " ") not in df.ExternalID.values:
        count += 1
        print(count, v.title())
"""
df.to_csv("merch_hierarchy_comp.csv", index=False)



folder = r"N:\IT Shared\SO Shared\ERP Data\Products\20231002_filled_templates"

parents_fashion_file = os.path.join(folder, "parents_fashion.csv")
parents_home_and_gift_file = os.path.join(folder, "parents_home_and_gift.csv")
main_fashion_file = os.path.join(folder, "main_fashion.csv")
main_home_and_gift_file = os.path.join(folder, "main_home_and_gift.csv")

parents_fashion_unique_file = os.path.join(folder, "corrected", "parents_fashion_unique_nodes.csv")
parents_home_and_gift_unique_file = os.path.join(folder, "corrected", "parents_home_and_gift_unique_nodes.csv")
parents_fashion_dupe_file = os.path.join(folder,"corrected",  "parents_fashion_dupe_nodes.csv")
parents_home_and_gift_dupe_file = os.path.join(folder, "corrected", "parents_home_and_gift_dupe_nodes.csv")

child_fashion_file = os.path.join(folder, "corrected", "child_fashion.csv")
child_home_and_gift_file = os.path.join(folder, "corrected", "child_home_and_gift.csv")
single_fashion_file = os.path.join(folder, "corrected", "single_fashion.csv")
single_home_and_gift_file = os.path.join(folder, "corrected", "single_home_and_gift.csv")


parents_fashion = pandas.read_csv(parents_fashion_file)
parents_home_and_gift = pandas.read_csv(parents_home_and_gift_file)
main_fashion = pandas.read_csv(main_fashion_file)
main_home_and_gift = pandas.read_csv(main_home_and_gift_file)

main_fashion.external_id = main_fashion.external_id.astype(str)
main_home_and_gift.external_id = main_home_and_gift.external_id.astype(str)
hierarchy.refnr = hierarchy.refnr.astype(str)

parents_fashion = pandas.merge(
    parents_fashion,
    hierarchy[["config", "merch_node_corrected"]],
    how = "left",
    left_on = "external_id",
    right_on = "config"
).drop(columns=["config", "merch_hierarchy_nodes"])

parents_home_and_gift = pandas.merge(
    parents_home_and_gift,
    hierarchy[["config", "merch_node_corrected"]],
    how = "left",
    left_on = "external_id",
    right_on = "config"
).drop(columns=["config", "merch_hierarchy_nodes"])

main_fashion = pandas.merge(
    main_fashion,
    hierarchy[["refnr", "merch_node_corrected"]],
    how = "left",
    left_on = "external_id",
    right_on = "refnr"
).drop(columns=["refnr", "merch_hierarchy_nodes"])

main_home_and_gift = pandas.merge(
    main_home_and_gift,
    hierarchy[["refnr", "merch_node_corrected"]],
    how = "left",
    left_on = "external_id",
    right_on = "refnr"
).drop(columns=["refnr", "merch_hierarchy_nodes"])

single_fashion = main_fashion.loc[main_fashion.parent.isna(), : ]
child_fashion = main_fashion.loc[~main_fashion.parent.isna(), : ]
single_home_and_gift = main_home_and_gift.loc[main_home_and_gift.parent.isna(), : ]
child_home_and_gift = main_home_and_gift.loc[~main_home_and_gift.parent.isna(), : ]

single_fashion.drop(columns=["parent"], inplace=True)
single_home_and_gift.drop(columns=["parent"], inplace=True)

single_fashion.to_csv(single_fashion_file, index=False)
single_home_and_gift.to_csv(single_home_and_gift_file, index=False)
child_fashion.to_csv(child_fashion_file, index=False)
child_home_and_gift.to_csv(child_home_and_gift_file, index=False)

unique_fashion_nodes = parents_fashion.loc[~parents_fashion.external_id.duplicated(keep=False), : ]
duped_fashion_nodes = parents_fashion.loc[parents_fashion.external_id.duplicated(keep=False), : ]
#everything.loc[everything.config.notna(),["refnr", "config", "new_pgr", "new_sgr", "new_type", "new_type_detail"]]

#unique_fashion_nodes.to_csv(parents_fashion_unique_file, index=False)
#duped_fashion_nodes.to_csv(parents_fashion_dupe_file, index=False)

unique_home_and_gift_nodes = parents_home_and_gift.loc[~parents_home_and_gift.external_id.duplicated(keep=False), : ]
duped_home_and_gift_nodes = parents_home_and_gift.loc[parents_home_and_gift.external_id.duplicated(keep=False), : ]

#unique_home_and_gift_nodes.to_csv(parents_home_and_gift_unique_file, index=False)
#duped_home_and_gift_nodes.to_csv(parents_home_and_gift_dupe_file, index=False)
print("stop")
