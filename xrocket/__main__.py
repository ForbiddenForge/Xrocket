import logging

import click

from xrocket.plots import (
    create_plots,
    create_rocket_dict,
    csv_output,
    update_rocket_dict,
)
from xrocket.rocket import Rocket
from xrocket.settings import (
    CORE_STAGE,
    EARTH_MASS,
    EARTH_RADIUS,
    EXPLORATION_UPPER_STAGE,
    INTERIM_CRYOGENIC_STAGE,
    SOLID_ROCKET_BOOSTERS,
)
from xrocket.stage import Stage

LOG = logging.getLogger(__name__)


def log_setup(log_level):
    logger = logging.getLogger()
    logger.setLevel(log_level)

    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)

    logger.addHandler(ch)


@click.command()
@click.option("--show-plots", is_flag=True)
@click.option("--save-plots", is_flag=True)
@click.option("--verbose", is_flag=True)
def run_rocket(show_plots, save_plots, verbose):
    if verbose:
        log_setup(logging.DEBUG)
    else:
        log_setup(logging.ERROR)

    # Create stages and rocket object instances using settings file

    # set initial time, dt, gravity, and eventually air resistance and more complex gravity
    t = 0
    dt = 0.01  # seconds

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

    rocket = Rocket(
        core_stage=core_stage,
        srb_stage=srb_stage,
        interim_stage=interim_stage,
        exploration_stage=exploration_stage,
        earth_mass=EARTH_MASS,
        earth_radius=EARTH_RADIUS,
    )

    # Create dictionary and associated keys for use with HUD GUI within pygame
    rocket_parameters = {}
    create_rocket_dict(rocket_parameters)

    # Loop over rocket.update and its related methods while the rocket still has fuel
    while t < 3000:
        t += 0.01
        # fmt: off
        LOG.debug(f"Time is {t} seconds")
        rocket.update(dt)
        if show_plots or save_plots:
            update_rocket_dict(
                rocket_parameters=rocket_parameters,
                t=t,
                rocket=rocket,
                core_stage=core_stage,
                srb_stage=srb_stage,
                interim_stage=interim_stage,
                exploration_stage=exploration_stage
                )

    if show_plots or save_plots:
        csv_output(rocket_parameters)

    create_plots(rocket_parameters, show_plots, save_plots)


if __name__ == "__main__":
    run_rocket()
