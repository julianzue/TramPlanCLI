import kvv_plan
import time

from rich.table import Table, Style
from rich.console import Console

console = Console()

t = input("Enter Time: ")
n = input("Train:      ")
s = input("Station:    ")

if t == "now" or t == "":
    t = time.strftime("%H:%M")
    show_time = True
else:
    show_time = False

if show_time:
    print("")
    print("Time: " + t)

plan = kvv_plan.plan

if n in plan[0]["number"]:

    print("")
    #print(plan[0]["number"] + " -> " + plan[0]["to"])
    #print("="*len(plan[0]["number"] + " -> " + plan[0]["to"]))

    table = Table(show_lines=True, title=(plan[0]["number"] + " -> " + plan[0]["to"]))

    count = 0

    result_id = 0

    table.add_column("ID")
    table.add_column("Route")
    table.add_column("Status")
    table.add_column("Arrival")
    table.add_column("Time")
    table.add_column("Station")

    if s == "":

        for line in plan[0]["stations"]["plan"]:

            count += 1
            
            for i, routes in enumerate(line, 1):

                sp = routes["time"].split(":")
                t_sp = t.split(":")

                if int(t_sp[0]) == int(sp[0]):
                    if int(t_sp[1]) == int(sp[1]):
                        result_id += 1
                        #print("{:02d}".format(result_id) +  " | " + "{:02d}".format(count) + " | now  | " + routes["time"] + " | " + routes["station"])
                        table.add_row("{:02d}".format(result_id),"{:02d}".format(count),"now","0 min", routes["time"],routes["station"])


                    if int(t_sp[1]) + 1 == int(sp[1]):
                        result_id += 1
                        #print("{:02d}".format(result_id) +  " | " + "{:02d}".format(count) + " | next | " + routes["time"] + " | " + routes["station"])
                        table.add_row("{:02d}".format(result_id),"{:02d}".format(count),"next","1 min",routes["time"],routes["station"])

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
                            #print("{:02d}".format(result_id) +  " | " + "{:02d}".format(count) + " | now  | " + routes["time"] + " | " + routes["station"])
                            table.add_row("{:02d}".format(result_id),"{:02d}".format(count),"now","0 min",routes["time"],routes["station"])

                        else:
                            for i in range(30):

                                if (int(t_sp[1]) + i) == int(sp[1]):
                                    result_id += 1
                                    #print("{:02d}".format(result_id) +  " | " + " | next | " + routes["time"] + " | " + routes["station"])
                                    table.add_row("{:02d}".format(result_id),"{:02d}".format(count),"next", (str(i) + " min"),routes["time"],routes["station"])
                                    break
                

                    elif int(t_sp[0]) + 1 == int(sp[0]):
                        if int(t_sp[1]) == int(sp[1]):
                            result_id += 1
                            #print("{:02d}".format(result_id) +  " | " + " | now  | " + routes["time"] + " | " + routes["station"])
                            table.add_row("{:02d}".format(result_id),"{:02d}".format(count),"now","0 min",routes["time"],routes["station"])


                        else:
                            for i in range(59):

                                if i == int(sp[1]):
                                    result_id += 1
                                    #print("{:02d}".format(result_id) +  " | " + "{:02d}".format(count) + " | next | " + routes["time"] + " | " + routes["station"])

                                    if i == 0:
                                        change_i = 60
                                    else:
                                        change_i = i

                                    arr_in_min = change_i - int(t.split(":")[1])

                                    if arr_in_min < 0:
                                        hours = False
                                        arr_in_min = 60 + arr_in_min
                                    else:
                                        hours = True

                                    if hours:
                                        table.add_row("{:02d}".format(result_id),"{:02d}".format(count),"next",("1 h, " + str(arr_in_min) + " min"),routes["time"],routes["station"])
                                    else:
                                        table.add_row("{:02d}".format(result_id),"{:02d}".format(count),"next",(str(arr_in_min) + " min"),routes["time"],routes["station"])
                                    
                                    break
            
console.print(table)