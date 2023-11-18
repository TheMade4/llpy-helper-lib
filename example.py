# region import example

from typing import TYPE_CHECKING, Any

# I suggest not importing the package at runtime and providing type hints only in development
# this way, you don't have to install it as a plugin dependency
if TYPE_CHECKING:
    # you can input any ll's built-ins from `llpy`
    from llpy import *

    # you can input types provided by llpy from `llpy.types`
    # (add quotes when using these types because you didn't import it at runtime)
    from llpy.types import *

# endregion


# region register a listener example

# register manually
mc.listen("onServerStarted", lambda: colorLog("green", "The Server Started!"))


# or you can use the decorator from BaseLib (no type hints) :(
@handle("onJoin")
def _(player: LLSE_Player):
    logger.info(f"Player {player.realName} joined the server!")


# endregion


# region register a command example

# register a command
cmd = mc.newCommand("testcmd", "A Test Command", PermType.Any)
cmd.optional("input", ParamType.RawText)
cmd.overload(["input"])


# set callback using decorator from BaseLib
@cmd.handle
def _(_, ori: LLSE_CommandOrigin, out: LLSE_CommandOutput, res: dict[str, Any]):
    arg: str | None = res.get("input")
    tip = f'§aYou inputed §r"§6§l{arg}§r"' if arg else "§cNothing inputted!"

    player = ori.player
    if player:
        # if player exec the cmd, send a form
        form = mc.newSimpleForm().setTitle("Test Form").setContent(tip)
        player.sendForm(form, lambda _, __: None)

    else:
        # if not, send output to console
        out.success(tip) if arg else out.error(tip)

    return True


cmd.setup()  # set up it

# endregion


# and more...


# set plugin metadata
ll.registerPlugin(
    "example",
    "An example plugin",
    [0, 0, 1, Version.Dev],
    {"Author": "student_2333"},
)
