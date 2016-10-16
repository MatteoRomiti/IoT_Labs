class Bike_Sharing(object):

	def sort_by_available_slots(self, lst, user):
		# cast slots to int
		for i in range(len(lst)):
			lst[i]["slots"] = int(lst[i]["slots"])
		# sort
		lst = sorted(lst, key=lambda k: k["slots"], reverse=user["order"]) 
		# limit the list to N
		new_lst = []
		for i in range(int(user["N"])):
			new_lst.append(lst[i])
		return new_lst

	def sort_by_available_bikes(self, lst, user):
		# cast bikes to int
		for i in range(len(lst)):
			lst[i]["bikes"] = int(lst[i]["bikes"])
		# sort
		lst = sorted(lst, key=lambda k: k["bikes"], reverse=int(user["order"]))
		# limit the list to N
		new_lst = []
		for i in range(int(user["N"])):
			new_lst.append(lst[i])
		return new_lst		

	def select_by_zipcode(self, lst, user):
		# select the requested stations 
		new_lst = []
		for i in range(len(lst)):
			if int(lst[i]["zip"]) == int(user["zipcode"]):
				new_lst.append(lst[i])
		return new_lst
		# zip_list = []
		# for i in range(len(lst)):
		# 	if lst[i]["zip"] in zip_list:
		# 		pass
		# 	else:
		# 		zip_list.append(lst[i]["zip"])
		# return zip_list

	def stations_with_more_than_N_available_ebikes(self, lst, user):
		e_lst = []
		new_lst = []
		for i in range(len(lst)):
			if lst[i]["stationType"] == "ELECTRIC_BIKE":
				e_lst.append(lst[i])
		for i in range(len(e_lst)):
			if int(e_lst[i]["bikes"]) > int(user["Ne"]):
				new_lst.append(e_lst[i])
		return new_lst

	def get_the_amount_of_bikes_and_slots_in_a_district(self, lst, user):
		new_lst = []
		bikes = 0
		slots = 0
		for i in range(len(lst)):
			if int(lst[i]["district"]) == int(user["district"]):
				bikes += int(lst[i]["bikes"])
				slots += int(lst[i]["slots"])
		dct = {"bikes": bikes, "slots": slots}
		new_lst.append(dct)
		return new_lst
