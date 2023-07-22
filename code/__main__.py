import click
from rocket import Rocket
from settings import (CORE_STAGE, EARTH_MASS, EARTH_RADIUS,
                      EXPLORATION_UPPER_STAGE, INTERIM_CRYOGENIC_STAGE,
                      SOLID_ROCKET_BOOSTERS)
from stage import Stage

import plots


@click.command()
@click.option('--show-plots', is_flag=True)
def run_rocket(show_plots):
    # Create stages and rocket object instances using settings file

    # set initial time, dt, gravity, and eventually air resistance and more complex gravity
    t = 0
    dt = 0.1  # seconds    

    core_stage = Stage(
        dry_mass=CORE_STAGE["Dry Mass"],
        prop_mass=CORE_STAGE["Propellant Mass"],
        mass_flow=CORE_STAGE["Mass Flow"],
        exhaust_v=CORE_STAGE["Exhaust Velocity"],
        ref_area=CORE_STAGE["Reference Area"],
    )
    srb_stage = Stage(
        dry_mass=SOLID_ROCKET_BOOSTERS["Dry Mass"],
        prop_mass=SOLID_ROCKET_BOOSTERS["Propellant Mass"],
        mass_flow=SOLID_ROCKET_BOOSTERS["Mass Flow"],
        exhaust_v=SOLID_ROCKET_BOOSTERS["Exhaust Velocity"],
        ref_area=SOLID_ROCKET_BOOSTERS["Reference Area"],
    )
    interim_stage = Stage(
        dry_mass=INTERIM_CRYOGENIC_STAGE["Dry Mass"],
        prop_mass=INTERIM_CRYOGENIC_STAGE["Propellant Mass"],
        mass_flow=INTERIM_CRYOGENIC_STAGE["Mass Flow"],
        exhaust_v=INTERIM_CRYOGENIC_STAGE["Exhaust Velocity"],
        ref_area=INTERIM_CRYOGENIC_STAGE["Reference Area"],
    )
    exploration_stage = Stage(
        dry_mass=EXPLORATION_UPPER_STAGE["Dry Mass"],
        prop_mass=EXPLORATION_UPPER_STAGE["Propellant Mass"],
        mass_flow=EXPLORATION_UPPER_STAGE["Mass Flow"],
        exhaust_v=EXPLORATION_UPPER_STAGE["Exhaust Velocity"],
        ref_area=EXPLORATION_UPPER_STAGE["Reference Area"],
    )

    rocket = Rocket(core_stage=core_stage, srb_stage=srb_stage, interim_stage=interim_stage, earth_mass=EARTH_MASS, earth_radius=EARTH_RADIUS )

    # Create dictionary and associated keys for use with HUD GUI within pygame
    rocket_parameters = {}
    plots.create_rocket_dict(rocket_parameters)



    # Loop over rocket.update and its related methods while the rocket still has fuel
    while t < 1000:
        t += 0.1
        # fmt: off
        print(f"Time is {t} seconds")
        rocket.update(dt)
        plots.update_rocket_dict(
            rocket_parameters=rocket_parameters, 
            t=t, 
            rocket=rocket, 
            core_stage=core_stage, 
            srb_stage=srb_stage, 
            interim_stage=interim_stage
            )

    if show_plots:
        plots.csv_output(rocket_parameters)
        plots.altitude_plot(rocket_parameters)
        plots.position_plot(rocket_parameters)
        plots.velocity_plot(rocket_parameters)
        plots.acceleration_plot(rocket_parameters)
        plots.force_plot(rocket_parameters)
        plots.fuel_plot(rocket_parameters)
        plots.drag_force_plot(rocket_parameters)
        plots.weight_plot(rocket_parameters)
        plots.gravity_plot(rocket_parameters)
        




if __name__ == '__main__':
    run_rocket()