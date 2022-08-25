import kvv_plan
import time

t = input("Enter Time: ")
n = input("Train:      ")
s = input("Station:    ")

plan = kvv_plan.plan

if n in plan[0]["number"]:

    print("")
    print(plan[0]["number"] + " -> " + plan[0]["to"])
    print("="*len(plan[0]["number"] + " -> " + plan[0]["to"]))

    count = 0

    result_id = 0

    if s == "":

        for line in plan[0]["stations"]["plan"]:

            count += 1
            
            for i, routes in enumerate(line, 1):

                sp = routes["time"].split(":")
                t_sp = t.split(":")

                if int(t_sp[0]) == int(sp[0]):
                    if int(t_sp[1]) == int(sp[1]):
                        result_id += 1
                        print("{:02d}".format(result_id) +  " | " + "{:02d}".format(count) + " | now  | " + routes["time"] + " | " + routes["station"])

                    if int(t_sp[1]) + 1 == int(sp[1]):
                        result_id += 1
                        print("{:02d}".format(result_id) +  " | " + "{:02d}".format(count) + " | next | " + routes["time"] + " | " + routes["station"])

    else:

        for line in plan[0]["stations"]["plan"]:

            count += 1
            
            for i, routes in enumerate(line, 1):

                if s in routes["station"]:
                    sp = routes["time"].split(":")
                    t_sp = t.split(":")
                    

                    if int(t_sp[0]) == int(sp[0]):
                        if int(t_sp[1]) == int(sp[1]):
                            result_id += 1
                            print("{:02d}".format(result_id) +  " | " + "{:02d}".format(count) + " | now  | " + routes["time"] + " | " + routes["station"])

                        else:
                            for i in range(30):

                                if (int(t_sp[1]) + i) == int(sp[1]):
                                    result_id += 1
                                    print("{:02d}".format(result_id) +  " | " + " | next | " + routes["time"] + " | " + routes["station"])
                                    break
                

                    elif int(t_sp[0]) + 1 == int(sp[0]):
                        if int(t_sp[1]) == int(sp[1]):
                            result_id += 1
                            print("{:02d}".format(result_id) +  " | " + " | now  | " + routes["time"] + " | " + routes["station"])


                        else:
                            for i in range(59):

                                if i == int(sp[1]):
                                    result_id += 1
                                    print("{:02d}".format(result_id) +  " | " + "{:02d}".format(count) + " | next | " + routes["time"] + " | " + routes["station"])
                                    break
            