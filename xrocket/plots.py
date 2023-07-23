import csv


def create_rocket_dict(rocket_parameters):
    # Create dictionary and associated keys for use with HUD GUI within pygame
    rocket_parameters["Time"] = []
    rocket_parameters["Altitude"] = []
    rocket_parameters["X Position"] = []
    rocket_parameters["Velocity"] = []
    rocket_parameters["Acceleration"] = []
    rocket_parameters["Thrust"] = []
    rocket_parameters["Weight"] = []
    rocket_parameters["Gravity Acceleration"] = []
    rocket_parameters["Drag Force"] = []
    rocket_parameters["Resultant Force"] = []
    rocket_parameters["Mach Speed"] = []
    rocket_parameters["Air Density"] = []
    rocket_parameters["Reference Area"] = []
    rocket_parameters["Current Total Mass"] = []
    rocket_parameters["Total Fuel Remaining"] = []
    rocket_parameters["Core Fuel Remaining"] = []
    rocket_parameters["SRB Fuel Remaining"] = []
    rocket_parameters["Interim Fuel Remaining"] = []


def update_rocket_dict(
    rocket_parameters, t, rocket, core_stage, srb_stage, interim_stage
):
    rocket_parameters["Time"].append(t)
    rocket_parameters["Total Fuel Remaining"].append(rocket.total_propellant_mass)
    rocket_parameters["Core Fuel Remaining"].append(core_stage.prop_mass)
    rocket_parameters["SRB Fuel Remaining"].append(srb_stage.prop_mass)
    rocket_parameters["Interim Fuel Remaining"].append(interim_stage.prop_mass)
    rocket_parameters["Current Total Mass"].append(rocket.total_mass)
    rocket_parameters["Altitude"].append(rocket.pos[1])
    rocket_parameters["X Position"].append(rocket.pos[0])
    rocket_parameters["Velocity"].append(rocket.rocket_velocity)
    rocket_parameters["Acceleration"].append(rocket.rocket_acceleration)
    rocket_parameters["Thrust"].append(rocket.thrust)
    rocket_parameters["Drag Force"].append(rocket.drag_force)
    rocket_parameters["Weight"].append(rocket.weight)
    rocket_parameters["Gravity Acceleration"].append(rocket.gravity)
    rocket_parameters["Resultant Force"].append(rocket.resultant_force)
    rocket_parameters["Mach Speed"].append(rocket.mach_speed)
    rocket_parameters["Air Density"].append(rocket.air_density)
    rocket_parameters["Reference Area"].append(rocket.reference_area)


def csv_output(rocket_parameters):
    # fmt: off
    with open("Rocket Values.csv", "w") as new_file:
        writer = csv.writer(new_file)
        key_list = list(rocket_parameters.keys())

        writer.writerow(key_list)
        writer.writerows(zip(*rocket_parameters.values()))


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# WARNING THERE BE PLOTS AHEAD, PROCEED AT YOUR OWN RISK---------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------


def altitude_plot(rocket_parameters, show_plots, save_plots):
    import matplotlib
    import mplcyberpunk
    from matplotlib import pyplot as plt
    from mpl_toolkits import mplot3d
    plt.style.use("cyberpunk")

    # fmt: off
    fig = plt.figure()
    plt.plot(rocket_parameters["Time"],rocket_parameters["Current Total Mass"],label="Current Total Mass",)
    plt.plot(rocket_parameters["Time"],rocket_parameters["Altitude"],label="Altitude",)
    plt.xlabel("Time")
    plt.xscale("linear")
    plt.ylabel("Altitude")
    plt.yscale("linear")
    plt.ticklabel_format(useOffset=False, style="plain")
    plt.legend()
    plt.grid(True)
    mplcyberpunk.make_lines_glow()
    plt.tight_layout()
    if save_plots:
        plt.savefig("Altitude.png", dpi=900)
    if show_plots:
        plt.show()
        
    
