import npc_gen
import json


# CLASS TO RECONSTRUCT NPCS FROM SAVE FILE

class NPCSaved:

    def __init__(self, name, sex, char, principles, law_disposition, trait1_type,
                 trait2_type, trait1, trait2, conf_ct1, conf_ct2,
                 conf_tt, quirk, prof_type, prof, con, ill, looks):  # 18
        self.name = name
        # SEX AND GENDER
        self.sex = sex
        self.gender, self.subj, self.poss, self.obj, self.reflex = self.pronouns()
        # CHARACTER AND PERSONALITY
        self.char = char
        self.principles = principles
        self.law_disposition = law_disposition
        self.trait1_type = trait1_type
        self.trait2_type = trait2_type
        self.trait1 = trait1
        self.trait2 = trait2
        self.conf_ct1 = conf_ct1
        self.conf_ct2 = conf_ct2
        self.conf_tt = conf_tt
        self.quirk = quirk
        # PROFESSION
        self.prof_type = prof_type
        self.prof = prof
        # CONSTITUTION AND APPEARANCE
        self.con = con
        self.ill = ill
        self.looks = looks

    def pronouns(self):
        if self.sex == "male":
            #     gender, subj, poss,  obj,   reflex
            return "man", "he", "his", "him", "himself"
        else:
            #       gender, subj,  poss,  obj,   reflex
            return "woman", "she", "her", "her", "herself"


#########  FUNCTIONS  #########

def append_to_file(npc):
    """Append the attributes of an NPC to save file as a JSON string"""
    # Pull the attributes off an NPC class instance
    attrib_list = [npc.name, npc.sex, npc.char, npc.principles, npc.law_disposition,
                   npc.trait1_type, npc.trait2_type, npc.trait1, npc.trait2,
                   npc.conf_ct1, npc.conf_ct2, npc.conf_tt, npc.quirk,
                   npc.prof_type, npc.prof, npc.con, npc.ill, npc.looks]
    # Open (or create) the save file in append mode
    with open("saved_npcs.txt", "a") as save_file:
        # Serializing attribute list to save file
        # as a JSON-formatted string
        save_file.write(json.dumps(attrib_list))
        save_file.write("\n")


def pull_from_file():
    """Reconstruct all NPCs from the save file"""
    # Create list to store NPCs pulled from save file
    pulled_npcs = []
    # Load NPCs from save file
    with open("saved_npcs.txt", "r") as save_file:
        for each_list in save_file:
            pulled_npcs.append(json.loads(each_list))
    # Reconvert each attribute list to NPC class instance
    reconstructed_npcs = []
    for each_npc in pulled_npcs:
        reconstructed_npcs.append(NPCSaved(*each_npc))
    return reconstructed_npcs


def delete_npc():
    """Delete a single NPC from the save file and then update it"""
    # Pull NPCs from save file
    pulled = pull_from_file()
    # Display saved NPCs in a numbered list
    print("\n" * 2)
    for x, y in enumerate(pulled, start=1):
        print(f"{x}. {npc_gen.narrative_view(y)}", "\n" * 2)
    # Ask the user which saved NPC he wants to delete
    while True:
        # Check to see if user gives valid input (int)
        try:
            del_index = int(input("Which NPC do you want to delete? ")) - 1
            # Check to see if input corresponds to an NPC index
            if del_index in range(0, len(pulled)):
                break
            else:
                print("Invalid input.  That number does not correspond to an NPC in the list.")
        except ValueError:
            print("Invalid input.  Please enter a number.")
    # Ask for confirmation
    print(f"\n\n{del_index + 1}. {npc_gen.narrative_view(pulled[del_index])}")
    del_verify = input("\nAre you sure you want to delete this character? ")
    # If confirmed, delete NPC
    if "y" in del_verify.lower():
        # Delete the NPC
        del pulled[del_index]
        # Clear the save file
        with open("saved_npcs.txt", "w") as save_file:
            pass
        # Push updated list to save file
        for each_npc in pulled:
            append_to_file(each_npc)
    else:
        # Not deleting, return to main menu
        pass


def delete_all():
    """Clear the save file"""
    # Ask for confirmation
    del_verify = input("\nAre you sure you want to delete all the NPCs you've saved? ")
    if "y" in del_verify.lower():
        # Clear the save file
        with open("saved_npcs.txt", "w") as save_file:
            pass



#########  TESTING  #########

# n1 = npc_gen.NPC()
# append_to_file(n1)
# p = pull_from_file()
# for x in p:
#     print("\n" * 3, npc_gen.narrative_view(x))

#########  INTRO TEXT  #########

# print(" ")
# print("##########################################################")
# print(" ")
# print("You are at the main menu.  Type M to bring up this menu again.")
# print("Hit Enter to generate a new random NPC.")
# print("Type C to change view mode between profile and narrative.")
# print("Type S to save the current NPC or V to view saved NPCs.")
# print(" ")
# print("##########################################################")
# print(" ")
#


#########  MAIN MENU  #########


# narrative_view = True
# current_npcs = []
#
# while True:
#     user_input = input("")
#     if user_input.lower() == "m":
#         print(" ")
#         print("##########################################################")
#         print(" ")
#         print("You are at the main menu.")
#         print("Hit Enter to generate a new random NPC.")
#         print("Type C to change view mode between profile and narrative.")
#         print("Type S to save the current NPC or V to view saved NPCs.")
#         print(" ")
#         print("##########################################################")
#         print(" ")
#     elif user_input.lower() == "c":
#         narrative_view = not narrative_view
#         if narrative_view:
#             print("You are now in narrative mode.")
#             print("")
#             for x in current_npcs:
#                 output = npc_gen.narrative_view(x)
#                 print(output)
#                 print("")
#                 print("")
#                 print("")
#         else:
#             print("You are now in profile mode.")
#             print("")
#             for x in current_npcs:
#                 npc_gen.profile_view(x)
#                 print("")
#                 print("")
#                 print("")
#     elif user_input.lower() == "s":
#         pass
#     elif user_input.lower() == "v":
#         pass
#     else:  # Enter generates new NPC
#         current_npcs.append(npc_gen.NPC())
#         if narrative_view:
#             output = npc_gen.narrative_view(current_npcs[-1])
#             print(output)
#             print("")
#             print("")
#             print("")
#         else:  # profile view
#             npc_gen.profile_view(current_npcs[-1])
#             print("")
#             print("")
#             print("")
