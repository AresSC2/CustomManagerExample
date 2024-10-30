from typing import Optional

from ares import AresBot
from ares.managers.manager_mediator import ManagerMediator
from ares.managers.hub import Hub

from ares.managers.manager import Manager

from bot.worker_rush_manager import WorkerRushManager


class MyBot(AresBot):
    def __init__(self, game_step_override: Optional[int] = None):
        """Initiate custom bot

        Parameters
        ----------
        game_step_override :
            If provided, set the game_step to this value regardless of how it was
            specified elsewhere
        """
        super().__init__(game_step_override)

    def register_managers(self) -> None:
        """
        Override the default `register_managers` in Ares, so we can
        add our own managers.
        """
        # if we override this we have to setup the mediator
        manager_mediator = ManagerMediator()

        # add custom managers as `additional_managers`
        additional_managers: list[Manager] = [
            WorkerRushManager(self, self.config, manager_mediator),
        ]

        # we also have to setup the manager hub
        # pass in `additional_managers` to the manager
        # custom managers will run after ares managers
        self.manager_hub = Hub(
            self, self.config, manager_mediator, additional_managers=additional_managers
        )

        self.manager_hub.init_managers()


    async def on_step(self, iteration: int) -> None:
        await super(MyBot, self).on_step(iteration)

        # step logic here ...
        pass

    """
    Can use `python-sc2` hooks as usual, but make a call the inherited method in the superclass
    Examples:
    """
    # async def on_start(self) -> None:
    #     await super(MyBot, self).on_start()
    #
    #     # on_start logic here ...
    #
    # async def on_end(self, game_result: Result) -> None:
    #     await super(MyBot, self).on_end(game_result)
    #
    #     # custom on_end logic here ...
    #
    # async def on_building_construction_complete(self, unit: Unit) -> None:
    #     await super(MyBot, self).on_building_construction_complete(unit)
    #
    #     # custom on_building_construction_complete logic here ...
    #
    # async def on_unit_created(self, unit: Unit) -> None:
    #     await super(MyBot, self).on_unit_created(unit)
    #
    #     # custom on_unit_created logic here ...
    #
    # async def on_unit_destroyed(self, unit_tag: int) -> None:
    #     await super(MyBot, self).on_unit_destroyed(unit_tag)
    #
    #     # custom on_unit_destroyed logic here ...
    #
    # async def on_unit_took_damage(self, unit: Unit, amount_damage_taken: float) -> None:
    #     await super(MyBot, self).on_unit_took_damage(unit, amount_damage_taken)
    #
    #     # custom on_unit_took_damage logic here ...