def position_plot(rocket_parameters, show_plots, save_plots):
    import matplotlib
    import mplcyberpunk
    from matplotlib import pyplot as plt
    from mpl_toolkits import mplot3d
    plt.style.use("cyberpunk")
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    x_axis = rocket_parameters["Time"]
    y_axis = rocket_parameters["X Position"]
    z_axis = rocket_parameters["Altitude"]
    ax.set_xlabel('Time')
    ax.set_ylabel('X Position')
    ax.set_zlabel('Altitude')
    plt.xscale("linear")
    plt.yscale("linear")
    plt.ticklabel_format(useOffset=False, style="plain")
    ax.plot3D(x_axis,y_axis, z_axis)
    mplcyberpunk.make_lines_glow()
    if show_plots:
        plt.show()
    if save_plots:
        plt.savefig('Position.png', dpi=900)
        

def velocity_plot(rocket_parameters, show_plots, save_plots):
    import matplotlib
    import mplcyberpunk
    from matplotlib import pyplot as plt
    from mpl_toolkits import mplot3d
    plt.style.use("cyberpunk")

    # fmt: off
    fig = plt.figure()

    plt.plot(rocket_parameters["Time"], rocket_parameters["Velocity"],label="Velocity")
    plt.xlabel("Time")
    plt.xscale("linear")
    plt.ylabel("Velocity")
    plt.yscale("linear")
    plt.ticklabel_format(useOffset=False, style="plain")
    plt.legend()
    plt.grid(True)
    mplcyberpunk.make_lines_glow()
    plt.tight_layout()
    if save_plots:
        plt.savefig("Velocity.png", dpi=900)
    if show_plots:
        plt.show()


def acceleration_plot(rocket_parameters, show_plots, save_plots):
    import matplotlib
    import mplcyberpunk
    from matplotlib import pyplot as plt
    from mpl_toolkits import mplot3d
    plt.style.use("cyberpunk")

    # fmt: off
    fig = plt.figure()

    plt.plot(rocket_parameters["Time"],rocket_parameters["Acceleration"],label="Acceleration",)
    plt.xlabel("Time")
    plt.xscale("linear")
    plt.ylabel("Acceleration")
    plt.yscale("linear")
    plt.ticklabel_format(useOffset=False, style="plain")
    plt.legend()
    plt.grid(True)
    mplcyberpunk.make_lines_glow()
    plt.tight_layout()
    if save_plots:
        plt.savefig("Acceleration.png", dpi=900)
    if show_plots:
        plt.show()    


def force_plot(rocket_parameters, show_plots, save_plots):
    import matplotlib
    import mplcyberpunk
    from matplotlib import pyplot as plt
    from mpl_toolkits import mplot3d
    plt.style.use("cyberpunk")

    # fmt: off
    fig = plt.figure()

    plt.plot(rocket_parameters["Time"],rocket_parameters["Drag Force"],label="Drag Force",)
    plt.plot(rocket_parameters["Time"],rocket_parameters["Weight"],label="Weight",)
    plt.plot(rocket_parameters["Time"], rocket_parameters["Thrust"], label="Thrust")
    plt.plot(rocket_parameters["Time"],rocket_parameters["Resultant Force"],label="Resultant Force",)
    plt.xlabel("Time")
    plt.xscale("linear")
    plt.ylabel("Forces")
    plt.yscale('linear')
    plt.ticklabel_format(useOffset=False, style="plain")
    plt.legend()
    plt.grid(True)
    mplcyberpunk.make_lines_glow()
    plt.tight_layout()
    if save_plots:
        plt.savefig("Forces.png", dpi=900)
    if show_plots:
        plt.show()


