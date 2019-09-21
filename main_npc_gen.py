import npc_gen
import json


# CLASS TO RECONSTRUCT NPCS FROM SAVE FILE

class NPCSaved:

    def __init__(self, sex, char, principles, law_disposition, trait1_type,
                 trait2_type, trait1, trait2, conf_ct1, conf_ct2,
                 conf_tt, quirk, prof_type, prof, con, ill, looks):  # 17
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
    """Append the attributes of an NPC to save file as a string"""
    attrib_list = [npc.sex, npc.char, npc.principles, npc.law_disposition,
            npc.trait1_type, npc.trait2_type, npc.trait1, npc.trait2,
            npc.conf_ct1, npc.conf_ct2, npc.conf_tt, npc.quirk,
            npc.prof_type, npc.prof, npc.con, npc.ill, npc.looks]
    # Open (or create) the save file in append mode
    with open("saved_npcs.txt", "a") as save_file:
        # Serializing attribute list to save file
        # as a JSON-formatted string
        save_file.write(json.dumps(attrib_list))


def pull_from_file():
    """Reconstruct all NPCs from the save file"""
    # Open the save file in read mode
    with open("saved_npcs.txt", "r") as save_file:
        s = json.load(save_file)
        for x in s:
            print(x)


def delete_npc():
    """Delete a single NPC from the save file and then update it"""
    # Open the save file in read mode
    save_file = open("saved_npcs.txt", "r")
    #
    # CODE HERE
    # Close the save file
    save_file.close()


#########  TESTING  #########


# n1 = npc_gen.NPC()
# append_to_file(n1)
pull_from_file()

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