def fuel_plot(rocket_parameters, show_plots, save_plots):
    import matplotlib
    import mplcyberpunk
    from matplotlib import pyplot as plt
    from mpl_toolkits import mplot3d
    plt.style.use("cyberpunk")

    # fmt: off
    fig = plt.figure()

    # plt.plot(rocket_parameters["Time"],rocket_parameters["Current Total Mass"],label="Current Total Mass",)
    # plt.plot(rocket_parameters["Time"],rocket_parameters["Total Fuel Remaining"],label="Total Fuel Remaining",)
    # plt.plot(rocket_parameters["Time"],rocket_parameters["Core Fuel Remaining"] ,label="Core Fuel Remaining",)
    # plt.plot(rocket_parameters["Time"],rocket_parameters["SRB Fuel Remaining"] ,label="SRB Fuel Remaining",)
    plt.plot(rocket_parameters["Time"],rocket_parameters["Interim Fuel Remaining"] ,label="Interim Fuel Remaining",)
    plt.xlabel("Time")
    plt.xscale("linear")
    plt.ylabel("Mass")
    plt.yscale("linear")
    plt.ticklabel_format(useOffset=False, style="plain")
    plt.legend()
    plt.grid(True)
    mplcyberpunk.make_lines_glow()
    plt.tight_layout()
    if save_plots:
        plt.savefig("Mass.png", dpi=900)
    if show_plots:
        plt.show()


def drag_force_plot(rocket_parameters, show_plots, save_plots):
    import matplotlib
    import mplcyberpunk
    from matplotlib import pyplot as plt
    from mpl_toolkits import mplot3d
    plt.style.use("cyberpunk")

    # fmt: off
    fig = plt.figure()

    plt.plot(rocket_parameters["Time"],rocket_parameters["Drag Force"],label="Drag Force",)
    plt.xlabel("Time")
    plt.xscale("linear")
    plt.ylabel("Drag Force (N)")
    plt.yscale("linear")
    plt.ticklabel_format(useOffset=False, style="plain")
    plt.legend()
    plt.grid(True)
    mplcyberpunk.make_lines_glow()
    plt.tight_layout()
    if save_plots:
        plt.savefig("DragForce.png", dpi=900)
    if show_plots:
        plt.show()


def weight_plot(rocket_parameters, show_plots, save_plots):
    import matplotlib
    import mplcyberpunk
    from matplotlib import pyplot as plt
    from mpl_toolkits import mplot3d
    plt.style.use("cyberpunk")

    # fmt: off
    fig = plt.figure()

    plt.plot(rocket_parameters["Time"],rocket_parameters["Weight"],label="Weight",)
    plt.xlabel("Time")
    plt.xscale("linear")
    plt.ylabel("Weight")
    plt.yscale("linear")
    plt.ticklabel_format(useOffset=False, style="plain")
    plt.legend()
    plt.grid(True)
    mplcyberpunk.make_lines_glow()
    plt.tight_layout()
    if save_plots:
        plt.savefig("Weight.png", dpi=900)
    if show_plots:
        plt.show()


def gravity_plot(rocket_parameters, show_plots, save_plots):
    import matplotlib
    import mplcyberpunk
    from matplotlib import pyplot as plt
    from mpl_toolkits import mplot3d
    plt.style.use("cyberpunk")

    # fmt: off
    fig = plt.figure()

    plt.plot(rocket_parameters["Time"],rocket_parameters["Gravity Acceleration"],label="Gravitational Acceleration",)
    plt.xlabel("Time")
    plt.xscale("linear")
    plt.ylabel("Gravitational Acceleration (m/s^2)")
    plt.yscale("linear")
    plt.ticklabel_format(useOffset=False, style="plain")
    plt.legend()
    plt.grid(True)
    mplcyberpunk.make_lines_glow()
    plt.tight_layout()
    if save_plots:
        plt.savefig("Gravity.png", dpi=900)
    if show_plots:
        plt.show()
        
        
def create_plots(rocket_parameters, show_plots, save_plots):
    if not show_plots and not save_plots:
        return
    
    altitude_plot(rocket_parameters, show_plots, save_plots)
    velocity_plot(rocket_parameters, show_plots, save_plots)
    acceleration_plot(rocket_parameters, show_plots, save_plots)
    force_plot(rocket_parameters, show_plots, save_plots)
    fuel_plot(rocket_parameters, show_plots, save_plots)
    drag_force_plot(rocket_parameters, show_plots, save_plots)
    weight_plot(rocket_parameters, show_plots, save_plots)
    gravity_plot(rocket_parameters, show_plots, save_plots)
    position_plot(rocket_parameters, show_plots, save_plots)
